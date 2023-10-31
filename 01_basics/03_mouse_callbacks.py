import cv2


def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:  # double click left mouse button
        print(f'x = {x}, y = {y}')


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(
            img=img,
            center=(x, y),
            radius=50,
            color=(0, 255, 0),
            thickness=2
        )


img = cv2.imread(r'images\tesla.jpg')

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

# cv2.setMouseCallback('image', get_position)
# cv2.imshow('image', img)
# cv2.waitKey(0)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #press q to close window
        break

cv2.destroyAllWindows()

