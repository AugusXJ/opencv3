import cv2

grayImage = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('1.png', grayImage)