# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:52:25 2018

@author: gwu
"""
import Tkinter as tk
from tkFileDialog import askopenfilename
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2

class cellSelect(Frame):
    
    def getFile(self):
        tk.Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
        
        #TODO show img in window
        fromCenter = False
        r = cv2.selectROI("Cell Selection", img, fromCenter)
        top = int(r[1])
        bott = int(r[1]+r[3])
        left = int(r[0])
        right = int(r[0]+r[2])
        height = int(bott-top)
        width = int(right-left)
        centerX = int(r[1] + width/2)
        centerY = int(r[2] + height/2)
        
        imgCrop = img[top:bott, left:right]   #width
        
        #Display cropped image window
        #gui display roi img with coords,l&w
        cv2.imshow("Enter descriptors", imgCrop)
        print 'Cell center coord: ', centerX, ', ', centerY, '\n', 'Height x Width: ', height, 'x', width
                
        
    def createWidgets(self):
        browse = tk.Button(self)
        browse.pack(side= tk.LEFT)
        browse.pack(side = tk.BOTTOM)
        browse["text"] = "Browse",
        browse["command"] = self.getFile
        
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        

root = tk.Tk()
app = cellSelect(master=root)
app.mainloop()
root.destroy()