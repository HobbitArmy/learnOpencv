# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:09:49 2017

@author: Green
"""
#高通滤波器 high pass filter : 根据像素与临近像素的亮度差值 来提升该像素的亮度.
#而低通滤波器 low pass filter : 当像素与周围像素差值小于特定值时,平滑该像素,主要用于去噪和模糊.
import cv2
import numpy as np
from scipy import ndimage
# 自定义卷积核 : 
kernel_3x3 = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])
kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                       [-1,-1,4,-1,-1],
                       [-1,4,6,4,-1],
                       [-1,-1,4,-1,-1],
                       [-1,-1,-1,-1,-1]])
img = cv2.imread('RC.png', 0)
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)
# 高斯模糊 是常用的平滑滤波器,是一削弱高频信号的低通滤波器
blurred = cv2.GaussianBlur(img, (11,11), 0)
g_hpf = img - blurred

cv2.imshow('3x3', k3)
cv2.imshow('5x5', k5)
cv2.imshow('g_hpf', g_hpf)
cv2.imshow('blurred', blurred)
cv2.waitKey()
cv2.destroyAllWindows()


