from ultralytics import YOLO

# Load a model
model = YOLO('saved_model.pt')  # pretrained YOLOv8n model

results = model.predict('1ea21011-PICT0105.JPG')
for r in results:
    print(r.obb)  # print the OBB object containing the oriented detection bounding boxes