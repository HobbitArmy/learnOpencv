# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:53:59 2017

@author: Green
"""

import cv2
import numpy as np

#回调函数,不做任何事情所以直接pass
def recall_nothing():
    pass

image = np.zeros((300, 500, 3), dtype = np.uint8)
cv2.namedWindow('image')

#creat trackbar
cv2.createTrackbar('R', 'image', 0, 255, recall_nothing)
cv2.createTrackbar('G', 'image', 0, 255, recall_nothing)
cv2.createTrackbar('B', 'image', 0, 255, recall_nothing)
#value:可选的指向整型变量的指针，整型变量的值对应于滑动条的位置
#count:滑动条最大的值。最小值总是为0
# onchange:指向回调函数的指针，每次滚动条改变位置时，这个函数就会被调用

#creat switch 0 -> close RGB(means black)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, recall_nothing)

while 1:
    cv2.imshow('image', image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        cv2.destroyAllWindows()
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    
    if s == 0:
        image[:] = 0
    else:
        image[:] = [b,g,r]
       