# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:01:37 2018

@author: gwu


1. Import image
2. display desired image
3. ROI - region of interest
        a. click to select roi
        b. Remember edgepoints or center point
5. Save ROI with:
        a. cell number
        b. coordinates
        c. descriptions:
            i. TODO
6. Save ROI image
    filename format: cell#_xcoord_ycoord_descrip1_descrip2....tiff

EBI.jpg 
"""


import numpy as np
import cv2
from Tkinter import Tk
from tkFileDialog import askopenfilename
from PyQt5 import QtCore, QtGui, QtWidgets

#import image file
#TODO resize image stuff
Tk().withdraw()     #keeps blank tk window from popping up
filename = askopenfilename()
img = cv2.imread(filename)

#Select ROI window
#TODO loop to select multiple
fromCenter = False
r = cv2.selectROI("Cell Selection", img, fromCenter)

#Crop image
#TODO save center coord + length&width
#TODO select multiple ROI
#TODO redo selection with control+Z
#if cv2.waitKey(0):
#   cv2.destroyAllWindows()

#while True:
    
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
   
if cv2.waitKey(0):
    cv2.destroyAllWindows()

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

import sys, traceback, threading
thread_names = {t.ident: t.name for t in threading.enumerate()}
for thread_id, frame in sys._current_frames().iteritems():
    print("Thread %s:" % thread_names.get(thread_id, thread_id))
    traceback.print_stack(frame)
    print()
