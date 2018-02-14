# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:09:33 2018

@author: gwu


cell labels
Table should look roughly like:
    ______________________________________________________________
    |Image | Cell # | ROI coord | labels/characteristics | ... TBA|
    |------------------------------------------------------------ |
    |      |        |           |                        |        |
    |      |        |           |                        |        | 

"""

import xlsxwriter


# Create an new Excel file and add a worksheet.
#EXCEL FILE CURRENTLY SAVES TO PATH:
#C:\Users\gwu\git\SBP-project
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Headers
locked = workbook.add_format()
locked.set_locked(True)
worksheet.write('A1', 'Image', bold)
worksheet.write('B1', 'Cell #', bold)

#Cell center coord, length, width
worksheet.write('C1', 'Cell Coord', bold)
worksheet.write('D1', 'Labels', bold)

# Insert an image.
#TODO image from different folder?
worksheet.insert_image('A1', 'logo.png')