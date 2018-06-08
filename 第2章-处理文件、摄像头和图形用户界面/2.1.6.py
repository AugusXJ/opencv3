"""
2.1.6 在窗口显示图像
"""
import cv2
import numpy as np

img = cv2.imread('test.jpg')
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()