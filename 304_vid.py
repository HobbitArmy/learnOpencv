# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:52:49 2017

@author: Green
"""

import cv2
cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('OutVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

sucess, frame = cameraCapture.read()
FramesRemaining = 5 * fps -1
while sucess and FramesRemaining > 0:
    videoWriter.write(frame)
    condition, frame = cameraCapture.read()
    FramesRemaining -= 1
cameraCapture.release()
