# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:59:29 2017

@author: Green
"""

import cv2
import numpy as np
import time

class CaptureManager(object):
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview
        
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        
        self._startTime = None
        self._framesElapsed = int(0)
        self._fpsEstimate = None

    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None
    
    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve() # i dont know _,
        return self._frame
    
    @property
    def isWritingImage(self):
        return self._imageFilename is not None
    
    @property
    def isWritingVideo(self):
        return self._videoFilename is not None

    def enterFrame(self):
        """Capture The Next Frame, If Any."""
        # First, check that any previous frame was exited.
        assert not self._enteredFrame, \
        'previous enterFrame() had no matching exitFrame()'
        
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()
            
    def exitFrame(self):
        """Draw To The Window. Write To Flies. Release The Frame."""
        # Check whether any grabbed frame is retrievable. The getter may retrive and cache the frame.
        if self.frame is None:
            self._enteredFrame = False
            return
        
        # Update the FPS estimate and related variables.
        if self._framesElapsed == 0:
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed
        self._framesElapsed += 1
        
        # Draw to the Window, if any.
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroredFrame = np.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)
        
        # Write to the image file, if any.
        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)
            self._imageFilename = None
        
        # Write to the video file, if any.
        self._writeVideoFrame()
            
        # Release the frame.
        self._frame = None
        self._enteredFrame = False
    
    ## enterFrame() 只能同步获取一帧，且会推迟从一个通道的获取，以便从变量 frame 中读取
    ## exitFrame() 可以从当前通道中获取图像,估计帧速率,通过窗口管理器显示图像,执行暂停的请求,从而向文件中写入图像
    def writeImage(self, filename):
        self._imageFilename = filename
        
    def startWritingVideo(self, filename, encoding = cv2.VideoWriter_fourcc('I','4','2','0')):
        self._videoFilename = filename
        self._videoEncoding = encoding
        
    def stopWritingVideo(self):
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        
    def _writeVideoFrame(self):
        if not self.isWritingVideo:
            return
        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                if self._framesElapsed < 20:
                    return
                else:
                    fps = self._fpsEstimate
                size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                            int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                self._videoWriter = cv2.VideoWriter(self._videoFilename,self._videoEncoding,fps,size)
            self._videoWriter.write(self._frame)

# 提供键盘事件处理
class WindowManager(object):
    def __init__(self, windowName, keypressCallback = None):
        self.keypressCallback = keypressCallback
        
        self._windowName = windowName
        self._isWindowCreated = False
        
    @property
    def isWindowCreated(self):
        return self._isWindowCreated
    def createdWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True
    def show(self, frame):
        cv2.imshow(self._windowName, frame)
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # Discard any non-ASCII info encoded by GTK.
            keycode &= 0xFF
            self.keypressCallback(keycode)





        
