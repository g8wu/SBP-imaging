# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:52:09 2018

@author: gwu
"""

#TODO WHY IS IT SAYING 'BUTTON' NOT DEFINED??
from Tkinter import Tk, Button, BOTTOM, RIGHT, IntVar, Checkbutton
import cv2
from tkFileDialog import askopenfilename


class TKtest:
    def __init__(self, master):
        self.master = master
        master.title("TK TEST")
        # Browse button
        browse = Button(master, text = "Browse", command = self.getFile)
        browse.pack(side=BOTTOM)
        browse.pack(side=RIGHT)
        
        #Check buttons
        self.v1 = IntVar()
        check = Checkbutton(self, text = "Undifferentiated", variable = self.v1, command = self.enterDscrp)
        
        #Packing
        check.grid(row = 1, column = 1)
        
        
        window.mainloop()
    
    def enterDscrp():
        print ("clicked checkbox")
        
    def getFile():
        Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
        return img

if __name__ == "__main__":
    root = Tk()
    app = TKtest(root)
    root.mainloop()
    #TKtest()