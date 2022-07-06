# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:50:07 2017

@author: Green
"""
#查找轮廓
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,draw

#example1
#生成二值测试图像
img = np.zeros([200, 200])
img[20:40, 100:120] = 1#矩形
rr, cc = draw.circle(60, 60, 10)
rr1, cc1 = draw.circle(100, 100, 20)
img[rr, cc] = 1
img[rr1, cc1] = 1
#检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)
#绘制轮廓
fig, (ax0, ax1) = plt.subplots(1, 2, figsize = (8,8))
ax0.imshow(img, plt.cm.gray)
ax1.imshow(img, plt.cm.gray)
for n, contours in enumerate(contours):
    ax1.plot(contours[:, 1], contours[:, 0], linewidth = 2)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])
plt.show
#example2
from skimage import measure, data, color
img = color.rgb2gray(data.horse())
contours = measure.find_contours(img, 0.5)
fig, axes = plt.subplots(1, 2, figsize = (8, 8))
ax0, ax1 = axes.ravel()
ax0.imshow(img, plt.cm.gray)
ax0.set_title('original image')
rows, cols = img.shape
ax1.axis([0, rows, cols, 0])
for n, contours in enumerate(contours):
    ax1.plot(contours[:, 1], contours[:, 0], linewidth = 2)
ax1.axis('image')
ax1.set_title('contours')
plt.show()