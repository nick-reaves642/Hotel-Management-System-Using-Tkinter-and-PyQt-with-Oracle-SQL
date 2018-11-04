# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:33:12 2018

@author: nimis
"""
import cx_Oracle
import tkinter as tk
import tkinter.messagebox as mb

class New_User():
    def __init__(self,root):
        self.root=root
        self.root.title('Registeration Form')
        self.root.geometry('500x500')
        self.fullname=tk.StringVar()
        self.var = tk.StringVar()
        self.phone= tk.IntVar() 
        self.room=  tk.IntVar()
        
    def database(self):
        self.meth()
        name=self.fullname.get()
        gender=self.var.get()
        ph=self.phone.get()        
        if len(str(ph))!=10:
            mb.showwarning("Warning","You have not entered 10 digit number!!!")
            
        rm=self.room.get()
        conn=cx_Oracle.connect('hr/hr@localhost/orcl')
        
        cur=conn.cursor()
        cur.execute("select room_no from test")
        fl=0
        for x in cur:
            if rm in x:
                fl=1
        print("FLAG=",fl)
        if (fl==0):
            try:
                cur=conn.cursor()
                print("Block 1")
                cur.execute('insert into test(name,room_no,floor,available,entry,phone) values({},{},{},{},{},{})'.format("'"+name+"'",rm,int(rm/100),"'n'","sysdate",ph))
            except cx_Oracle.IntegrityError as e:
                fl=3
                cur=conn.cursor()
                mb.showerror('Error! in Test',e)
            except tk.TclError as e:
                mb.showerror('Error!',e)
            else:
                pass
                
                
        else:
            try:
                print("Block 2")
                cur.execute("update test set name={},floor={},available='n',entry=sysdate,phone={} where room_no={}".format("'"+name+"'",int(rm/100),ph,rm))
            except cx_Oracle.IntegrityError as e:
                fl=4
                mb.showerror('Error! in Test_2',e)
            else:
                pass
        
        
        if (fl!=3 and fl!=4):
            try:
                cur=conn.cursor()
                cur.execute("delete from avail where room_no="+str(rm))
                cur=conn.cursor()
                cur.execute('insert into customer(fullname,phone,gender,entry,room) values({},{},{},sysdate,{})'.format("'"+name+"'",ph,"'"+gender+"'",rm))
            except :
                pass
            else:
                mb.showinfo('Message','Input added to database')
        
        conn.commit()
        conn.close()
    

    def meth(self):
        
                
        label=tk.Label(self.root,text='Registeration Form',width=20,font=('bold',20))
        label.place(x=90,y=53)
        
        
        label_1=tk.Label(self.root,text='FullName',width=20,font=('bold',10))
        label_1.place(x=80,y=130)
        
        entry_1=tk.Entry(self.root,textvar=self.fullname)
        entry_1.place(x=240,y=130)
        
        
        label_2=tk.Label(self.root,text='Mobile no',width=20,font=('bold',10))
        label_2.place(x=80,y=170)
        
        entry_2=tk.Entry(self.root,textvar=self.phone)
        entry_2.place(x=240,y=170)
        
        
        label_3=tk.Label(self.root,text='Room',width=20,font=('bold',10))
        label_3.place(x=80,y=210)
        entry_3=tk.Entry(self.root,textvar=self.room)
        entry_3.place(x=240,y=210)
        
        label_3 =tk.Label(self.root,text="Gender",width=20,font=('bold',10))
        label_3.place(x=80,y=250)
        
        tk.Radiobutton(self.root, text="Male",padx = 5, variable=self.var, value='M').place(x=235,y=250)
        tk.Radiobutton(self.root, text="Female",padx = 20, variable=self.var, value='F').place(x=290,y=250)
        tk.Button(self.root, text='Submit',width=20,bg='brown',fg='white',command=self.database).place(x=180,y=290)
        
root=tk.Tk()
New_User(root).meth()
root.mainloop() 
        