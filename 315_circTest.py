# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:38:51 2017

@author: Green
"""
    
import cv2
import numpy as np

img = cv2.imread('SR2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray, 5)# 中值滤波(Median filter)
# 用像素点邻域灰度值的中值来代替该像素点的灰度值,去噪的同时又能保留图像边缘细节
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, minDist = 120,
                    param1 = 100, param2 = 3, minRadius = 20, maxRadius = 30)
# 参数 , img:输入图像; cv2.HOUGH_GRADIENT:Hough 变换方式; 1 :累加器图像的分辨率,设置为1设置为1不变;
# minDist = 120 :两个不同圆之间的最小距离; param1 = 100 :边缘阀值上限; param2 = 3 :累加器的阀值;
# minRadius :最小圆半径 ; maxRadius = 0 :最大圆半径;
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imwrite('circles.jpg', img)
cv2.imshow('circles.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()