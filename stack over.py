# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 07:00:54 2018

@author: Ginny Wu
"""
from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

excelBrowse = Button(frame, text="Select Excel file")
excelBrowse.pack( side = TOP)


imgBrowse = Button(frame, text="Select image")
imgBrowse.pack( side = LEFT )

root.mainloop()


import Tkinter,tkFileDialog
root = Tkinter.Tk()
root.withdraw()

filename = tkFileDialog.askopenfilename(title='Choose an excel file')
print(filename)
print type(filename)
#file = str(filename)
file = [filetypes for filetypes in filename if ".xlsx" in filetypes]
workbook = xlrd.open_workbook(filename)
#for file in filename:
sheet = workbook.sheet_by_index(0)
print(sheet)

for value in sheet.row_values(0):
  print(value)
  print(type(value))

master = Tk()
variable=StringVar(master)
#variable=sheet.row_values(0)[0]
variable.set(sheet.row_values(0)[0])

#for var in value:
# variable = StringVar(master)
# variable.set(value) # default value

#w = OptionMenu(master, variable, value)
w = apply(OptionMenu, (master, variable) + tuple(sheet.row_values(0)))
w.pack()

mainloop()
