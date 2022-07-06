# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:11:00 2017

@author: Green
"""

import cv2
videoCapture = cv2.VideoCapture('OutVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('OutVid2.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
sucess, frame = videoCapture.read()
while sucess:
    videoWriter.write(frame)
    achive, frame = videoCapture.read()








