import cv2

image = cv2.imread('test.jpg')

cv2.imshow("Original Image", image)
cv2.waitKey(0)

if image is None:
    print("Could not read image")

imageLine = image.copy()
pointA = (200, 80)
pointB = (450, 80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow("Image Line", imageLine)
cv2.waitKey(0)