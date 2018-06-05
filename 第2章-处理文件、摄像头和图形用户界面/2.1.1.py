"""
2.1.1 读写图像文件
"""
import cv2

grayImage = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('test.png', grayImage)