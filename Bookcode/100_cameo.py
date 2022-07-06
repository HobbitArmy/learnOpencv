# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:17:33 2017

@author: Green
"""

import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),
                                              self._windowManager, True)
        self._curveFilter = filters.SharpenFilter()
        
    def run(self):
        """ Run The Main Loop."""
        self._windowManager.createdWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)
            # Filter the Frame
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
            
    def onKeypress(self, keycode):
        """ space -> Take a screenshot. \\ tab -> Start/stop a screencast. 
                                        \\ esc -> Quit."""
        if keycode == 32:# space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:# tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:# esc
            self._windowManager.destroyWindow()
            cv2.VideoCapture.release(0)

if __name__ == "__main__":
    Cameo().run()
        
        
    
        
        
        
        
        
        