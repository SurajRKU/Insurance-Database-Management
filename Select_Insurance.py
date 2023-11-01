# -*- coding: utf-8 -*-

import random
import mysql
import mysql.connector
#from mysql import connector
#import mysql.connector as mysql
from datetime import date
from tkinter import *
import tkinter as tk


def polic():
     cursor.execute("""select * from Policy""")
   
     rootpol=tk.Tk()
     rootpol.geometry("1920x1080")
     rootpol.configure(background="light blue")
     text=tk.Label(rootpol,text="POLICY TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.45,rely=0.1)
     namelist=cursor.fetchall()
     output=[" |"+"\t"+"Policy Number"+"\t\t"+"|"+"\t\t"+"Policy Branch"+"\t\t\t"+"    |"+"\t"+"Premium Value"+"\t\t"+"|"+"\t\t"+"Client-Id"+"\t"+"|"+"\n"]
     t=Text(rootpol)
    
     for i in range(len(namelist)):
         output.append(" |"+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+str(namelist[i][1])+"\t\t\t"+"    |"+"\t"+str(namelist[i][2])+"\t\t"+"|"+"\t\t"+str(namelist[i][3])+"\t"+"|")
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=20,font=11)
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     rootpol.mainloop()
 
def notice():
     
     cursor.execute("""select* from Notice""")
     rootnot=tk.Tk()
     rootnot.geometry("1920x1080")
     rootnot.configure(background="light blue")
     namelist=cursor.fetchall()
     #output=[" "+"Notice id"+"\t\t\t\t"+"Notice type"+"\t\t\t\t"+"Description"+"\t\t\t\t"+"Notice Date"+"\n\n"]
     output=[" | "+"\t"+"Notice Id\t\t"+"|"+"\t\tNotice type\t\t"+"|"+"   \t\tDescription\t\t"+"|"+"\t\tNotice Date\t"+"|"+"\n"]
    # output.append()
     t=Text(rootnot)
     t=Text(rootnot)
     text=tk.Label(rootnot,text="NOTICE TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.425,rely=0.1)
     for i in range(len(namelist)):
         output.append(" | "+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+str(namelist[i][1])+"\t\t"+"|"+"\t\t"+str(namelist[i][2])+"\t\t"+"|"+"\t\t"+str(namelist[i][3])+"\t"+"|")
         
   
         #output.append(" "+str(namelist[i][0])+"\t\t\t\t"+str(namelist[i][1])+"\t\t\t\t"+str(namelist[i][2])+"\t\t\t\t"+str(namelist[i][3]))
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=20,font=11)
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     
     rootnot.mainloop()
def insurance():
     cursor.execute("""select * from Insurance""")
     rootie=tk.Tk()
     rootie.geometry("1920x1080")
     rootie.configure(background="light blue")
   
     namelist=cursor.fetchall()
     output=["  |  "+"Insurance Type"+"\t\t\t"+"|"+"\t\t\t"+"Insurance Plan"+"\t\t"+"\t"+"|"+"\t\t\t"+"Client Id"+"\t"+"|"+"\n\n"]
     t=Text(rootie)
     text=tk.Label(rootie,text="INSURANCE TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.425,rely=0.1)
     #text.configure(foreground="Light blue")
     
     for i in range(len(namelist)):
         output.append("  |  "+str(namelist[i][0])+"\t\t\t"+"|"+"\t\t\t"+str(namelist[i][1])+"\t\t\t"+"|"+"\t\t\t"+str(namelist[i][2])+"\t"+"|")
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=20,font=12)
         t.tag_configure(x,background="light blue",foreground="green")
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     
     rootie.mainloop()

def insured():
     #Client_id, Notice_id, F_name, L_name, Sex, Contact_person, Address
     cursor.execute("""select* from Insured""")
     rootins=tk.Tk()
     rootins.geometry("1920x1080")
     rootins.configure(background="light blue")
     text=tk.Label(rootins,text="INSURED TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.425,rely=0.1)
     namelist=cursor.fetchall()
     output=[" |"+"\tClient-id"+"\t"+"|"+"\t"+"Notice Id"+"\t"+"|"+"\t"+"First name"+"\t"+"|"+"\t"+"Last name"+"\t"+"|"+"\t"+"Sex"+"\t"+"|"+"\t"+"Contact person"+"\t"+"|"+"\t"+"City"+"\t|"+"\n"]
     t=Text(rootins)
    
     for i in range(len(namelist)):
         output.append(" | "+"\t"+str(namelist[i][0])+"\t"+"|"+"\t"+str(namelist[i][1])+"\t"+"|"+"\t"+str(namelist[i][2])+"\t"+"|"+"\t"+str(namelist[i][3])+"\t"+"|"+"\t"+str(namelist[i][4])+"\t"+"|"+"\t"+str(namelist[i][5])+"\t"+"|"+"\t"+str(namelist[i][6])+"\t|")
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=25,font=11)
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     rootins.mainloop()
     
     
     #Object_id, Object_name, , Insured_value, , FKcli_id, FKpay_id
     
def Object():
     #Client_id, Notice_id, F_name, L_name, Sex, Contact_person, Address
     cursor.execute("""select* from Object""")
     rootobj=tk.Tk()
     rootobj.geometry("1920x1080")
     rootobj.configure(background="light blue")
     text=tk.Label(rootobj,text="OBJECT TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.425,rely=0.1)
     namelist=cursor.fetchall()
     output=[" |"+"\tObject-Id"+"\t"+"|"+"\t"+"Object name"+"\t"+"|"+"\t"+"Object type"+"\t"+"|"+"        "+"Insured value"+"\t"+"|"+"\t"+"         Year of insurance"+"\t"+"|"+"\t"+"Client Id            "+"\t"+"|"+"\t"+" Payment Id\t\t"+"|"+"\n"]
     t=Text(rootobj)
    
     for i in range(len(namelist)):
        # output.append(" |"+"\t"+str(namelist[i][0])+"\t\t"+str(namelist[i][1])+"\t\t"+str(namelist[i][2])+"\t\t"+str(namelist[i][3])+"\t\t"+str(namelist[i][4])+"\t\t"+str(namelist[i][5])+"\t\t"+str(namelist[i][6]))
         output.append(" | "+"\t"+str(namelist[i][0])+"\t"+"|"+"\t"+str(namelist[i][1])+"\t"+"|"+"\t"+str(namelist[i][2])+"\t"+"|"+"\t"+str(namelist[i][3])+"\t"+"|"+"\t"+str(namelist[i][4])+"\t"+"|"+"\t"+str(namelist[i][5])+"\t"+"|"+"\t"+str(namelist[i][6])+"\t"+"|")
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=25,font=11)
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     rootobj.mainloop()     
     
     
     
def account():
     
     
     cursor.execute("""select* from _Account""")
     rootobj1=tk.Tk()
     rootobj1.geometry("1920x1080")
     rootobj1.configure(background="light blue")
     namelist=cursor.fetchall()
     text=tk.Label(rootobj1,text="ACCOUNT TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.425,rely=0.1)
     output=[" | "+"\tAccount Id\t\t"+"|"+"\tUsername\t\t"+"|"+"\tPassword\t\t"+"|"+"\tUserRole\t\t"+"|"+"\tClient Id\t"+"|"+"\n"]
     t=Text(rootobj1)
    
     for i in range(len(namelist)):
         output.append(" | "+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t"+str(namelist[i][1])+"\t\t"+"|"+"\t"+str(namelist[i][2])+"\t\t"+"|"+"\t"+str(namelist[i][3])+"\t\t"+"|"+"\t"+str(namelist[i][4])+"\t"+"|")
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=25,font=11)
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     rootobj1.mainloop()     
def payment():
  
     cursor.execute("""select* from Payment""")
     rootobj2=tk.Tk()
     rootobj2.geometry("1920x1080")
     rootobj2.configure(background="light blue")
     namelist=cursor.fetchall()
     output=[" | "+"\t"+"Payment Id\t\t"+"|"+"\t\tPayment date\t\t"+"|"+"\t\tAmount paid\t\t"+"|"+"\t\tClient Id\t"+"|"+"\n"]
    # output.append()
     t=Text(rootobj2)
     text=tk.Label(rootobj2,text="PAYMENT TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.425,rely=0.1)
     for i in range(len(namelist)):
         output.append(" | "+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+str(namelist[i][1])+"\t\t"+"|"+"\t\t"+str(namelist[i][2])+"\t\t"+"|"+"\t\t"+str(namelist[i][3])+"\t"+"|")
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=25,font=11)
     t.place(relx=0.1,rely=0.2)    
    # print(output)
     rootobj2.mainloop()        
     
def report():
  
     cursor.execute("""select* from Report""")
     rootobj3=tk.Tk()
     rootobj3.geometry("1920x1080")
     rootobj3.configure(background="light blue")
     namelist=cursor.fetchall()
     text=tk.Label(rootobj3,text="REPORT TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.435,rely=0.1)
     output=[" |"+ "\tReport Id\t\t" + "|" + "\t\tReport date\t\t" + "|" + "\t\tReport type\t\t"+ "\t|"+ "\tClient Id\t" + "|" +"\n" ]
     t=Text(rootobj3)
    
     for i in range(len(namelist)):
         output.append(" |" + "\t"+str(namelist[i][0])+"\t\t" + "|" +"\t\t"+str(namelist[i][1])+"\t\t"+"|"+"\t\t"+str(namelist[i][2])+"\t\t\t"+"|"+"\t"+str(namelist[i][3])+"\t"+"|")
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=25,font=11)
     t.place(relx=0.1,rely=0.2)    
     
     rootobj3.mainloop()        
def address():
     #Client_id, Address
     cursor.execute("""select* from Address""")
     rootobj4=tk.Tk()
     rootobj4.geometry("1920x1080")
     rootobj4.configure(background="light blue")
     namelist=cursor.fetchall()
     text=tk.Label(rootobj4,text="ADDRESS TABLE")
     text.config(font=("Verdana",16))
     text.place(relx=0.435,rely=0.1)
     output=["\t|"+"\t"+"Client Id"+"\t\t"+"|"+"\t\t"+"\tAddress"+"   "+"\n"]
     t=Text(rootobj4)
    
     for i in range(len(namelist)):
         output.append("\t"+"|"+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+ "\t"+str(namelist[i][1]))
         
   
     for x in output:
         t.insert(END,x+'\n\n')
         t.configure(width=120,height=25,font=11)
     t.place(relx=0.1,rely=0.2)    
     #print(output)
     rootobj4.mainloop()                  
     
     
     
     