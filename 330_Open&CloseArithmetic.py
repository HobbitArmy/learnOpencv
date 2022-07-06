# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:50:44 2018

@author: Green
"""

import cv2
img = cv2.imread('fly.jpg', 0)
ret1, thresh1 = cv2.threshold(img, 0, 255, 
                            cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# OpenCV定义的结构元素  
eroded = cv2.erode(img, kernel) # 腐蚀图像 
dilated = cv2.dilate(img, kernel) # 膨胀图像 
'''cv2.imshow('origin', img)
cv2.imshow('thresh', thresh1)
cv2.imshow('eroded', eroded)
cv2.imshow('dilated', dilated)
cv2.waitKey()
cv2.destroyAllWindows()'''

## 开运算和闭运算就是将腐蚀和膨胀按照一定的次序进行处理。
## 但这两者并不是可逆的，即先开后闭并不能得到原先的图像
## morphologyEx : 形态学变换
closed = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
opened = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
'''cv2.imshow('closed', closed)
cv2.imshow('opened', opened)
cv2.waitKey()
cv2.destroyAllWindows()'''

##膨胀时，图像中的物体会想周围“扩张”；腐蚀时，图像中的物体会“收缩”。
##比较这两幅图像，由于其变化的区域只发生在边缘。所以这时将两幅图像相减，
##得到的就是图像中物体的边缘。 ***检测边缘***
result = cv2.absdiff(dilated, eroded)
retcal, result = cv2.threshold(result, 40, 255,
                               cv2.THRESH_BINARY_INV)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()