# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:48:52 2019

@author: setgo
"""

from train4 import Train
from test4 import Test
from storeData4 import storeData
    
def main_register():
    cjTrain=Train()
    cjstoreData = storeData()

    personList=[]
    #####person 그룹 생성
   # personGroupId=cjstoreData.createPersongroup()
    
    ####DB에 person 이름, ID 생성
    name,personID,personGroupId=cjstoreData.newPerson()
    
    ####person 이미지 저장
    personList,personImageList= cjstoreData.savePersonImage(personID,personList,name)
    
    ####person 이미지,NAME을 API에 보냄
    cjstoreData.createPerson(personGroupId,personID,personImageList,name)
    
    ####person그룹 트레인
    cjTrain.trainModel(personGroupId)


if __name__ == '__main__':
    main_register()