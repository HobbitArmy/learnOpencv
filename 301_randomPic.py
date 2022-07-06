# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:20:21 2017

@author: Green
"""

import cv2
import numpy as np
import os

randmByteArray = bytearray(os.urandom(240000))
flatNumpyArray = np.array(randmByteArray)

grayImage = flatNumpyArray.reshape(400, 600)
bgrImage = flatNumpyArray.reshape(400, 200, 3)
cv2.imwrite('RandomGray.png', grayImage)
cv2.imwrite('RandmColor.png', bgrImage)
cv2.imshow('3011', grayImage)
cv2.imshow('3012', bgrImage)
cv2.waitKey()
cv2.destroyAllWindows()
