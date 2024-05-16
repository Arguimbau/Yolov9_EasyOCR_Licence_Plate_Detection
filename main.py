import easyocr
from yolov9 import YOLOv9

# Predict with yolov9 with out weights
yolov9.predict('sample.jpg')


reader = easyocr.Reader(['en'])


result = reader.readtext('sample.jpg')

for(bbox, text, prob) in result:
    print(f'Detected text: {text} with probability {prob}')