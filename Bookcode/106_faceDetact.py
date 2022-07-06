# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:36:56 2018

@author: Green
"""

import cv2

def detect():
    # 加载 Haar级联文件
    face_cascade = cv2.CascadeClassifier(
            './cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(
            './cascades/haarcascade_eye.xml')
    # 打开 videoCaptire目标,初始化摄像头
    camera = cv2.VideoCapture(0)
    # 0表示第一个
    while True:
        # 捕获帧, read()返回两个参数第一个为布尔值,表明是否成功读取;
        # 第二个为帧本身.
        ret, frame = camera.read()
        cv2.imshow('camera', frame)
        # 转化为灰度图像是必要的,因为 opencv中人脸检测需要灰度的色彩空间
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 对灰度的帧调用 detectMultiScale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # 创建目标矩形框,并在内检测眼睛
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h),
                                (100,200,100), 2)
            roi_gray = gray[y:y+h, x:x+w]
            # 1.03:图像迭代压缩率; (40,40)限制眼睛搜索最小尺寸为60x60像素
            eyes = eye_cascade.detectMultiScale(
                            roi_gray, 1.03, 5, 0, (60,60))
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(frame[y:y+h, x:x+w],
                              (ex, ey), (ex+ew,ey+eh),
                                  (0,100,200), 2)
            cv2.imshow('camera', frame)
            
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()
    
if  __name__ == '__main__':
    detect()
    