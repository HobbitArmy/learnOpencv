# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:25:22 2017

@author: Green
"""

import cv2

clicked = False
def Mouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked =True
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('305')
cv2.setMouseCallback('305', Mouse)

print('Showing Camera Feed. Click Window or Press Any Key to Stop.')
sucess, frame = cameraCapture.read()
while sucess and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('305', frame)
    sucess, frame = cameraCapture.read()

cameraCapture.release()
cv2.destroyAllWindows
