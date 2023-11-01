import cv2

og_img = cv2.imread(r'images\python.png')
img = og_img.copy()
cv2.imshow('python', img)

#convert into gray scale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#mask
mask = cv2.threshold(src=gray, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow('mask', mask)

#contour detection
contours = cv2.findContours(image=mask, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'length of contours: {len(contours)}')
print('single contour:', contours[0])

img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[4]], contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow('img_cnt', img_cnt)

#area of single contour
area = cv2.contourArea(contour=contours[4], oriented=True)
print(area)

#calculate area of each contour and pick max
areas = []
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour=contour, oriented=True)
    areas.append((idx, area))

print('areas:', areas)
print('max area:', max(areas, key=lambda x: x[1]))
max_idx, max_area = max(areas, key=lambda x: x[1])
img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[max_idx]],
                           contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow('max_cnt_area', img_cnt)
cv2.waitKey(0)

#length of sing contour
length = cv2.arcLength(curve=contours[max_idx], closed=True)
print('length of max area contour:', length)

cv2.destroyAllWindows()
