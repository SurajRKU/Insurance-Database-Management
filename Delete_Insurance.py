# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:11:36 2023

@author: ASUS
"""
import random
import mysql
import mysql.connector
#from mysql import connector
#import mysql.connector as mysql
from datetime import date
from tkinter import *
import tkinter as tk

def delete():
    rootdel=tk.Tk()
    rootdel.geometry("1920x1080")
    text1=tk.Label(rootdel,text="Enter Client-id :",fg="black",font=12)
    text1.place(relx=0.3,rely=0.5)
 
    client=Entry(rootdel,width=20,selectborderwidth=50,font="Arial")
    client.place(relx=0.425,rely=0.5)
    
    def delt():
     cnt_id=str(client.get())
     
     cursor.execute("""select Insured_value from Object where FKcli_id= %s""",(cnt_id,))     
     record=str(cursor.fetchall())
 
     if record=="[]":
         rootnotfound1=tk.Tk()
         width=rootnotfound1.winfo_reqwidth()
         height=rootnotfound1.winfo_reqheight()
         
         posright=int(rootnotfound1.winfo_screenwidth()/2-width/2-100)
         posleft=int(rootnotfound1.winfo_screenheight()/2-height/2)
         text2=tk.Label(rootnotfound1,text="Record not found",fg="black")
         text2.config(font=("Verdana",12))
         text2.place(relx=0.5,rely=0.5,anchor=CENTER)
         rootnotfound1.geometry("400x150+{}+{}".format(posright,posleft))
         rootnotfound1.mainloop()    
         #rootdel.mainloop()    
     else:
         rooterdel=tk.Tk()
         cursor.execute("""select F_name,L_name from Insured where Client_id= %s""",(cnt_id,))     
         record=cursor.fetchall()
   
         width=rooterdel.winfo_reqwidth()
         height=rooterdel.winfo_reqheight()
         posright=int(rooterdel.winfo_screenwidth()/2-width/2-100)
         posleft=int(rooterdel.winfo_screenheight()/2-height/2)
         t1=record[0][0]
         t2=record[0][1]
         rooterdel.geometry("400x150+{}+{}".format(posright,posleft))
         text3=tk.Label(rooterdel,text="Are you sure to delete all the records associated with\n"+t1+" "+t2,fg="black")
         text3.config(font=("Verdana",10))
         text3.place(relx=0.5,rely=0.5,anchor=CENTER)
         def delok():
             delorder(cnt_id)
         confirm=tk.Button(rooterdel,text= "CONFIRM" ,bg="light blue",fg="black",command=delok)
         confirm.place(relx=0.4,rely=0.65)
         confirm.config(height=1,width=10)
         
         rooterdel.mainloop()    
         rootdel.mainloop()
         
         
    
    
    search=tk.Button(rootdel,text="DELETE",bg="black",fg="white",command=delt)
    search.place(relx=0.6,rely=0.5,) 
    search.configure(width=20,height=1)  