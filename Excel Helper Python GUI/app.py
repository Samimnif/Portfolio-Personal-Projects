from ast import Lambda
from tkinter import *
from tkinter import ttk
import tkinter
import xlrd
from tkinter.filedialog import askopenfilename
import xlwt
from xlwt import Workbook
from time import sleep


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
        self.master.geometry("400x500")
        self.submitU = ''
        self.entry = ''
        self.entriesU = []
        self.main()

    def main(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='  Welcome to Excel modifier\nChoose between these options\n\n')
        self.reg_txt.pack()
        self.get_sheet_btn = ttk.Button(self.frame1, text="New File creation", command=self.get_sheet)
        self.get_sheet_btn.pack()
        self.quit_btn = ttk.Button(self.frame1, text="Quit", command=self.master.destroy)
        self.quit_btn.pack()
    
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
        self.reg_txt3 = Text(self.frame3,font=("Helvetica", 10))
        self.reg_txt3.insert(INSERT,show_sheets(self.filename))
        self.reg_txt3.pack()
        self.frame3.pack()
        self.label = ttk.Label(self.frame3, text='Select sheet by enetring the number below:')
        self.label.pack()
        self.entry= Entry(self.frame3, width= 40)
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
        self.label2 = ttk.Label(self.frame4, text='For Reference')
        self.label2.pack()
        self.reg_txt4 = Text(self.frame4,font=("Helvetica", 10))
        self.reg_txt4.insert(INSERT,show_cols(self.filename, self.submitU))
        self.reg_txt4.pack()
        self.label3 = ttk.Label(self.frame4, text='Press Next to continue')
        self.label3.pack()
        self.sheetnumber_btn = ttk.Button(self.frame4, text="Next", command = self.creating)
        self.sheetnumber_btn.pack()
        self.main_btn = ttk.Button(self.frame4, text="Back to Main", command=self.main)
        self.main_btn.pack()
    
    def creating(self):
        #for i in self.root.winfo_children():
        #     i.destroy()
        self.root = Tk()
        self.root.title('Excel modifier')
        self.root.geometry("400x500")
        self.frame5 = Frame(self.root, width=300, height=300)
        self.frame5.pack()
        self.reg_txt5 = ttk.Label(self.frame5, text='How many columns for new sheet')
        self.reg_txt5.pack()
        self.entry= Entry(self.frame5, width= 40)
        self.entry.focus_set()
        self.entry.pack()
        self.sheetnumber_btn = ttk.Button(self.frame5, text="submit number", command = self.new_sheet)
        self.sheetnumber_btn.pack()
        self.main_btn = ttk.Button(self.frame5, text="Back to Main", command=self.main)
        self.main_btn.pack()
    def new_sheet(self):
        self.get_entry()
        for i in self.root.winfo_children():
            i.destroy()
        self.frame6 = Frame(self.root, width=300, height=300)
        self.frame6.grid(column = 1, row = 0)
        self.reg_txt6 = ttk.Label(self.frame6, text='Enter column number')
        self.reg_txt6.grid(column = 1, row = 0)
        self.reg_txt7 = ttk.Label(self.frame6, text='Enter new column name')
        self.reg_txt7.grid(column = 2, row = 0)
        self.entries = [Entry(self.frame6) for _ in range(int(self.submitU)*2)]
        n = 1
        nextLine= False
        for self.entry in self.entries:
            if nextLine:
                self.entry.grid(column = 2, row = n)
                nextLine =False
                n += 1
            else:
                self.reg_txt6 = ttk.Label(self.frame6, text=str(n))
                self.reg_txt6.grid(column = 0, row = n)
                self.entry.grid(column = 1, row = n)
                nextLine = True
        self.label4 = ttk.Label(self.frame6, text='New file Name:')
        self.label4.grid(column = 2, row = n+1)
        self.entryN= Entry(self.frame6)
        self.entryN.focus_set()
        self.entryN.grid(column = 2, row = n+2)
        self.sheetnumber_btn = ttk.Button(self.frame6, text="submit form", command = self.finalize)
        self.sheetnumber_btn.grid(column = 2, row = n+3)
        self.main_btn = ttk.Button(self.frame6, text="Back to Main", command=self.main)
        self.main_btn.grid(column = 2, row = n+4)
    def getEnteries(self):
        for self.entry in self.entries:
            self.entriesU.append(self.entry.get())
    
    def getName(self):
        self.submitU = self.entryN.get()
    def finalize(self):
        global externalS
        self.getEnteries()
        self.getName()
        for i in self.master.winfo_children():
            i.destroy()
        self.root.destroy()
        self.frame8 = Frame(self.master, width=300, height=300)
        self.frame8.pack()
        for self.entry in self.entriesU:
            print(self.entry)
        self.reg_txt5 = ttk.Label(self.frame8, text='Saving ...')
        self.reg_txt5.pack()
        self.pb1 = ttk.Progressbar(self.frame8, orient=HORIZONTAL, length=200, mode='determinate')
        self.pb1.pack(expand=True)
        wb = Workbook()
        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1')
        for i in range(len(self.entriesU)):
            self.frame8.update_idletasks()
            self.pb1['value'] += 200/len(self.entriesU)
            sleep(0.4)
            if i%2 == 1:
                colName = str(self.entriesU[i])
                importCol = int(self.entriesU[i-1])
                sheet1.write(0, i//2, colName)
                for m in range(1, externalS.nrows):
                    sheet1.write(m, i//2, externalS.cell_value(m, importCol) )
        wb.save(f'{self.submitU}.xls')
        self.main_btn = ttk.Button(self.frame8, text="Done!", command=self.endTask)
        self.main_btn.pack()
    def endTask(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame7 = Frame(self.master, width=300, height=300)
        self.frame7.pack()
        self.reg_txt = ttk.Label(self.frame7, text=f'Saved as: {self.submitU}.xls')
        self.reg_txt.pack()
        self.reg_txt2 = ttk.Label(self.frame7, text=f'Check your folder')
        self.reg_txt2.pack()
        self.reg_txt3 = ttk.Label(self.frame7, text=f'Thanks for using this app')
        self.reg_txt3.pack()
        self.get_sheet_btn = ttk.Button(self.frame7, text="Back to Main", command=self.main)
        self.get_sheet_btn.pack()
        self.quit_btn = ttk.Button(self.frame7, text="Quit", command=self.master.destroy)
        self.quit_btn.pack()

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

root = Tk()
app(root)
root.mainloop()
