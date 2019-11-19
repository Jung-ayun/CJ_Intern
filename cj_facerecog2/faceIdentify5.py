# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:38:14 2019

@author: setgo
"""


from train5 import Train
from test5 import Test
from storeData5 import storeData
from tkinter import *

class faceIdentify:
      
cjTrain=Train()
cjstoreData = storeData()
cjTest=Test()

def __init__(self):
    window=Tk()

def Store(self):
    personGroupId=cjstoreData.createPersongroup()
    self.name = 
    cjstoreData.savePersonImage(name,famousList)
    cjstoreData.createPerson(personGroupId)
    cjTrain.trainModel(personGroupId)
    
def Authenticate():
    print("22")
    img_bgr, faceId, left, top, bottom, right = cjTest.faceDetect()
    personGroupId = cjstoreData.createPersongroup()
    cjTest.faceidentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    
    
def main():
    #cjTrain=Train()
    #cjstoreData = storeData()
    #cjTest=Test()
    #window=Tk()
    window.geometry('400x430')
    window.title("CJ직원인증시스템")
    cj = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\cj_biosemester\\cj.png')
    label=Label(window,image=cj,width="400",height="400")
    label.pack()
    
    btn1 = Button(window,text="새로운 직원 등록",width=27,command=Store)
    btn2 = Button(window,text="직원 인증",width=27,command=Authenticate)
    
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    window.mainloop()
    
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