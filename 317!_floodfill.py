# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:15:55 2017

@author: Green
"""

import numpy as np
import cv2
import random

help_message = ''' floodFill 漫水填充

From : 
http://blog.csdn.net/gjy095/article/details/9198845

Click image to set seed
Keys:
    f   ->    toggle floating range 
    c   ->    toggle 4/8 connectivity 
    ESC ->    exit 

'''

if __name__ == '__main__':
    import sys
    try: fn = sys.argv[1]
    except: fn = 'RC.jpg'
    print (help_message)
    
    img = cv2.imread(fn, True)
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    
    seed_pt = None
    fixed_range = True
    connectivity = 4
    
    def update(dummy = None):
        if seed_pt is None:
            cv2.imshow('Rachel', img)
            return
        flooded = img.copy()
        mask[:] = 0
        lo = cv2.getTrackbarPos('lo', 'floodFill')
        hi = cv2.getTrackbarPos('hi', 'floodFill')
        flags = connectivity
        if fixed_range:
            flags |= cv2.FLOODFILL_FIXED_RANGE # |= 按位与
        
        cv2.floodFill(flooded, mask, seed_pt, (
                random.randint(0, 255), random.randint(0, 255),
                random.randint(0,255)), (lo,)*3, (hi,)*3, flags)
        
        cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)
        cv2.imshow('floodFill', flooded)
        
    def onmouse(event, x, y, flags, parm):
        global seed_pt
        if flags & cv2.EVENT_FLAG_LBUTTON:
            seed_pt = x, y
            update()
            
    update()
    cv2.setMouseCallback('floodFill', onmouse)
    cv2.createTrackbar('lo', 'floodFill', 20, 255, update)
    cv2.createTrackbar('hi', 'floodFill', 20, 255, update)
    
    while True:
        ch = 0xFF & cv2.waitKey()
        if ch == 27:
            break
        if ch == ord('f'):
            fixed_range = not fixed_range
            print('using %s range'%('floating', 'fixed')[fixed_range])
            update()
        if ch == ord('c'):
            connectivity = 12 - connectivity
            print('connectivity = ', connectivity)
            update()
    cv2.destroyAllWindows()
        