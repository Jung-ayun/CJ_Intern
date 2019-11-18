# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:35:09 2019

@author: Administrator
"""

import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QApplication,QWidget,QLabel,QPushButton,QHBoxLayout,QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def btn1ClickListener():
        print("111")
    def btn2ClickListener():
        print("2222")
    
    def makeUI(self):
        myLabel1=QLabel("CJ 직원인식 시스템")
        btn1 = QPushButton("새로운 직원 등록")
        btn1.clicked.connect(btn1ClickListener)
        btn2 = QPushButton("직원 인증")
        btn2.clicked.connect(btn2ClickListener)
        
        hBoxLayout= QHBoxLayout()
        hBoxLayout.addWidget(btn1)
        hBoxLayout.addWidget(btn2)
        
        vBoxLayout = QVBoxLayout()
        vBoxLayout.addWidget(myLabel1)
        vBoxLayout.addLayout(hBoxLayout)
        vBoxLayout.addStretch()
        
        win=QWidget()
        win.setLayout(vBoxLayout)
        self.setCentralWidget(win)
        
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("mywindow")
        self.show()
app=QApplication(sys.argv)
myWin=MyWindow()
myWin.makeUI()
sys.exit(app.exec())        


    