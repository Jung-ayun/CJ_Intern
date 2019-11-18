# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:41:14 2019

@author: Administrator
"""

import cv2
import requests

cap =cv2.VideoCapture(0)
frame_count = 0

while(True):
    ret, frame = cap.read()
    
    frame_count+=1
    cv2.imshow('unknown',frame)
    if cv2.waitKey(20)&0xFF == ord('q'):
        break
cap.release()
cv2.destroyALLWindows()