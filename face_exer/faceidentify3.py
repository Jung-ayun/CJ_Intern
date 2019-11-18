# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 00:06:03 2019

@author: Administrator
"""


from train3 import Train
from test3 import Test
from storedata3 import enrollData
from tkinter import *


cjTrain=Train()
cjenrollData = enrollData()
cjTest=Test()

def Enroll():
    print("11")
    personGroupId=cjenrollData.createPersongroup()
    cjenrollData.savePersonImage(name,famousList)
    cjenrollData.createPerson(personGroupId)
    cjTrain.trainModel(personGroupId)
    
def Authenticate():
    print("22")
    img_bgr, faceId, left, top, bottom, right = cjTest.faceDetect()
    personGroupId = cjenrollData.createPersongroup()
    cjTest.faceidentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    
def main():
#    cjTrain=Train()
#    cjstoreData = storeData()
   # cjTest=Test()
    
    window=Tk()
    window.geometry('400x430')
    window.title("CJ직원인증시스템")
    cj = PhotoImage(file='C:\\Users\\Administrator\\Desktop\\cj_biosemester\\cj.png')
    label=Label(window,image=cj,width="400",height="400")
    label.pack()
    
    btn1 = Button(window,text="새로운 직원 등록",width=27,command=Enroll)
    btn2 = Button(window,text="직원 인증",width=27,command=Authenticate)
    
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    window.mainloop()
#    personGroupId=cjstoreData.createPersongroup()
#   cjstoreData.createPerson(personGroupId)
 #   cjTrain.trainModel(personGroupId)
 #   img_bgr, faceId, left, top, bottom, right = cjTest.faceDetect()
  #  cjTest.faceidentify(personGroupId ,img_bgr,faceId,left,top,bottom,right)
    print('Completed.')

if __name__ == '__main__':
    main()