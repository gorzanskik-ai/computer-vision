import cv2

img = cv2.imread(r'images\grey.png')
print(img)
cv2.imshow('gray', img)
cv2.waitKey(0)

thresh_binary = cv2.threshold(src=img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow('thresh', thresh_binary)
cv2.waitKey(0)

for thresh in [0, 50, 100, 150, 200]:
    thresh_binary = cv2.threshold(src=img, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.putText(
        img=thresh_binary,
        text=f'{thresh}',
        org=(20, 40),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.5,
        color=(255, 255, 255),
        thickness=2)
    cv2.imshow(f'thresh_binary', thresh_binary)
    cv2.waitKey(2000)

cv2.destroyAllWindows()
