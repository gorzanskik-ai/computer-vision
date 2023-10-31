import cv2
import numpy as np


def nothing(x):
    pass


img = np.ones((300, 500, 3), dtype='uint8')
cv2.namedWindow('Palette')

cv2.createTrackbar('Red', 'Palette', 0, 255, nothing)
cv2.createTrackbar('Green', 'Palette', 0, 255, nothing)
cv2.createTrackbar('Blue', 'Palette', 0, 255, nothing)

while True:
    cv2.imshow('Palette', img)

    r = cv2.getTrackbarPos('Red', 'Palette')
    g = cv2.getTrackbarPos('Green', 'Palette')
    b = cv2.getTrackbarPos('Blue', 'Palette')

    img[:] = [b, g, r]

    if cv2.waitKey(1) & 0xFF == ord('q'):   #press q to close window
        break

cv2.destroyAllWindows()
