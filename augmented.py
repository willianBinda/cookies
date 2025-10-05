import os
import cv2
import albumentations as A
from glob import glob

# Diretórios
images_dir = "scraping/dataset_cookies/images"
labels_dir = "scraping/dataset_cookies/labels"
aug_images_dir = "scraping/augmented_dataset/images"
aug_labels_dir = "scraping/augmented_dataset/labels"

os.makedirs(aug_images_dir, exist_ok=True)
os.makedirs(aug_labels_dir, exist_ok=True)

# Transformações de Data Augmentation
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=30, p=0.5),
    A.RandomScale(scale_limit=0.2, p=0.5)
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

counter = 1

# Coleta todas as imagens
image_paths = glob(os.path.join(images_dir, "*.jpg")) + \
              glob(os.path.join(images_dir, "*.jpeg")) + \
              glob(os.path.join(images_dir, "*.png"))

# Loop pelas imagens
for img_path in image_paths:
    base_name = os.path.splitext(os.path.basename(img_path))[0]

    img = cv2.imread(img_path)

    # Lê labels do YOLO
    txt_path = os.path.join(labels_dir, base_name + ".txt")
    bboxes, class_labels = [], []

    if os.path.exists(txt_path):
        with open(txt_path, "r") as f:
            for line in f.readlines():
                parts = line.strip().split()
                class_id = int(parts[0])
                bbox = [float(x) for x in parts[1:]]  # x_center, y_center, w, h
                bboxes.append(bbox)
                class_labels.append(class_id)

    # Aplica Data Augmentation
    for i in range(5):  # gera 5 variações por imagem
        augmented = transform(image=img, bboxes=bboxes, class_labels=class_labels)
        aug_img = augmented["image"]
        aug_bboxes = augmented["bboxes"]
        aug_labels = augmented["class_labels"]

        # Salva imagem aumentada
        new_img_name = f"cookie_{counter:04d}.jpg"
        cv2.imwrite(os.path.join(aug_images_dir, new_img_name), aug_img)

        # Salva label aumentada (classe como int)
        new_txt_name = f"cookie_{counter:04d}.txt"
        with open(os.path.join(aug_labels_dir, new_txt_name), "w") as f:
            for cls, bbox in zip(aug_labels, aug_bboxes):
                cls = int(cls)  # <---- forçar inteiro
                bbox_str = " ".join(f"{x:.6f}" for x in bbox)  # limitar casas decimais
                f.write(f"{cls} {bbox_str}\n")

        counter += 1

print(f"[INFO] Dataset aumentado! Total de imagens geradas: {counter - 1}")