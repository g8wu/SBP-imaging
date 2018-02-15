# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:03:18 2018

@author: gwu
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class qtpyApp(QWidget):
    
    def __init__(self):
        super().__init__()  #for Python 3. issue with Python 2.7 :/
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.title = 'Cell Selection'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.ttitle)
        self.setGeometry(self.left, self.top, self.width, self.height )
        
        browse = QPushButton('Browse', self)
        browse.move(100, 70)
        browse.clicked.connect(self.getFiles)
        
        self.show()
    
    def getFiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File',QtCore.QDir.rootPath(), '.jpg')
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = qtpyApp()
    sys.exit(app.exec_())