# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:28:32 2017

@author: Green
"""

import math
import skimage.transform as tf
import matplotlib.pyplot as plt
from skimage import data

text = data.text()

tform = tf.SimilarityTransform(scale = 1, rotation = math.pi/4, translation = 
                               (text.shape[0]/2, -100))

rotated = tf.warp(text, tform)
back_rotated = tf.warp(rotated, tform.inverse)

fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, figsize = (14, 6))
plt.gray()

ax1.imshow(text)
ax1.axis('off')
ax2.imshow(rotated)
ax2.axis('off')
ax3.imshow(back_rotated)
ax3.axis('off')
