from PIL import Image
import os

# Pasta onde estão suas imagens
folder = "dataset_cookies/images/val"

for filename in os.listdir(folder):
    if filename.lower().endswith(".jpeg"):
        filepath = os.path.join(folder, filename)
        img = Image.open(filepath)
        
        # Novo nome com extensão .jpg
        new_filename = filename.rsplit(".", 1)[0] + ".jpg"
        new_filepath = os.path.join(folder, new_filename)
        
        # Salvar como JPG
        img.convert("RGB").save(new_filepath, "JPEG")
        
        # Remover arquivo .jpeg original
        os.remove(filepath)
        print(f"Convertido: {filename} -> {new_filename}")