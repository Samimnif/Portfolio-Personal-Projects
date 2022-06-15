from tkinter import *
from tkinter import ttk
import tkinter
import xlrd
from tkinter.filedialog import askopenfilename
import xlwt
from xlwt import Workbook
import os


def show_sheets(loc):
    wb = xlrd.open_workbook(loc)
    n = 0
    strin=''
    for i in wb.sheet_names():
        strin += str(n)+'-  '+ i + '\n'
        n+=1
    return strin



class app:
    def __init__(self, master):
        self.master = master
        self.master.title('Excel modifier')
        self.master.geometry("500x500")
        self.submitU = ''
        self.entry = ''
        self.entriesU = []
        self.main()

    def main(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='Welcome to Excel modifier\nChoose between these options')
        self.reg_txt.pack()
        self.register_btn = ttk.Button(self.frame1, text="New File creation", command=self.get_sheet)
        self.register_btn.pack()
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.main_btn = ttk.Button(self.frame2, text="Back to Main", command=self.main)
        self.main_btn.pack()
    def get_entry(self):
        self.submitU = self.entry.get()
    def get_sheet(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.filename = askopenfilename()
        
        self.frame3 = Frame(self.master, width=300, height=300)
        self.frame3.pack()
        self.reg_txt3 = ttk.Label(self.frame3, text=show_sheets(self.filename))
        self.reg_txt3.pack()
        self.entry= Entry(self.master, width= 40)
        self.entry.focus_set()
        self.entry.pack()
        self.sheetnumber_btn = ttk.Button(self.frame3, text="submit number", command = self.get_col)
        self.sheetnumber_btn.pack()
        self.main_btn = ttk.Button(self.frame3, text="Back to Main", command=self.main)
        self.main_btn.pack()
    
    def get_col(self):
        self.get_entry()
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = Frame(self.master, width=300, height=300)
        self.frame4.pack()
        self.reg_txt4 = ttk.Label(self.frame4, text=show_cols(self.filename, self.submitU))
        self.reg_txt4.pack()
        # self.entry= Entry(self.master, width= 40)
        # self.entry.focus_set()
        # self.entry.pack()
        self.sheetnumber_btn = ttk.Button(self.frame4, text="Next", command = self.creating)
        self.sheetnumber_btn.pack()
        self.main_btn = ttk.Button(self.frame4, text="Back to Main", command=self.main)
        self.main_btn.pack()
    
    def creating(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        print(self.submitU)
        self.reg_txt5 = ttk.Label(self.frame5, text='How many columns for new sheet')
        self.reg_txt5.pack()
        self.entry= Entry(self.master, width= 40)
        self.entry.focus_set()
        self.entry.pack()
        self.sheetnumber_btn = ttk.Button(self.frame5, text="submit number", command = self.new_sheet)
        self.sheetnumber_btn.pack()
        self.main_btn = ttk.Button(self.frame5, text="Back to Main", command=self.main)
        self.main_btn.pack()
    def new_sheet(self):
        self.get_entry()
        for i in self.master.winfo_children():
            i.destroy()
        self.frame6 = Frame(self.master, width=300, height=300)
        self.frame6.grid(column = 1, row = 0)
        self.reg_txt6 = ttk.Label(self.frame6, text='Enter column number replacing')
        self.reg_txt6.grid(column = 1, row = 0)
        # self.entry= Entry(self.master, width= 40)
        # self.entry.focus_set()
        # self.entry.pack()
        self.entries = [Entry(self.frame6) for _ in range(int(self.submitU)*2)]
        n = 1
        nextLine= False
        for self.entry in self.entries:
            if nextLine:
                self.entry.grid(column = 2, row = n)
                #self.entry.pack()
                nextLine =False
                n += 1
            else:
                self.reg_txt6 = ttk.Label(self.frame6, text=str(n))
                self.reg_txt6.grid(column = 0, row = n)
                #self.reg_txt6.pack()
                self.entry.grid(column = 1, row = n)
                #self.entry.pack()
                nextLine = True
        self.sheetnumber_btn = ttk.Button(self.frame6, text="submit form", command = self.finalize)
        self.sheetnumber_btn.grid(column = 1, row = n+1)
        self.main_btn = ttk.Button(self.frame6, text="Back to Main", command=self.main)
        self.main_btn.grid(column = 1, row = n+2)
    def getEnteries(self):
        for self.entry in self.entries:
            self.entriesU.append(self.entry.get())

    def finalize(self):
        global externalS
        self.getEnteries()
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()
        for self.entry in self.entriesU:
            print(self.entry)
        self.reg_txt5 = ttk.Label(self.frame5, text='How many columns for new sheet')
        self.reg_txt5.pack()
        wb = Workbook()
        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1')
        for i in range(len(self.entriesU)):
            print(i)
            if i%2 == 1:
                colName = str(self.entriesU[i])
                importCol = int(self.entriesU[i-1])
                sheet1.write(0, i//2, colName)
                for m in range(1, externalS.nrows):
                    sheet1.write(m, i//2, externalS.cell_value(m, importCol) )
                    print('saved in col '+str(i))
        #newFile = input('new file name: ')
        #wb.save(f'{newFile}.xls')
        wb.save('new.xls')

        self.sheetnumber_btn = ttk.Button(self.frame5, text="submit number", command = self.new_sheet)
        self.sheetnumber_btn.pack()
        self.main_btn = ttk.Button(self.frame5, text="Back to Main", command=self.main)
        self.main_btn.pack()

def show_cols(loc, index):
    global externalS
    wb = xlrd.open_workbook(loc)
    strin=''
    if index == '':
        index = 0
    sheet = wb.sheet_by_index(int(index))
    externalS = sheet
    for i in range(sheet.ncols):
        strin += str(i)+"-  "+sheet.cell_value(0, i) + '\n'
    return strin

def newFile(loc):
    wb = xlrd.open_workbook(loc)
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



root = Tk()
app(root)
root.mainloop()