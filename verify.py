import os

image_folder = "dataset_cookies/images/train"
label_folder = "dataset_cookies/labels/train"

images = os.listdir(image_folder)
labels = os.listdir(label_folder)

for img in images:
    label_file = img.replace(".jpg", ".txt")
    if label_file not in labels:
        print(f"Faltando label para {img}")