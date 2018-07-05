# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:34:38 2018

@author: Ginny Wu
"""

from PIL import Image
import matplotlib.pyplot as plt
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from tkFileDialog import askopenfilename
import xlsxwriter
import unicodedata


class cellImg:
    
    def __init__(self):
        excelFile = ""           # Global container: Selected Excel file with ROI coordinates
        imgFile = ""             # Global container: Selected image file to crop
        root = Tk()
        root.title("Cell Imaging")
        frame = Frame(root)
        frame.pack()
        
        excelBrowse = Button(frame, text="Select Excel file", command = self.getExcel)
        excelBrowse.pack(side = TOP)
        
        imgBrowse = Button(frame, text="Select image",command = self.getImg)
        imgBrowse.pack(side = LEFT)
        
        
        
        root.mainloop()

    # Open file browser and select Excel file
    ###########################################
    def getExcel(self):
        Tk().withdraw()
        excelFile = askopenfilename(filetypes = [("Excel files", "*.xlsx")])
        print excelFile
        
        
    # Open file browser and select image file
    ###########################################
    def getImg(self):
        Tk().withdraw()
        imgFile = askopenfilename()
        
        img = plt.imread(imgFile)
        plt.imshow(img)
        print imgFile

    
    # Set up selected Excel file with column titles for new input
    # ROI column (AY) for cropped image insert
    # Tags column (AZ) with dropdown options for tags
    ############################################
    def excelSetup(self):
        wb = xlsxwriter.Workbook(filename = excelFile)
        print excelFile
        ws = wb.add_worksheet()
        
        # To keep rows linked with added images, set cell height to fit cropped images
        # Later in imgSetup, anchor the image to the cell
        ws.set_default_row(150)
        
        
        # P2 is Bounding Box column
        boundBox = ws['P2']
        boundBox = boundBox.value[1:-1]     # reads coordinates in the cell between the brackets (ASCII)
        box1 = (boundBox)
        
        roi = openpyxl.drawing.image.Image(filename)
        roi.anchor(ws.cell('A1'))
        ws.add_image(roi)
        
        ws.write('AY', 'ROI')
        ws.write('AZ', 'Tags')
        
        # Dummy: limiting input to a value in a dropdown list.
        '''
        txt = 'Select a value from a drop down list (using a cell range)'
        
        worksheet.write('A15', txt)
        worksheet.data_validation('B15', {'validate': 'list', 
                                          'source': ['differentiated', 'undifferentiated', 'Trait1', 'Trait2']})
        '''
        
        wb.save('output.xlsx')
        
    
    # Load selected image file
    # Crop using Bounding Box coordinates
    ############################################
    def imgSetup(self):
        img = Image.open(imgFile)
        roi = openpyxl.drawing.image.Image(excelFile)
        roi.anchor(ws.cell('A1'))
        ws.add_image(roi)
        
        
    def main():
        app = cellImg()
        app.excelSetup(self)

# instance of class
cellImg()