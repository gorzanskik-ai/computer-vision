import cv2
import imutils
import numpy as np

view = cv2.imread(r'images\view.jpg')
cube = cv2.imread(r'images\cube.jpg')
cube = imutils.resize(cube, height=150)

# cv2.imshow('view', view)
# cv2.imshow('tesla', tesla)
# cv2.waitKey(0)

rows, cols, channels = cube.shape
roi = view[:rows, :cols]    #roi - region of interest
cv2.imshow('roi', roi)
cv2.waitKey(0)

#gray scale
gray = cv2.cvtColor(src=cube, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(0)

#threshold
mask = cv2.threshold(src=gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1]   #pixel <220 (black) others white
cv2.imshow('mask', mask)
cv2.waitKey(0)

mask_inv = np.bitwise_not(mask)     #inverse
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(0)

view_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)    #bg - background white -> img
cube_fg = cv2.bitwise_and(src1=cube, src2=cube, mask=mask_inv)  #fg - foreground
cv2.imshow('view_bg', view_bg)
cv2.imshow('cube_fg', cube_fg)
cv2.waitKey(0)


dst = cv2.add(src1=view_bg, src2=cube_fg)
view[:rows, :cols] = dst
cv2.imshow('out', view)
cv2.waitKey(0)

cv2.destroyAllWindows()

