# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:41:25 2019

@author: Administrator
"""

from train2 import Train
from test2 import Test
from storedata2 import storeData

#class Main:
#    def faceTrain(self):
#        a=Train()
#        personGroupId=a.createPersongroup()
#        a.createPerson(personGroupId)
#        a.trainModel(personGroupId)
#        return(personGroupId)
    
#    def faceTest(personGroupId):
#        b=Test()
#        img_bgr, faceId, left, top, bottom, right = b.faceDetect()
#        b.faceIdentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    
def main():
    cjTrain=Train()
    cjstoreData = storeData()
    cjTest=Test()
    
    personGroupId=cjstoreData.createPersongroup()
    cjstoreData.createPerson(personGroupId)
    cjTrain.trainModel(personGroupId)
    img_bgr, faceId, left, top, bottom, right = cjTest.faceDetect()
    cjTest.faceidentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    print('Completed.')

if __name__ == '__main__':
    main()