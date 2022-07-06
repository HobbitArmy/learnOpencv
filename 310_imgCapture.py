# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:31:41 2017

@author: Green
"""

import cv2
import time


def cv2_show_capture():
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 25920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 19440)
        cap.set(cv2.CAP_PROP_FPS, 60)
        while True:
            ret, frame = cap.read()
            # print('fps:%.2f' % cap.get(5))
            cv2.namedWindow('capture', cv2.WINDOW_NORMAL)
            cv2.imshow('capture', frame)
            if cv2.waitKey(1) == ord('q'):
                local_time = time.strftime('./capture/%Y%m%d_%H%M%S', time.localtime())
                cv2.imwrite('./%s.jpg' % local_time, frame)
                break
        # cap.release()
        cv2.destroyAllWindows()
    finally:
        print('CAP read finished')

if __name__ == '__main__':
    cv2_show_capture()
'''
img = cv2.imread('cap2.jpg')
cv2.imshow('cap2', img)
cv2.waitKey()
cv2.destroyAllWindows()'''
