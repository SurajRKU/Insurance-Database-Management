# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:23:45 2023

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
#from Delete_Insurance import *
#from Select_Insurance import *


def delorder(cnt_id):
    delroot=tk.Tk()
    cursor.execute("select Notice_id from Insured where Client_id=%s",(cnt_id,))
    record= cursor.fetchall()
    print(record[0][0])
    #rootnotfound=tk.Tk()
    width=delroot.winfo_reqwidth()
    height=delroot.winfo_reqheight()
    posright=int(delroot.winfo_screenwidth()/2-width/2-100)
    posleft=int(delroot.winfo_screenheight()/2-height/2)
    text=tk.Label(delroot,text="Details deleted successfully",fg="black")
    text.config(font=("Verdana",10))
    text.place(relx=0.5,rely=0.5,anchor=CENTER)
    delroot.geometry("400x150+{}+{}".format(posright,posleft))     
    
    
    cursor.execute("delete from Accident where FK_client_id=%s",(cnt_id,))
    
    cursor.execute("delete from Object where FKcli_id=%s",(cnt_id,))
    cursor.execute("delete from Report where FK_client_id=%s",(cnt_id,))
    cursor.execute("delete from Policy where FK_client_id=%s",(cnt_id,))
    cursor.execute("delete from _Account where FK_client_id=%s",(cnt_id,))
    cursor.execute("delete from Address where Client_id=%s",(cnt_id,))  
    cursor.execute("delete from Insurance where FK_client_id=%s",(cnt_id,))
    cursor.execute("delete from Insured where Client_id=%s",(cnt_id,))
    cursor.execute("delete from Notice where Notice_id=%s",(record[0][0],))  
  
    mydb.commit()    
  
       
    ok=tk.Button(delroot,text="OK",bg="light blue",fg="black",command=delroot.destroy)
    ok.place(relx=0.4,rely=0.65)
    ok.config(height=1,width=10)
    delroot.mainloop()