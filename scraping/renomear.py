import os

# Caminho da pasta com as imagens
directory = "dataset_cookies/images"  # altere para o seu diretório

# Lista todos os arquivos no diretório e filtra apenas .jpg
images = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

# Ordena os arquivos (opcional, para manter ordem)
images.sort()

# Renomeia cada arquivo
for idx, filename in enumerate(images, start=1):
    # Novo nome com 2 dígitos: 01.jpg, 02.jpg ...
    new_name = f"{idx:02d}.jpg"
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_name)
    
    # Renomeia
    os.rename(old_path, new_path)

print(f"[INFO] Renomeadas {len(images)} imagens no diretório '{directory}'.")