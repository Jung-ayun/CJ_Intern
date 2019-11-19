# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:48:52 2019

@author: setgo
"""

from train4 import Train
from test4 import Test
from storeData4 import storeData

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
 #   famousList= cjstoreData.savePersonImage(name,famousList)
    cjstoreData.createPerson(personGroupId)
    cjTrain.trainModel(personGroupId)
    cjTest.camera()
    img_bgr, faceId, left, top, bottom, right = cjTest.faceDetect()
    cjTest.faceidentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    print('Completed.')

if __name__ == '__main__':
    main()