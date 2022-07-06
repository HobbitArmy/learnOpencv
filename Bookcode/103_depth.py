# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:59:05 2018

Foreground Detection

@author: Green
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
# 读取图像 并创建同形状的掩模 并以0填充//
img = cv2.imread('cap1.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
# 创建以0填充的前景和背景模型
bgdModel = np.zeros((1, 65), np.float64)
fgbModel = np.zeros((1, 65), np.float64)
# 选定目标矩形 来初始化GrabCut算法
rect = (180, 20, 380, 480) # (x1, y1, x2, y2) zeroPoint on mostLeftTop
cv2.grabCut(img, mask, rect, bgdModel, fgbModel, 12, 
            cv2.GC_INIT_WITH_RECT)
# 12 : 迭代次数
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]
# 将0 和 2 转化为 0 ，值为 1 和 3 的转化为 1；然后保存在mask2中，
# 这样就可以用mask2过滤 所有0值像素， 保留所有前景像素
plt.figure(figsize=[8, 8])
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('grabcut'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread('cap1.jpg'),\
                             cv2.COLOR_BGR2RGB))
plt.title('origin'), plt.xticks([]), plt.yticks([])
plt.show()