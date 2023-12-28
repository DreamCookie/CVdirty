#pip install -r req.txt
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

img = cv2.imread("2.png")
img = cv2.resize(img, (img.shape[1]//2,img.shape[1]//2 ))
result = model(img, show=True)
k = cv2.waitKey(0) & 0xFF
print(k)
if k == 27:  # close on ESC key
    cv2.destroyAllWindows()