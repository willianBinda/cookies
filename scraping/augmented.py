import os
import cv2
import albumentations as A
from glob import glob

# Diretórios
images_dir = "dataset_cookies/images"
labels_dir = "dataset_cookies/labels"
aug_images_dir = "augmented_dataset/images"
aug_labels_dir = "augmented_dataset/labels"

os.makedirs(aug_images_dir, exist_ok=True)
os.makedirs(aug_labels_dir, exist_ok=True)

# Transformações de Data Augmentation
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=30, p=0.5),
    A.RandomScale(scale_limit=0.2, p=0.5)
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

# Contador para novas imagens
counter = 1

# Percorre todas as imagens
for img_path in glob(os.path.join(images_dir, "*.jpg")):
    base_name = os.path.basename(img_path).split(".")[0]

    # Lê imagem
    img = cv2.imread(img_path)

    # Lê labels do YOLO
    txt_path = os.path.join(labels_dir, base_name + ".txt")
    bboxes = []
    class_labels = []
    if os.path.exists(txt_path):
        with open(txt_path, "r") as f:
            for line in f.readlines():
                parts = line.strip().split()
                class_id = int(parts[0])
                bbox = [float(x) for x in parts[1:]]  # x_center, y_center, w, h (normalizado)
                bboxes.append(bbox)
                class_labels.append(class_id)

    # Aplica Data Augmentation várias vezes por imagem
    for i in range(5):  # gera 5 variações por imagem
        augmented = transform(image=img, bboxes=bboxes, class_labels=class_labels)
        aug_img = augmented['image']
        aug_bboxes = augmented['bboxes']

        # Salva imagem
        new_img_name = f"cookie_{counter:04d}.jpg"
        cv2.imwrite(os.path.join(aug_images_dir, new_img_name), aug_img)

        # Salva labels
        new_txt_name = f"cookie_{counter:04d}.txt"
        with open(os.path.join(aug_labels_dir, new_txt_name), "w") as f:
            for cls, bbox in zip(class_labels, aug_bboxes):
                line = f"{cls} {' '.join([str(x) for x in bbox])}\n"
                f.write(line)

        counter += 1

print(f"[INFO] Dataset aumentado! Total de imagens: {counter-1}")