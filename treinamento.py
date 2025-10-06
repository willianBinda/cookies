
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


# Treinar normalmente
model.train(
    data="dataset_cookies.yaml",
    epochs=100,
    imgsz=640,
    batch=4,
    project="yolo_novo_dataset",
    name="exp1",
    exist_ok=True
)