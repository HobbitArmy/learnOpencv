# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:00:36 2017

@author: Green
"""

import cv2  
from matplotlib import pyplot as plt  
img = cv2.imread('408.bmp',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)  
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)  
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)  
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)  
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)  
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']  
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]  
for i in range(6):  
    plt.subplot(6,1,i+1),plt.imshow(images[int(i)],'gray')  
    plt.title(titles[i])  
    plt.xticks([]),plt.yticks([])  
plt.subplots_adjust(right = 12, top = 10)
plt.show()
plt.imshow(thresh2,'gray')
plt.subplots_adjust(right = 4,top=2)
