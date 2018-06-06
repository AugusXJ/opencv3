"""
2.1.3 使用numpy.array访问图像数据
"""
import cv2
import numpy as np

# # 改变RHB图像在(0, 0)处的像素，改变为白像素
# img = cv2.imread('test.jpg')
# img[0, 0] = [255, 255, 255]
# cv2.imshow('result.jpg', img)
# cv2.waitKey(0)

# item()和itemset()的使用
# img = cv2.imread('test.jpg')
# print(img.item(150, 120, 0))            # 查看Blue通道的值
# img.itemset((150, 120, 0), 255)
# print(img.item(150, 120, 0))

# 索引操作
# img = cv2.imread('test.jpg')
# img[:, :, 1] = 110
# cv2.imshow('result.jpg', img)
# cv2.waitKey(0)

# ROI区域
# img = cv2.imread('test.jpg')
# my_roi = img[0:100, 0:100]
# img[200:300, 300:400] = my_roi
# cv2.imshow('result.jpg', img)
# cv2.waitKey(0)

# 图片属性
# img = cv2.imread('test.jpg')
# print(img.shape)
# print(img.size)
# print(img.dtype)


