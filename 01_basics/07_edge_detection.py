import cv2
import imutils
import numpy as np

img = cv2.imread(r'images\guido.jpg')
img = imutils.resize(image=img, height=500)
cv2.imshow('guido', img)

canny = cv2.Canny(image=img, threshold1=250, threshold2=250)
cv2.imshow('canny', canny)
cv2.waitKey(0)

thresholds = np.arange(0, 251, 25)
for threshold in thresholds:
    canny = cv2.Canny(image=img, threshold1=threshold, threshold2=threshold)
    cv2.putText(
        img=canny,
        text=f'{threshold}',
        org=(20, 40),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.5,
        color=(255, 255, 255),
        thickness=2)
    cv2.imshow(f'canny thresholds', canny)
    cv2.waitKey(2000)

cv2.destroyAllWindows()

