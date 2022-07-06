# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:32:57 2017

@author: Green
"""

import cv2
img = cv2.imread('RC.png')
img[:100, 50] = [255, 255, 255]
img.itemset( (200, 200, 1), 255) # itemset()函数 传入(x,y,index)&要设定的值；来改变像素在指定通道的值
cv2.imshow('3021', img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('RC.png')
img[:, :, 0] = 100
cv2.imshow('3022', img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('RC.png')
tree = img[0:100, 0:100]
img[499:599, 0:100] = tree
cv2.imshow('3023', img)
cv2.waitKey()
cv2.destroyAllWindows()
# 打印图像属性 shape:高度 宽度 通道数(仅彩色有); size:像素大小;
# datatype:图像数据类型,常为无符号整型变量 + 类型占位数 (eg: uint8 )
print(img.shape);print(img.size);print(img.dtype)
