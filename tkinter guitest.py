# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:52:25 2018

@author: gwu
"""
from Tkinter import Tk
import cv2
from tkFileDialog import askopenfilename


class TKtest():
    def __init__(self, master = None):
        window = Tk()
        browse = Button(window, text = "Browse", command = getFile)
        browse.pack(side=BOTTOM)
        browse.pack(side=RIGHT)
        
        window.mainloop()
        
    def getFile():
        Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
        return img

if __name__ == "__main__":
    TKtest()
