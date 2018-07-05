# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:01:37 2018

@author: gwu
"""


import numpy as np
import cv2
from Tkinter import Tk
from tkFileDialog import askopenfilename
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__' :
    #import image file
    #TODO resize image stuff
    Tk().withdraw()     #keeps blank tk window from popping up
    filename = askopenfilename()
    img = cv2.imread(filename)
    
    #Select ROI window
    #TODO loop to select multiple
    #fromCenter = False
    #cv2.selectROI("Cell Selection", img, fromCenter)
    cv2.selectRoi(img)
    
    top = int(r[1])
    bott = int(r[1]+r[3])
    left = int(r[0])
    right = int(r[0]+r[2])
    height = int(bott-top)
    width = int(right-left)
    centerX = int(r[1] + width/2)
    centerY = int(r[2] + height/2)
    
    imgCrop = img[top:bott,     #height
                  left:right]   #width
     
    
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
