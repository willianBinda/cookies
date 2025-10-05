from ultralytics import YOLO
import cv2

# Carrega o modelo treinado
model = YOLO("yolo_chocolate/exp1/weights/best.pt")

# Caminho da imagem do cookie
img_path = "images.jpeg"

# Detecta as gotas (gera boxes)
results = model.predict(source=img_path, conf=0.5, save=True, show=True)

# Conta quantas detecções houve
num_gotas = len(results[0].boxes)
print(f"Quantidade de gotas detectadas: {num_gotas}")

# (Opcional) Se quiser salvar a imagem manualmente com OpenCV:
annotated_frame = results[0].plot()  # desenha as detecções
cv2.imwrite("resultado_cookie.jpg", annotated_frame)