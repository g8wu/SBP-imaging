# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:52:25 2018

@author: gwu
"""
from Tkinter import *
import cv2
from tkFileDialog import askopenfilename


class TKtest():
    
    def __init__(self):
        window = Tk()
        window.title("Cell Selection")
        
        # Frame1: ROI Select, Browse Button
        frame1 = Frame(window)
        frame1.pack(side = LEFT)
        self.v1 = IntVar()
        self.canvas = Canvas(window, width = 200, height = 100, variable = self.v1, bg = "white")
        
        self.v2 = IntVar()
        browse = Button(window, variale = self.v2, text = "Browse", command = self.getFile)
        browse.pack(side=BOTTOM)
        browse.pack(side=RIGHT)
        
        
        window.mainloop()
        
    def getFile(self):
        Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
    
    
    
if __name__ == "__main__":
    TKtest()
