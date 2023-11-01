import cv2

og_img = cv2.imread(r'images\poland.png')
img = og_img.copy()
# cv2.imshow('poland', img)

#adding white frame to image to avoid stick pixels with window frame
img = cv2.copyMakeBorder(src=img, top=20, bottom=20, left=20, right=20,
                         borderType=cv2.BORDER_CONSTANT, value=(255, 255, 255))

#convert into gray scale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

#mask
mask = cv2.threshold(src=gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)

#contours
contours = cv2.findContours(image=mask, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'length of contours: {len(contours)}')

#draw contours
img = cv2.drawContours(image=img, contours=[contours[0]], contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow('contour', img)
cv2.waitKey(0)

contour = contours[0]
leftmost = contour[contour[:, :, 0].argmin()][0]
rightmost = contour[contour[:, :, 0].argmax()][0]
topmost = contour[contour[:, :, 1].argmin()][0]
bottommost = contour[contour[:, :, 1].argmax()][0]

for point in [leftmost, rightmost, topmost, bottommost]:
    cv2.circle(img, center=tuple(point), radius=10, color=(0, 0, 255), thickness=-1)

cv2.imshow('extreme_points', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

