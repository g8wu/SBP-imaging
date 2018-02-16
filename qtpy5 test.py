# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:27:18 2018

@author: gwu
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class CellImaging(QWidget):
    
    #constructor method for Python
    def __init__(self):
        self.initUI()
        
    def initUI():
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Cell Selection")
        self.setWindowIcon('logo.jpg')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())