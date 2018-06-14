# -*- coding: utf-8 -*-
"""
@Time    : 14/06/18 17:33
@Author  : XJH
"""

import cv2
import numpy as np

img = cv2.imread('../test.jpg')

cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
cv2.imshow("Canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()