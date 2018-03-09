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
        
        frame1 = Frame(window)
        label1 = Label(frame1, text = "Click center of cell and drag to select.\n Press ENTER to begin selecting descriptors.")
        label1.pack(side = TOP)
        
        canvas = Canvas(window, width = 200, height = 100, bg = "white")
        canvas.pack(fill=Y)
        
        browse = Button(window, text = "Browse", command = self.getFile)
        browse.pack(side=LEFT)
        """
        label1 = Label(window, text = "Click center of cell and drag to select.\n Press ENTER to begin selecting descriptors.")
        label1.pack(side = TOP)
        
        canvas = Canvas(window, width = 200, height = 100, bg = "white")
        canvas.pack(fill=Y)
        
        browse = Button(window, text = "Browse", command = self.getFile)
        browse.pack(side=LEFT)
        """        
        window.mainloop()
       
    def getFile(self):
        Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
        
    def ROI(self):
        Tk().withdraw()
        filename = askopenfilename()
        img = cv2.imread(filename)
        cv2.selectROI(img)

        imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        #Display cropped image window
        #gui display roi img with coords,l&w
        cv2.imshow("Enter descriptors", imgCrop)
        print 'Center (x,y): (', centerX, ', ', centerY, ')\n'
        print 'Height x Width: ', height, 'x', width, '\n'
        print 'Enter descriptors:'
        print ' 1: Undifferentiated \n 2: Differentiated \n 3: Damaged'
        print '>>'
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
 

TKtest()
