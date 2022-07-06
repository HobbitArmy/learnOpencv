# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:08:36 2018

@author: Green
"""

import cv2
from matplotlib import pyplot as plt

image = cv2.imread('capp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
plt.figure(figsize = [4, 12])
plt.subplot(311), plt.imshow(image, 'gray')
plt.title('origin'), plt.xticks([]), plt.yticks([])
plt.subplot(312), plt.hist(image.ravel(), 256)
plt.title('histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(313), plt.imshow(th1, 'gray')
plt.title('ostu thres='+str(ret1)), plt.xticks([]), plt.yticks([])
plt.show