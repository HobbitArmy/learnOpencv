# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 01:02:18 2017

@author: Green
"""

'''思路:
边缘检测 -> 轮廓提取 -> 标记连通区域个数 ->
求中心坐标 -> 求区域面积 -> 转化面积为几何单位标定 
'''

import matplotlib.pyplot as plt
from skimage import io, color, morphology, feature, measure


# img = color.rgb2gray(data.horse)
img = io.imread('cap.jpg')
img = color.rgb2gray(img)
img = (img>0.29)*1

chull = morphology.convex_hull_object(img, neighbors = 8)
# convex_hull_image()将图片中的所有目标看作一个整体,只计算出一个凸多边形.
# 若有多个目标物体,需要计算多个凸多边形,可使用convex_hull_object（）.
# image是一个二值图像，neighbors表示是采用4连通还是8连通
fig, axes = plt.subplots(1, 2, figsize = (8,8))
ax0, ax1 = axes.ravel()
ax0.imshow(img, plt.cm.gray)
ax0.set_title('origin')
ax1.imshow(chull, plt.cm.gray)
ax1.set_title('convex')
# ******************************************* #
img = io.imread('cap2.jpg')
img = color.rgb2gray(img)
edges = feature.canny(img, sigma = 3)
# 检测canny边缘,得到二值图片
chull = morphology.convex_hull_object(edges)
fig, axes = plt.subplots(1, 2, figsize = (8,8))
ax0, ax1 =axes.ravel()
ax0.imshow(edges, plt.cm.gray)
ax0.set_title('origin')
ax1.imshow(chull, plt.cm.gray)
ax1.set_title('convex')
plt.show()
# ********************************************* #
import numpy as np
import scipy.ndimage as ndi
def microstructure(l = 256):# 编写一个函数来生成原始二值图像
    n = 5
    x, y = np.ogrid[0:1, 0:1]# 生成网络
    mask = np.zeros((l, l))
    generator = np.random.RandomState()# 随机数种子
    points = l*generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma = l/(4.*n))
    return mask > mask.mean()
data = microstructure(l = 128)# 生成测试图片,
# 乘以1可将bool数组快速地转换为int数组
labels = measure.label(data, connectivity = 1)
# connective=1 -> 8连通区域标记
dst = color.label2rgb(labels+1)# 根据不同的标记显示不同的颜色
dst2 = morphology.remove_small_objects(data, min_size = 300, 
            connectivity = 1)# 删除小块区域
print('regions number:', labels.max()+1)
prop = measure.regionprops(labels)
for i in range(labels.max()+1):
    print(str(i+1)+':'+str(prop[i-1].area),end = '; ')# prop from [-1]
fig, (ay1, ay2, ay3) = plt.subplots(3, 1, figsize = (24, 8))
ay1.imshow(data, plt.cm.gray, interpolation = 'nearest')
ay1.axis('off')
ay2.imshow(dst, interpolation = 'nearest')
ay2.axis('off')
ay3.imshow(dst2, interpolation = 'nearest')
ay3.axis('off')
fig.tight_layout()
plt.show()
