 # -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 01:09:46 2017

@author: Green
"""

from skimage import data, util
from skimage.measure import label, regionprops

img = util.img_as_ubyte(data.coins()) > 110
label_img, num = label(img, return_num = True, connectivity = img.ndim)
# ndim -> diamension
props = regionprops(label_img)

props[0].centroid
props[0]['centroid']

print(props[0].centroid)
"""
属性名称	             类型	                   描述
area	                 int	              区域内像素点总数
bbox	                tuple    边界外接框(min_row,min_col,max_row,max_col)
centroid	             array　　           	质心坐标
convex_area	           int	             凸包内像素点总数
convex_image	          ndarray	        和边界外接框同大小的凸包　　
coords	                 ndarray	         区域内像素点坐标
Eccentricity            float	              离心率
equivalent_diameter 	   float	         和区域面积相同的圆的直径
euler_number	           int　　           	区域欧拉数
extent 	             float	           区域面积和边界外接框面积的比率
filled_area	           int    	   区域和外接框之间填充的像素点总数
perimeter           	  float	              区域周长
label	                int	                  区域标记
"""