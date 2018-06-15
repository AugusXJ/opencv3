# -*- coding: utf-8 -*-
"""
@Time    : 14/06/18 18:07
@Author  : XJH
"""

import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
ret, thresh = cv2.threshold(img, 127, 255, 0)       # 图像二值化
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)       # 转RGB
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)     # 对countour着色
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
