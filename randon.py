import os
import shutil
import random

# Diretórios originais
images_dir = "novo_dataset/cookies/images"
labels_dir = "novo_dataset/cookies/labels"

# Diretórios destino
train_img_dir = "novo_dataset/images/train"
val_img_dir = "novo_dataset/images/val"
train_label_dir = "novo_dataset/labels/train"
val_label_dir = "novo_dataset/labels/val"

# Criar pastas se não existirem
for d in [train_img_dir, val_img_dir, train_label_dir, val_label_dir]:
    os.makedirs(d, exist_ok=True)

# Lista de imagens
all_images = [f for f in os.listdir(images_dir) if f.endswith((".jpg", ".jpeg", ".png"))]
random.shuffle(all_images)

# Proporção treino/val (ex: 80% treino, 20% validação)
train_ratio = 0.8
train_count = int(len(all_images) * train_ratio)

train_images = all_images[:train_count]
val_images = all_images[train_count:]

# Função para copiar imagens e labels
def copy_files(images, img_src_dir, label_src_dir, img_dst_dir, label_dst_dir):
    for img_file in images:
        base_name = os.path.splitext(img_file)[0]
        # Copia imagem
        shutil.copy(os.path.join(img_src_dir, img_file), os.path.join(img_dst_dir, img_file))
        # Copia label
        label_file = base_name + ".txt"
        shutil.copy(os.path.join(label_src_dir, label_file), os.path.join(label_dst_dir, label_file))

# Copiar arquivos
copy_files(train_images, images_dir, labels_dir, train_img_dir, train_label_dir)
copy_files(val_images, images_dir, labels_dir, val_img_dir, val_label_dir)

print(f"Treino: {len(train_images)} imagens, Validação: {len(val_images)} imagens")
