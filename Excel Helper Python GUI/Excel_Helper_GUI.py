from ast import Lambda
from cgitb import text
from email import header
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter
from turtle import color, left
from webbrowser import BackgroundBrowser
import xlrd
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import xlwt
from xlwt import Workbook
from time import sleep
from datetime import datetime
import logging
import os

logfile = f"{str(os.path.dirname(os.path.abspath(__file__)))}/{(datetime.now()).strftime('%d-%m@%H;%M')} log.txt"

f = open(logfile,"w")
f.close()

logging.basicConfig(filename=logfile, level=logging.DEBUG)

try:
    def show_sheets(loc):
        wb = xlrd.open_workbook(loc)
        n = 0
        strin = ''
        for i in wb.sheet_names():
            strin += str(n)+'-  ' + i + '\n'
            n += 1
        return strin


    class app:
        def __init__(self, master):
            self.master = master
            self.master.title('Excel modifier')
            self.master.geometry("450x500")
            self.total=0
            self.submitU = ''
            self.entry = ''
            self.entriesU = []
            self.jack = {'room':[], 'Port ID':[], 'Native VLAN':[], 'VoIP VLAN Reply':[], 'Device ID':[], 'Jack ID':[]}
            self.main()

        def main(self):
            logging.debug('... Main Page ...')
            self.total = 0
            for i in self.master.winfo_children():
                i.destroy()
            self.frame1 = Frame(self.master, width=300, height=300)
            self.frame1.pack()
            self.reg_txt = ttk.Label(
                self.frame1, text='Welcome to Excel modifier\nChoose between these options\nWe accept only .xls Files.\nPlease make sure the file you are enetering is the correct extension.\n\n', justify='center')
            self.reg_txt.pack()
            self.get_sheet_btn = ttk.Button(
                self.frame1, text="New File creation", command=self.get_sheet)
            self.get_sheet_btn.pack()
            self.fetch_btn = ttk.Button(
                self.frame1, text="Wireshark fetch", command=self.fetch)
            self.fetch_btn.pack()
            self.quit_btn = ttk.Button(
                self.frame1, text="Quit", command=self.master.destroy)
            self.quit_btn.pack()
        def get_wireshark(self):
            self.submitU = self.text_area.get("1.0",END)
        def fetch(self):
            logging.debug('User selected Fetching data option')
            for i in self.master.winfo_children():
                i.destroy()
            self.frame2 = Frame(self.master, width=300, height=300)
            self.frame2.pack()
            self.reg_txt2 = ttk.Label(
                self.frame2, text='Enter the full Wireshark data in text field below\nMake sure you add the room # and the Jack ID in the text field below')
            self.reg_txt2.grid(column=0, row=1)#.pack()
            #self.entry = Entry(self.frame2, width=40)
            #self.entry.focus_set()
            #self.entry.pack()
            self.text_area = scrolledtext.ScrolledText(self.frame2, wrap=tkinter.WORD, width=50, height=8, font=("Arial", 10))
            self.text_area.insert(END, 'room: \nJack ID: ')
            self.text_area.grid(column=0, row=2, pady=10, padx=10)
            self.text_area.focus()
            self.next_btn = ttk.Button(self.frame2, text="Next", command=self.showing_data)
            self.next_btn.grid(column=0, row=3)
            self.main_btn = ttk.Button(self.frame2, text="Back to Main", command=self.main)
            self.main_btn.grid(column=0, row=4)
        def showing_data(self):
            self.total+=1
            #self.jack = {'room':'', 'Port ID':'', 'Native VLAN':'', 'VoIP VLAN Reply':'', 'Device ID':''}
            self.get_wireshark()
            for i in self.master.winfo_children():
                i.destroy()
            print(self.submitU)
            for line in self.submitU.split('\n'):
                for word in line.split(':'):
                    print (word.strip())
                    if word.strip() in self.jack:
                        print ('found')
                        self.jack[word.strip()].append((line.split(':')[(line.split(':').index(word))+1]).strip())
            for i in self.jack:
                if len(self.jack[i]) != self.total:
                    self.jack[i].append('None')
            logging.debug('Total Enteries: '+str(self.total) + ' ,DATA: '+str(self.jack))
            self.frame9 = Frame(self.master, width=300, height=300)
            self.frame9.pack()
            self.reg_txt11 = ttk.Label(self.frame9, text='Room:')
            self.reg_txt11.grid(column=0, row=1, sticky = 'w')
            self.reg_txt111 = ttk.Label(self.frame9, text=self.jack['room'][-1])
            self.reg_txt111.config(background="white")
            self.reg_txt111.grid(column=1, row=1, sticky = 'w')

            self.reg_txt1154 = ttk.Label(self.frame9, text='Jack ID:')
            self.reg_txt1154.grid(column=2, row=1, sticky = 'w')
            self.reg_txt11154 = ttk.Label(self.frame9, text=self.jack['Jack ID'][-1])
            self.reg_txt11154.config(background="white")
            self.reg_txt11154.grid(column=3, row=1, sticky = 'w')

            self.reg_txt12 = ttk.Label(self.frame9, text='Port ID:')
            self.reg_txt12.grid(column=0, row=2, sticky = 'w')
            self.reg_txt121 = ttk.Label(self.frame9, text=self.jack['Port ID'][-1])
            self.reg_txt121.config(background="white")
            self.reg_txt121.grid(column=1, row=2, sticky = 'w')
            self.reg_txt13 = ttk.Label(self.frame9, text='VLAN:')
            self.reg_txt13.grid(column=2, row=2, sticky = 'w')
            self.reg_txt131 = ttk.Label(self.frame9, text=self.jack['Native VLAN'][-1])
            self.reg_txt131.config(background="white")
            self.reg_txt131.grid(column=3, row=2, sticky = 'w')
            self.reg_txt14 = ttk.Label(self.frame9, text='VoIP VLAN:')
            self.reg_txt14.grid(column=0, row=3, sticky = 'w')
            self.reg_txt141 = ttk.Label(self.frame9, text=self.jack['VoIP VLAN Reply'][-1])
            self.reg_txt141.config(background="white")
            self.reg_txt141.grid(column=1, row=3, sticky = 'w')
            self.reg_txt15 = ttk.Label(self.frame9, text='Device ID:')
            self.reg_txt15.grid(column=2, row=3, sticky = 'w')
            self.reg_txt151 = ttk.Label(self.frame9, text=self.jack['Device ID'][-1])
            self.reg_txt151.config(background="white")
            self.reg_txt151.grid(column=3, row=3, sticky = 'w')
            self.frame10 = Frame(self.master, width=300, height=300)
            self.frame10.pack()
            self.reg_tt = ttk.Label(self.frame10, text = str(self.total))
            self.reg_tt.pack()
            self.add_btn = ttk.Button(self.frame10, text="Add", command=self.fetch)
            self.add_btn.pack()
            self.disregard2 = ttk.Button(self.frame10, text='Disregard this data', command=self.disregard_fn2)
            self.disregard2.pack()
            self.save_btn = ttk.Button(self.frame10, text="Save", command=self.save_data)
            self.save_btn.pack()
            self.main_btn = ttk.Button(self.frame10, text="Back to Main", command=self.main)
            self.main_btn.pack()
            self.disregard = ttk.Button(self.frame10, text='Disregard all data', command=self.disregard_fn)
            self.disregard.pack()
        def disregard_fn(self):
            self.jack = {'room':[], 'Port ID':[], 'Native VLAN':[], 'VoIP VLAN Reply':[], 'Device ID':[]}
            self.total=0
            self.reg_tt.config(text = str(self.total))
            logging.debug('User selected deleteing all data')
            self.message = ttk.Label(self.frame10, text='Deleted the data!')
            self.message.pack()
        def disregard_fn2(self):
            for i in self.jack:
                self.jack[i].pop()
            self.total -=1
            self.reg_tt.config(text = str(self.total))
            logging.debug('User selected deleting recent data only!')
            self.message = ttk.Label(self.frame10, text='Deleted recent data!')
            self.message.pack()
        def save_data(self):
            for i in self.master.winfo_children():
                i.destroy()
            logging.debug('Choosing saving data option ...')
            self.frame11 = Frame(self.master, width=300, height=300)
            self.frame11.pack()
            self.reg_txt20 = ttk.Label(self.frame11, text='Choose option to save current data')
            self.reg_txt20.pack()
            self.save_btn = ttk.Button(self.frame11, text='save as new file', command=self.saveasnew)
            self.save_btn.pack()
            self.main_btn = ttk.Button(self.frame11, text="Back to Main", command=self.main)
            self.main_btn.pack()
        def saveasnew(self):
            logging.debug('saving as new file ...')
            self.pb1 = ttk.Progressbar(self.frame11, orient=HORIZONTAL, length=200, mode='determinate')
            self.pb1.pack(expand=True)
            wb = Workbook()
            # add_sheet is used to create sheet.
            ws = wb.add_sheet('Sheet 1')
            columns = list(self.jack.keys())
            for i, header in enumerate(columns):
                ws.write(0, i, header)
            for j, col in enumerate(columns):
                self.frame11.update_idletasks()
                self.pb1['value'] += 200/len(self.jack)
                sleep(0.2)
                for i, row in enumerate(self.jack[col]):
                    print(i,row,' col:',j,col)
                    ws.write(i+1, j, row)
            files = [('Excel files', '*.xls')]
            self.file = asksaveasfilename(filetypes= files, defaultextension = files)
            wb.save(f'{self.file}')
            logging.debug('saving data as '+str(self.file))
            self.message = ttk.Label(self.frame11, text='Saved')
            self.message.pack()

        def get_entry(self):
            self.submitU = self.entry.get()
        def get_sheet(self):
            logging.debug('User selected making new file')
            for i in self.master.winfo_children():
                i.destroy()
            
            logging.debug('asking to open file ...')
            try:
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
            except Exception as Argument:
                logging.debug(str(Argument)+"\nUser didn't select a file, returning to main ...")
                self.main()
        
        def get_col(self):
            self.get_entry()
            logging.debug('Making a reference ...')
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
            # for i in self.root.winfo_children():
            #     i.destroy()
            logging.debug('new window')
            self.root = Tk()
            self.root.title('Excel modifier')
            self.root.geometry("450x500")
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
            logging.debug('creating new sheet with specific col&row')
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
            logging.debug(f'Saving data to a file named {self.submitU}.xls')
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
            logging.debug('end of process {creating new file} ...')
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
    logging.debug('-- Software Starting --')
    root = Tk()
    app(root)
    logging.debug('... main loop ...')
    root.mainloop()
    logging.debug('-- User Quit --')
except Exception as Argument:
    logging.critical(str(Argument))
