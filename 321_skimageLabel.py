# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 01:43:06 2017

@author: Green
"""
from skimage.measure import label,regionprops
import numpy as np

x = np.eye(4).astype(int)
print('x:');print(x)
print(label(x, connectivity = 1))
print(label(x, connectivity = 2))
print(label(x, background = -1))
# Consider all pixels with this value as background pixels,
# and label them as 0. 
print('\n')
b = np.array([[1,0,1,0],
              [1,1,1,1],
              [0,0,0,1],
              [1,0,2,1]])
c = np.array([[1,0,0,0],
              [0,1,1,0],
              [0,0,0,0],
              [0,0,0,1]])
print('b:');print(b)
print(label(b, connectivity = 1))
print('\n')
print('c:');print(c)
print(label(c, connectivity = 2))
groups = regionprops(c)
groups[0].centroid