# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:11:26 2017

@author: Green
"""

import cv2
import numpy as np

img = cv2.imread('cap3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 50, 200)

minLineLength = 20
maxLineGap = 20
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, minLineLength, maxLineGap)
for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        cv2.line(img, (x1,y1), (x2, y2), (0, 255, 0), 2)
    
cv2.imshow('edges', edges)
cv2.imshow('lines', img)

cv2.waitKey()
cv2.destroyAllWindows()
    