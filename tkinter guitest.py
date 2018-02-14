# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:52:25 2018

@author: gwu
"""
from Tkinter import *
import numpy as np
import cv2
from Tkinter import Tk
from tkFileDialog import askopenfilename
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class cellSelect(Frame):

    
    def testPrint(self):
        print "Hello, World"
        Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
        #TODO show img in window
        
    def createWidgets(self):
        self.browse = Button(self)
        self.browse["text"] = "Browse",
        self.browse["command"] = self.testPrint

        self.browse.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = cellSelect(master=root)
app.mainloop()
root.destroy()
        