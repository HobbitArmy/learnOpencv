# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:41:58 2017

@author: Green
"""

import cv2
import numpy as np
img = cv2.pyrDown(cv2.imread('cap.jpg', cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 190, 255, cv2.THRESH_BINARY)

image, contours, heir = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c) # 计算出边界框
    cv2.rectangle(img, (x,y), (x+w, y+w), (0, 255, 0), 2)
    
    # min area rectangle
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)
    # min area circle
    (x,y) ,radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow('contours', img)
cv2.waitKey()
cv2.destroyAllWindows()