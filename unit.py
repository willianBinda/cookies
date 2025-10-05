import os
import cv2
from glob import glob

# Diretório das imagens
images_dir = "novo_dataset/cookies/images"

# Diretório para salvar imagens processadas (pode ser o mesmo se quiser sobrescrever)
output_dir = "novo_dataset/cookies/images_renamed"
os.makedirs(output_dir, exist_ok=True)

# Tamanho padrão para YOLO (pode ajustar)
width, height = 416, 416

# Pegar todas as imagens com extensões comuns
image_paths = glob(os.path.join(images_dir, "*.*"))
image_paths = [p for p in image_paths if p.lower().endswith((".jpg", ".jpeg", ".png"))]

if not image_paths:
    print("[INFO] Nenhuma imagem encontrada.")
else:
    print(f"[INFO] {len(image_paths)} imagens encontradas. Processando...")

for idx, img_path in enumerate(sorted(image_paths), start=1):
    # Ler imagem
    img = cv2.imread(img_path)
    if img is None:
        print(f"[WARNING] Não foi possível ler a imagem {img_path}")
        continue

    # Redimensionar
    img_resized = cv2.resize(img, (width, height))

    # Novo caminho
    new_filename = f"{idx}.jpg"
    new_path = os.path.join(output_dir, new_filename)

    # Salvar imagem
    cv2.imwrite(new_path, img_resized)

print(f"[INFO] {len(image_paths)} imagens renomeadas e redimensionadas para '{output_dir}' com sucesso!")
