import cv2
import glob
from ultralytics import YOLO
# colocar as imagens para prever nesse diretório
input = "input"

for filename in glob.glob("input/*.*"):
    imagem = cv2.imread(filename)
    if imagem is None:
        continue

    # Carrega o modelo treinado
    # # dataset com 200 imagens
    # model = YOLO("yolo_novo_dataset/exp1/weights/best.pt") 
    # # dataset com 25 imagens - melhor
    model = YOLO("yolo_chocolate/exp1/weights/best.pt")

    # Detecta as gotas (gera boxes)
    results = model.predict(source=filename, conf=0.5, save=True, show=True)

    # Conta quantas detecções houve
    num_gotas = len(results[0].boxes)
    
    print(f"Quantidade de gotas detectadas: {num_gotas}")


# o resultado sai em runs