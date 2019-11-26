# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:55:54 2019

@author: setgo
"""

from train4 import Train
from test4 import Test
from storeData4 import storeData
import pymongo
    
def createGroup():
    cjstoreData = storeData()

    #####person 그룹 생성
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["employee"]
    mycol=mydb["group"]
    groupname = str(input("그룹이름을 입력하세요 : "))
        
    groupDict={"name":groupname}
    mycol.insert_one(groupDict)
        
    cjstoreData.createPersongroup(groupname)
        
    
    
if __name__ == '__main__':
    createGroup()