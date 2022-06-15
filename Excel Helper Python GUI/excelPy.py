# Reading an excel file using Python
import xlrd
from tkinter.filedialog import askopenfilename
import xlwt
from xlwt import Workbook


def newFile():
    # Give the location of the file
    filename = askopenfilename()
    loc = filename #("/Users/samimnif/Downloads/HardwareList.xls")

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    # For row 0 and column 0
    n = 0
    for i in wb.sheet_names():
        print (str(n)+'-  '+ i)
        n+=1
    sheetnumber = int(input('sheet number: '))
    sheet = wb.sheet_by_index(sheetnumber)

    for i in range(sheet.ncols):
        print (str(i)+"-  "+sheet.cell_value(0, i))
    col = int(input('Eneter number of columnss: '))
    wb = Workbook()
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    for i in range(col):
        importCol = int(input('select column inport from original: '))
        colName = input('column name: ')
        sheet1.write(0, i, colName)
        for m in range(1, sheet.nrows):
            sheet1.write(m, i, sheet.cell_value(m, importCol) )
    newFile = input('new file name: ')
    wb.save(f'{newFile}.xls')
    
newFile()