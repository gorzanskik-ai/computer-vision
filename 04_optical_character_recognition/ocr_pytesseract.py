import pytesseract
from PIL import Image
import imutils
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ocr(file):
    return pytesseract.image_to_string(image=Image.open(file))


filename = r'images\3.png'
img = cv2.imread(filename)

print(ocr(filename))
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
