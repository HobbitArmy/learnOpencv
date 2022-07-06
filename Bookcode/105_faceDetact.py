# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:56:18 2018

@author: Green
"""

import cv2

filename = 'SRs.jpg'

def detect(filename):
    # 声明变量,变量为CascadeClassifier对象,他负责检测
    face_cascade = cv2.CascadeClassifier(
            './cascades/haarcascade_frontalface_default.xml')
    # 加载文件,并转化为灰度图像,因为检测需要
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # face_cascade.detectMultiScale 进行实际的人脸检测
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2,
            minNeighbors = 3) # scaleFactor:检测过程中每次迭代图像的压缩率
    #minNeighbors:每个矩形保留近邻数目的最小值
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('SRs', img)
        
detect(filename)
cv2.waitKey()
cv2.destroyAllWindows()