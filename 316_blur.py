8# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:40:28 2017

@author: Green
"""

import cv2
import matplotlib.pyplot as plt
img = cv2.imread('RC.png')
h, w = img.shape[:2]
cannyBlured = cv2.Canny(img, 50, 100)
py1 = cv2.pyrDown(img)
py2 = cv2.pyrUp(py1)
blured = cv2.blur(img,(5,5))
imgs = [img, cannyBlured, py1, py2, blured]


for i in range(len(imgs)):
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i])
    plt.subplots_adjust(right = 1, top = 1.6)
    
for i in range(len(imgs)):
    cv2.imshow('blur'+str(i), imgs[i])
cv2.waitKey()
cv2.destroyAllWindows()