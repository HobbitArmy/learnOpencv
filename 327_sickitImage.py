# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:39:15 2017

from:
http://blog.csdn.net/u011532367/article/details/51012975

@author: Green
"""
import skimage
from skimage import io, data, filters, exposure, morphology
import scipy
import os
import numpy as np

filename = os.path.join(skimage.data_dir, 'camera.png')
camera = io.imread(filename)

camera = data.camera()
camera.dtype # 检验数据类型
camera_sobel = filters.sobel(camera) # Sobel算法像素边缘检测
camera_sobel.max()

# 另一个提取轮廓
cat = data.chelsea()[:,:,1]
hsobel_cat = filters.sobel(cat)
# 增强对比度
cat_equalized = exposure.equalize_hist(cat)
io.imshow(cat)
io.imshow(hsobel_cat)
io.imshow(cat_equalized)
# otsu阀值法 图像分割
thresh = filters.threshold_otsu(cat)
dst = (cat <= thresh)*1.0
io.imshow(dst)
# 对图像连通的部分加标签
n = 16
l = 256
im = np.zeros((l, l))
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = scipy.ndimage.filters.gaussian_filter(im, sigma = l/(4.*n))
blobs = im > im.mean()
all_labels = morphology.label(blobs)# 对连通的部分加标签
blobs_labels = morphology.label(blobs, background = 0)
    # 去掉背景的部分，不为背景加标签
io.imshow(blobs)
io.imshow(all_labels)
io.imshow(blobs_labels)
# Harris角点检测检测角点
from skimage.feature import corner_harris, \
 corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform
import matplotlib.pyplot as plt
tform = AffineTransform(scale = (1.3, 1.1), rotation = 1, \
 shear = 0.7, translation = (210, 50))
image = warp(data.checkerboard(), tform.inverse, \
             output_shape = (350, 350))

coords = corner_peaks(corner_harris(image), min_distance = 5)
coords_subpix = corner_subpix(image, coords, window_size = 13)
plt.gray() # 灰度图
plt.figure(figsize = (8,8))
plt.imshow(image, interpolation = 'nearest')
plt.plot(coords_subpix[:, 1], coords_subpix[:, 0], 'xr', \
         markersize = 10, mew = 5)
plt.plot(coords[:, 1], coords[:, 0], '.g', markersize = 7)
plt.axis('off')
plt.show()
