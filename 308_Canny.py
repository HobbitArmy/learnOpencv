# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:37:01 2017

@author: Green
"""

import cv2

img = cv2.imread('Bookcode/cameo.png', 0) # second parameter = 0 -> Return a grayscale image.
cv2.imwrite('canny.jpg', cv2.Canny(img, 90, 100))
cv2.imshow('canny.jpg', cv2.imread('canny.jpg'))
cv2.waitKey()
cv2.destroyAllWindows()


