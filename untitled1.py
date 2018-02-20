# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:09:23 2018

@author: gwu
"""

from Tkinter import *

class App:
    def __init__(self, master, img = None):
        self.master = master
        self.browseButt()
        master.geometry("300x200")
    
    def getFile(self):
        self.withdraw()
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
           
    def browseButt(self):
        browse = Button(self)
        browse.pack(side= LEFT)
        browse.pack(side = BOTTOM)
        browse["text"] = "Browse",
        browse["command"] = self.getFile        


root = Tk()
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Cell Selection")
display = App(root)
root.mainloop()