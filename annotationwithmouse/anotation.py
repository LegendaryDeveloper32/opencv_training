import cv2
top_left_corner = []
bottom_right_corner = []

def drawRectangle(action, x, y, flags, *userdata):
    global top_left_corner, bottom_right_corner

    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner=[(x, y)]
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner=[(x, y)]

        cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0), 2, 8)
        cv2.imshow("Window", image)

image = cv2.imread("test.jpg")
temp = image.copy()

cv2.namedWindow("Window")
cv2.setMouseCallback("Window", drawRectangle)

k = 0
while k!= 113:
    cv2.imshow("Window", image)
    k = cv2.waitKey(0)
    if(k == 99):
        image = temp.copy()
        cv2.imshow("Window", image)

cv2.destroyAllWindows()