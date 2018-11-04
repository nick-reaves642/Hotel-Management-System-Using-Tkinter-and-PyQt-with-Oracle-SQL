# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:18:42 2018

@author: nimish
"""

import tkinter as tk
from tkinter import messagebox as mb
from Oracle_connect import connect

class Login:
    def __init__(self,master):
        self.master=master
        master.title('Login Screen')
        self.center()
        tk.Label(self.master,text="Username: ").grid(row=1)
        tk.Label(self.master,text="Password: ").grid(row=2)
        self.e1=tk.Entry(self.master)
        self.e1.grid(row=1,column=1)
        self.e2=tk.Entry(self.master,show='*')
        self.e2.grid(row=2,column=1)
        B=tk.Button(self.master,text='Login',fg='green',command=self.clicked)
        B.place(relx=0.34,rely=0.7,anchor='c',bordermode='outside')
    def center(self):
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w=250
        h=100
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def encrypt(self,message):
        result=''
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)
        return result
    def decrypt(self,message):
        result=''
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)
        return result
    def clicked(self):
        str1=str(self.e1.get())
        str2=str(self.e2.get())
        obj[0].execute('select * from id_pass_tab')
        fl=0
        for result in obj[0]:
            if (str1==result[0]):
                fl=1
                if(self.encrypt(str2)!=result[1]):
                    mb.showerror('Error','Password Incorrect')
                else:
                    import main_win_2
                    main_win_2.db_run()
        if (fl==0):
            mb.showerror('Error','User does not exist\nContact Administrator...')       
            
obj=connect()        
root=tk.Tk()
Login(root)
root.mainloop()
obj[0].close()
obj[1].close()
