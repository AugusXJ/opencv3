# -*- coding: utf-8 -*-
"""
@Time    : 09/06/18 09:07
@Author  : XJH
"""

# 3.2.1 高通滤波器
import cv2
import numpy as np
from scipy import ndimage
from skimage import io

kernel_3x3 = np.array([[-1, -1, -1],
                      [-1, 8, -1],
                      [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                      [-1, 1, 2, 1, -1],
                      [-1, 2, 4, 2, -1],
                      [-1, 1, 2, 1, -1],
                      [-1, -1, -1, -1, -1]])
img = io.imread('../test.jpg', as_gray=True)
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)
blurred = cv2.GaussianBlur(img, (11, 11), 0)            # 高斯滤波
g_hpf = img - blurred
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpef", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()