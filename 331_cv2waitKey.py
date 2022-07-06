# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:17:46 2018

cv2.waitKey([delay])
delay -> Delay in milliseconds. 0 means 'forever'

@author: Green
"""

import cv2

def test():
    sr2 = cv2.imread('SR2.jpg')
    cv2.imshow('img', sr2)
    cv2.waitKey(0)
    print('\nDone')
    cv2.destroyAllWindows()
def test2():
    sr = cv2.imread('SR.jpg')
    cv2.imshow('img', sr)
    keycode = cv2.waitKey(4000)
    cv2.destroyAllWindows()
    print('\n%i'%keycode)
    print('Done2')
def test3():
    fly = cv2.imread('fly.jpg')
    while(True):
        cv2.imshow('img', fly)
        if cv2.waitKey(1) & 0xff == 27:
            print('\nDone3')
            cv2.destroyAllWindows()
            break
        
if __name__ == '__main__':
    test()
    test2()
    test3()