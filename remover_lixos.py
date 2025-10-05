import os
from glob import glob

# Diretórios
images_dir = "novo_dataset/cookies/images"
labels_dir = "novo_dataset/cookies/labels"

# Pegar todas as imagens jpg
image_paths = glob(os.path.join(images_dir, "*.jpg"))

if not image_paths:
    print("[INFO] Nenhuma imagem encontrada.")
else:
    removed_count = 0
    for img_path in image_paths:
        # Nome do arquivo sem extensão
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        # Caminho do arquivo txt correspondente
        label_path = os.path.join(labels_dir, f"{base_name}.txt")
        
        # Verifica se o label existe
        if not os.path.exists(label_path):
            os.remove(img_path)
            removed_count += 1
            print(f"[REMOVIDO] {img_path} (arquivo txt não encontrado)")

    print(f"[INFO] Processo finalizado. {removed_count} imagens removidas.")
