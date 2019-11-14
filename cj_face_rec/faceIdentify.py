# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:10:44 2019

@author: setgo
"""
from train import Train
from test import Test

class FaceIdentify:
    def faceTrain(self):
        a=Train()
        personGroupId=a.createPersongroup()
        a.createPerson(personGroupId)
        a.trainModel(personGroupId)
        return(personGroupId)
    
    def faceTest(personGroupId):
        b=Test()
        img_bgr, faceId, left, top, bottom, right = b.faceDetect()
        b.faceIdentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    
def main():
    a=Train()
    personGroupId=a.createPersongroup()
    a.createPerson(personGroupId)
    a.trainModel(personGroupId)
    b=Test()
    img_bgr, faceId, left, top, bottom, right = b.faceDetect()
    b.faceidentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    print('Completed.')

if __name__ == '__main__':
    main()
