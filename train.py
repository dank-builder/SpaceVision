from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Use the model
model.train(data="./data/data.yaml", epochs=300, plots="true", imgSz="640")
metrics = model.val()