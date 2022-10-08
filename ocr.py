import cv2
from PIL import Image
from pytesseract import pytesseract
import numpy as np

cap = cv2.VideoCapture(0)     #read webcam
#cap = cv2.VideoCapture('http://192.168.1.6:8080/video')    #read mobile cam

while True:
  ret,frame = cap.read()
  resized = cv2.resize(frame,(600,400))
  cv2.imshow("Frame",frame)

  if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite('test2.jpg',frame)
        break

cap.release()
cv2.destroyAllWindows()

#filename = 'test1.jpg'
#img1 = np.array(Image.open(filename))
#text = pytesseract.image_to_string(img1)
#print(text)

def tesseract():
    path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    image_path = "test2.jpg"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)
    # print(text[:-1])
tesseract()
