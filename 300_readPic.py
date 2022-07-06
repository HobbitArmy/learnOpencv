# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:30:01 2017

@author: Green
"""

import numpy as np
img = np.zeros((3, 3), dtype = np.uint8)
img.shape # 返回行和列
print(img)
import cv2
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print('\n \n');print(img)
img.shape # 如果有一个以上通道 还会返回通道数

image = cv2.imread('RC.jpg')
cv2.imwrite('RC.png', image) # 转换格式

grayImage = cv2.imread('RC.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('RC_GRAY.png', grayImage) # 转化为灰度的PNG图像

byteArray = bytearray(image) # 将 8位通道的 图像转化为标准的 一维 Python bytearray 格式
# bytearray 含有恰当顺序的字节，可以显示转化和重构 得到 numpy.array形式的图像 ：
bgrImage = np.array(byteArray).reshape(600, 400, 3) # 第三个值 为颜色通道
cv2.imshow('300', bgrImage)

#cv2.imshow('B',image[:,:,0])
#cv2.imshow('G',image[:,:,1])
#cv2.imshow('R',image[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()