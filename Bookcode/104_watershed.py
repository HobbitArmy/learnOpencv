# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:47:27 2018

@author: Green
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('cap1.jpg')
# 灰度图像二值化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 75, 255,
                            cv2.THRESH_BINARY)
# 通过 morphologyEx变换 来去除噪声 先膨胀后再腐蚀 可用来提取图像特征
# 对变换后的图像膨胀处理 可以得到大部分都是背景的区域
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel,
                           iterations = 2)
sure_bg = cv2.dilate(opening, kernel, iterations = 3)
# 反之 可通过 distanceTransform 来获取前景区域
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 用一个阈值来决定哪些区域是前景
ret, sure_fg = cv2.threshold(dist_transform, .9*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
# 前景与背景中有重合部分, 确定这些区域:可通过将sure_bg与sure_fg集合相减得到
unknown = cv2.subtract(sure_bg, sure_fg)
# 设置‘栅栏’来阻止水汇聚
ret, markers = cv2.connectedComponents(sure_fg)
# 将unknow区域设置为0
markers = markers + 1
markers[unknown == 255] = 0
# 打开门把水漫起来并把栏杆绘制成红色
markers = cv2.watershed(img, markers)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img[markers == -1] = [255, 0, 0]
plt.imshow(img)
plt.show()
