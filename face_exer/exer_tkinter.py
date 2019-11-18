# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:56:33 2019

@author: Administrator
"""

from tkinter import *


def Enroll():
    print("11")
    
    
def Authenticate():
    print("22")

    
def main():

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

    print('Completed.')

if __name__ == '__main__':
    main()