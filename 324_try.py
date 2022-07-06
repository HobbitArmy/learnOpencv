# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:17:44 2017

@author: Green
"""

import cv2
from cv2 import contourArea
img = cv2.imread('cap2.jpg', 0)
img = cv2.GaussianBlur(img, (11,11), 0)
ret, thresh = cv2.threshold(img.copy(), 71, 255, 1)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, 
                cv2.CHAIN_APPROX_SIMPLE)
hierarchy = hierarchy[0]
Max = len(contours)
for i in range(Max):
    if hierarchy[i,3] != -1:
        del contours[i]
        # hierarchy = np.delete(hierarchy, i, 0)
        
i = 0
for c in contours:
    M = cv2.moments(c)
    #compute center
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    #area
    area = str(int(contourArea(contours[i])/5)+1)
    #draw
    cv2.drawContours(img, [c], -1, (0,255,0),2)
    cv2.circle(img, (cx,cy), 2, (255,255,255), -1)
    cv2.putText(img, str('S'+str(i)+'='+area+'r'), (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255,255,255), 1)
    i += 1

print('%d items found'%(i))
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
#img = cv2.drawContours(img, contours, -1, (0,255,0), 2)
    

