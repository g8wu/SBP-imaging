# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:52:33 2018

@author: gwu
"""

from Tkinter import *
import Pmw

class SLabel (Frame):
    def __init__(self, master, leftl, rightl):
        Frame.__init__(self ,master, bg ='gray40')
        self.pack(side=LEFT,expand=YES, fill = BOTH)
    Label(self, text=leftl, fg='steelblue1',
          font=("arial", 6, "bold"), width = 5, bg='gary40').pack(
                  side=LEFT, expand=YES, fill=BOTH)