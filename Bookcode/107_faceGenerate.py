# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:17:32 2018

@author: Green
"""

import cv2

def generate():
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x-20,y-20), (x+w,y+h), (255,0,0), 2)
            f = cv2.resize(gray[y-20:y+h, x-20:x+w], (200,200))
            cv2.imwrite('jpg/%s.jpg' % str(count), f)
            count += 1
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xff == 27:
            break
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    generate()