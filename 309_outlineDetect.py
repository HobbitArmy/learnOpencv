# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:55:41 2017

@author: Green
"""

import cv2
import numpy as np

img = np.zeros((200, 200), dtype = np.uint8) # 创建 200x200 大小的黑色空白图像
img[30:60, 50:150] = 255 # 在图像中放置一个 白色(255) 矩形块
ret, thresh = cv2.threshold(img.copy(), 127, 255, 0) # 对图像二值化操作，以127为阈值
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.findContours 传入参数: 输入图像；层次类型；轮廓逼近法; 该函数会修改输入图像，可用 img.copy() 作为输入
# 层次树 可作修改 cv2.RETR_TREE 会得到图像中轮廓的整体层次结构; cv2.RETR_EXTERNAL 只会得到最外的轮廓
# 函数有三个返回值: 修改后图像；图像轮廓；它们的层次

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# CvtColor是颜色空间转换函数，可以实现RGB颜色向HSV，HSI等颜色空间的转换，也可以转换为灰度图像
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2) # 画出图像轮廓

cv2.imshow('contours', color)
cv2.waitKey()
cv2.destroyAllWindows()



