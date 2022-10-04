import cv2
import numpy as np

img = cv2.imread('test.jpg')
print(img.shape)
cv2.imshow("Original", img)

#Cropping an image
cropped_image = img[80:280, 150:330]

#Display cropped image
cv2.imshow("Cropped", cropped_image)

#Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows
