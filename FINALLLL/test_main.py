# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:15:58 2019

@author: setgo
"""

from train4 import Train
from test4 import Test
from storeData4 import storeData

def main_test():
    cjTest=Test()
    ####테스트 이미지 카메라로 받아서 저장
    cjTest.camera()
    
    ####테스트 이미지 얼굴인식
    img_bgr, faceId, left, top, bottom, right = cjTest.faceDetect()
    
    ###테스트 이미지  데이터베이스에 있는지 확인 후 출력
    cjTest.faceidentify(img_bgr,faceId,left,top,bottom,right)
    print('Completed.')

if __name__ == '__main__':
    main_test()