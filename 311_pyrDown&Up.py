# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:52:29 2017

@author: Green
"""

import cv2
import matplotlib.pyplot as plt 
img0 = cv2.imread('RC.png', 0)
img1 = cv2.pyrDown(img0) # pyrDown 图像金字塔
img2 = cv2.pyrDown(img1)
img3 = cv2.pyrUp(img2)
img4 = img1 - img3
titles = ['img0(0)', 'img1(-1)', 'img2(-2)', 'img3(-1)', 'img4(-1)']
imgs = [img0, img1, img2, img3 ,img4]
for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
fig = plt.subplots_adjust(right = 1.3, top = 1.7)

