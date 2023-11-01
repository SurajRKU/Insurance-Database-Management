import random
import mysql
import mysql.connector
#from mysql import connector
#import mysql.connector as mysql
from datetime import date
from tkinter import *
import tkinter as tk
from Delete_Insurance import *
from Select_Insurance import *
from Delorder_Client import * 


#mydb=mysql.connector.connect(host="localhost",user="root",passwd="Suraj@mysql3577",database="InsurancePro")
mydb = mysql.connector.connect(database='insurancepro', host='localhost', port='3306',
                   user='root', password= 'Suraj@mysql3577',auth_plugin = 'mysql_native_password')

cursor=mydb.cursor()   
#def close(rooter):
 #   rooter.destroy()
 # cn_id=999
 #cursor.execute("delete from Accident where FK_client_id=%s",(cn_id,))
 #mydb.commit()
# def delorder(cnt_id):
#     delroot=tk.Tk()
#     cursor.execute("select Notice_id from Insured where Client_id=%s",(cnt_id,))
#     record= cursor.fetchall()
#     print(record[0][0])
#     #rootnotfound=tk.Tk()
#     width=delroot.winfo_reqwidth()
#     height=delroot.winfo_reqheight()
#     posright=int(delroot.winfo_screenwidth()/2-width/2-100)
#     posleft=int(delroot.winfo_screenheight()/2-height/2)
#     text=tk.Label(delroot,text="Details deleted successfully",fg="black")
#     text.config(font=("Verdana",10))
#     text.place(relx=0.5,rely=0.5,anchor=CENTER)
#     delroot.geometry("400x150+{}+{}".format(posright,posleft))     
    
    
#     cursor.execute("delete from Accident where FK_client_id=%s",(cnt_id,))
    
#     cursor.execute("delete from Object where FKcli_id=%s",(cnt_id,))
#     cursor.execute("delete from Report where FK_client_id=%s",(cnt_id,))
#     cursor.execute("delete from Policy where FK_client_id=%s",(cnt_id,))
#     cursor.execute("delete from _Account where FK_client_id=%s",(cnt_id,))
#     cursor.execute("delete from Address where Client_id=%s",(cnt_id,))  
#     cursor.execute("delete from Insurance where FK_client_id=%s",(cnt_id,))
#     cursor.execute("delete from Insured where Client_id=%s",(cnt_id,))
#     cursor.execute("delete from Notice where Notice_id=%s",(record[0][0],))  
  
#     mydb.commit()    
  
       
#     ok=tk.Button(delroot,text="OK",bg="light blue",fg="black",command=delroot.destroy)
#     ok.place(relx=0.4,rely=0.65)
#     ok.config(height=1,width=10)
#     delroot.mainloop()
    
    
    
    
def updatter(ac_ty,ac_re,ac_date,ac_loc,ac_claimed,clienter):
    
    query="""update Accident set Accident_type=%s,Accident_reason=%s,Accident_date=%s,Accident_location=%s,claimed=%s where FK_client_id= %s"""
    records=[ac_ty,ac_re,ac_date,ac_loc,ac_claimed,clienter]
    cursor.execute(query,records)   
    mydb.commit()         
    
# def delete():
#     rootdel=tk.Tk()
#     rootdel.geometry("1920x1080")
#     text1=tk.Label(rootdel,text="Enter Client-id :",fg="black",font=12)
#     text1.place(relx=0.3,rely=0.5)
 
#     client=Entry(rootdel,width=20,selectborderwidth=50,font="Arial")
#     client.place(relx=0.425,rely=0.5)
    
#     def delt():
#      cnt_id=str(client.get())
     
#      cursor.execute("""select Insured_value from Object where FKcli_id= %s""",(cnt_id,))     
#      record=str(cursor.fetchall())
 
#      if record=="[]":
#          rootnotfound1=tk.Tk()
#          width=rootnotfound1.winfo_reqwidth()
#          height=rootnotfound1.winfo_reqheight()
         
#          posright=int(rootnotfound1.winfo_screenwidth()/2-width/2-100)
#          posleft=int(rootnotfound1.winfo_screenheight()/2-height/2)
#          text2=tk.Label(rootnotfound1,text="Record not found",fg="black")
#          text2.config(font=("Verdana",12))
#          text2.place(relx=0.5,rely=0.5,anchor=CENTER)
#          rootnotfound1.geometry("400x150+{}+{}".format(posright,posleft))
#          rootnotfound1.mainloop()    
#          #rootdel.mainloop()    
#      else:
#          rooterdel=tk.Tk()
#          cursor.execute("""select F_name,L_name from Insured where Client_id= %s""",(cnt_id,))     
#          record=cursor.fetchall()
   
#          width=rooterdel.winfo_reqwidth()
#          height=rooterdel.winfo_reqheight()
#          posright=int(rooterdel.winfo_screenwidth()/2-width/2-100)
#          posleft=int(rooterdel.winfo_screenheight()/2-height/2)
#          t1=record[0][0]
#          t2=record[0][1]
#          rooterdel.geometry("400x150+{}+{}".format(posright,posleft))
#          text3=tk.Label(rooterdel,text="Are you sure to delete all the records associated with\n"+t1+" "+t2,fg="black")
#          text3.config(font=("Verdana",10))
#          text3.place(relx=0.5,rely=0.5,anchor=CENTER)
#          def delok():
#              delorder(cnt_id)
#          confirm=tk.Button(rooterdel,text= "CONFIRM" ,bg="light blue",fg="black",command=delok)
#          confirm.place(relx=0.4,rely=0.65)
#          confirm.config(height=1,width=10)
         
#          rooterdel.mainloop()    
#          rootdel.mainloop()
         
         
    
    
    search=tk.Button(rootdel,text="DELETE",bg="black",fg="white",command=delt)
    search.place(relx=0.6,rely=0.5,) 
    search.configure(width=20,height=1)       
   
   
    
    
# def polic():
#      cursor.execute("""select * from Policy""")
   
#      rootpol=tk.Tk()
#      rootpol.geometry("1920x1080")
#      rootpol.configure(background="light blue")
#      text=tk.Label(rootpol,text="POLICY TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.45,rely=0.1)
#      namelist=cursor.fetchall()
#      output=[" |"+"\t"+"Policy Number"+"\t\t"+"|"+"\t\t"+"Policy Branch"+"\t\t\t"+"    |"+"\t"+"Premium Value"+"\t\t"+"|"+"\t\t"+"Client-Id"+"\t"+"|"+"\n"]
#      t=Text(rootpol)
    
#      for i in range(len(namelist)):
#          output.append(" |"+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+str(namelist[i][1])+"\t\t\t"+"    |"+"\t"+str(namelist[i][2])+"\t\t"+"|"+"\t\t"+str(namelist[i][3])+"\t"+"|")
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=20,font=11)
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
#      rootpol.mainloop()
 
# def notice():
     
#      cursor.execute("""select* from Notice""")
#      rootnot=tk.Tk()
#      rootnot.geometry("1920x1080")
#      rootnot.configure(background="light blue")
#      namelist=cursor.fetchall()
#      #output=[" "+"Notice id"+"\t\t\t\t"+"Notice type"+"\t\t\t\t"+"Description"+"\t\t\t\t"+"Notice Date"+"\n\n"]
#      output=[" | "+"\t"+"Notice Id\t\t"+"|"+"\t\tNotice type\t\t"+"|"+"   \t\tDescription\t\t"+"|"+"\t\tNotice Date\t"+"|"+"\n"]
#     # output.append()
#      t=Text(rootnot)
#      t=Text(rootnot)
#      text=tk.Label(rootnot,text="NOTICE TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.425,rely=0.1)
#      for i in range(len(namelist)):
#          output.append(" | "+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+str(namelist[i][1])+"\t\t"+"|"+"\t\t"+str(namelist[i][2])+"\t\t"+"|"+"\t\t"+str(namelist[i][3])+"\t"+"|")
         
   
#          #output.append(" "+str(namelist[i][0])+"\t\t\t\t"+str(namelist[i][1])+"\t\t\t\t"+str(namelist[i][2])+"\t\t\t\t"+str(namelist[i][3]))
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=20,font=11)
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
     
#      rootnot.mainloop()
# def insurance():
#      cursor.execute("""select * from Insurance""")
#      rootie=tk.Tk()
#      rootie.geometry("1920x1080")
#      rootie.configure(background="light blue")
   
#      namelist=cursor.fetchall()
#      output=["  |  "+"Insurance Type"+"\t\t\t"+"|"+"\t\t\t"+"Insurance Plan"+"\t\t"+"\t"+"|"+"\t\t\t"+"Client Id"+"\t"+"|"+"\n\n"]
#      t=Text(rootie)
#      text=tk.Label(rootie,text="INSURANCE TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.425,rely=0.1)
#      #text.configure(foreground="Light blue")
     
#      for i in range(len(namelist)):
#          output.append("  |  "+str(namelist[i][0])+"\t\t\t"+"|"+"\t\t\t"+str(namelist[i][1])+"\t\t\t"+"|"+"\t\t\t"+str(namelist[i][2])+"\t"+"|")
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=20,font=12)
#          t.tag_configure(x,background="light blue",foreground="green")
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
     
#      rootie.mainloop()

# def insured():
#      #Client_id, Notice_id, F_name, L_name, Sex, Contact_person, Address
#      cursor.execute("""select* from Insured""")
#      rootins=tk.Tk()
#      rootins.geometry("1920x1080")
#      rootins.configure(background="light blue")
#      text=tk.Label(rootins,text="INSURED TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.425,rely=0.1)
#      namelist=cursor.fetchall()
#      output=[" |"+"\tClient-id"+"\t"+"|"+"\t"+"Notice Id"+"\t"+"|"+"\t"+"First name"+"\t"+"|"+"\t"+"Last name"+"\t"+"|"+"\t"+"Sex"+"\t"+"|"+"\t"+"Contact person"+"\t"+"|"+"\t"+"City"+"\t|"+"\n"]
#      t=Text(rootins)
    
#      for i in range(len(namelist)):
#          output.append(" | "+"\t"+str(namelist[i][0])+"\t"+"|"+"\t"+str(namelist[i][1])+"\t"+"|"+"\t"+str(namelist[i][2])+"\t"+"|"+"\t"+str(namelist[i][3])+"\t"+"|"+"\t"+str(namelist[i][4])+"\t"+"|"+"\t"+str(namelist[i][5])+"\t"+"|"+"\t"+str(namelist[i][6])+"\t|")
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=25,font=11)
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
#      rootins.mainloop()
     
     
#      #Object_id, Object_name, , Insured_value, , FKcli_id, FKpay_id
     
# def Object():
#      #Client_id, Notice_id, F_name, L_name, Sex, Contact_person, Address
#      cursor.execute("""select* from Object""")
#      rootobj=tk.Tk()
#      rootobj.geometry("1920x1080")
#      rootobj.configure(background="light blue")
#      text=tk.Label(rootobj,text="OBJECT TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.425,rely=0.1)
#      namelist=cursor.fetchall()
#      output=[" |"+"\tObject-Id"+"\t"+"|"+"\t"+"Object name"+"\t"+"|"+"\t"+"Object type"+"\t"+"|"+"        "+"Insured value"+"\t"+"|"+"\t"+"         Year of insurance"+"\t"+"|"+"\t"+"Client Id            "+"\t"+"|"+"\t"+" Payment Id\t\t"+"|"+"\n"]
#      t=Text(rootobj)
    
#      for i in range(len(namelist)):
#         # output.append(" |"+"\t"+str(namelist[i][0])+"\t\t"+str(namelist[i][1])+"\t\t"+str(namelist[i][2])+"\t\t"+str(namelist[i][3])+"\t\t"+str(namelist[i][4])+"\t\t"+str(namelist[i][5])+"\t\t"+str(namelist[i][6]))
#          output.append(" | "+"\t"+str(namelist[i][0])+"\t"+"|"+"\t"+str(namelist[i][1])+"\t"+"|"+"\t"+str(namelist[i][2])+"\t"+"|"+"\t"+str(namelist[i][3])+"\t"+"|"+"\t"+str(namelist[i][4])+"\t"+"|"+"\t"+str(namelist[i][5])+"\t"+"|"+"\t"+str(namelist[i][6])+"\t"+"|")
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=25,font=11)
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
#      rootobj.mainloop()     
     
     
     
# def account():
     
     
#      cursor.execute("""select* from _Account""")
#      rootobj1=tk.Tk()
#      rootobj1.geometry("1920x1080")
#      rootobj1.configure(background="light blue")
#      namelist=cursor.fetchall()
#      text=tk.Label(rootobj1,text="ACCOUNT TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.425,rely=0.1)
#      output=[" | "+"\tAccount Id\t\t"+"|"+"\tUsername\t\t"+"|"+"\tPassword\t\t"+"|"+"\tUserRole\t\t"+"|"+"\tClient Id\t"+"|"+"\n"]
#      t=Text(rootobj1)
    
#      for i in range(len(namelist)):
#          output.append(" | "+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t"+str(namelist[i][1])+"\t\t"+"|"+"\t"+str(namelist[i][2])+"\t\t"+"|"+"\t"+str(namelist[i][3])+"\t\t"+"|"+"\t"+str(namelist[i][4])+"\t"+"|")
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=25,font=11)
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
#      rootobj1.mainloop()     
# def payment():
  
#      cursor.execute("""select* from Payment""")
#      rootobj2=tk.Tk()
#      rootobj2.geometry("1920x1080")
#      rootobj2.configure(background="light blue")
#      namelist=cursor.fetchall()
#      output=[" | "+"\t"+"Payment Id\t\t"+"|"+"\t\tPayment date\t\t"+"|"+"\t\tAmount paid\t\t"+"|"+"\t\tClient Id\t"+"|"+"\n"]
#     # output.append()
#      t=Text(rootobj2)
#      text=tk.Label(rootobj2,text="PAYMENT TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.425,rely=0.1)
#      for i in range(len(namelist)):
#          output.append(" | "+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+str(namelist[i][1])+"\t\t"+"|"+"\t\t"+str(namelist[i][2])+"\t\t"+"|"+"\t\t"+str(namelist[i][3])+"\t"+"|")
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=25,font=11)
#      t.place(relx=0.1,rely=0.2)    
#     # print(output)
#      rootobj2.mainloop()        
     
# def report():
  
#      cursor.execute("""select* from Report""")
#      rootobj3=tk.Tk()
#      rootobj3.geometry("1920x1080")
#      rootobj3.configure(background="light blue")
#      namelist=cursor.fetchall()
#      text=tk.Label(rootobj3,text="REPORT TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.435,rely=0.1)
#      output=[" |"+ "\tReport Id\t\t" + "|" + "\t\tReport date\t\t" + "|" + "\t\tReport type\t\t"+ "\t|"+ "\tClient Id\t" + "|" +"\n" ]
#      t=Text(rootobj3)
    
#      for i in range(len(namelist)):
#          output.append(" |" + "\t"+str(namelist[i][0])+"\t\t" + "|" +"\t\t"+str(namelist[i][1])+"\t\t"+"|"+"\t\t"+str(namelist[i][2])+"\t\t\t"+"|"+"\t"+str(namelist[i][3])+"\t"+"|")
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=25,font=11)
#      t.place(relx=0.1,rely=0.2)    
     
#      rootobj3.mainloop()        
# def address():
#      #Client_id, Address
#      cursor.execute("""select* from Address""")
#      rootobj4=tk.Tk()
#      rootobj4.geometry("1920x1080")
#      rootobj4.configure(background="light blue")
#      namelist=cursor.fetchall()
#      text=tk.Label(rootobj4,text="ADDRESS TABLE")
#      text.config(font=("Verdana",16))
#      text.place(relx=0.435,rely=0.1)
#      output=["\t|"+"\t"+"Client Id"+"\t\t"+"|"+"\t\t"+"\tAddress"+"   "+"\n"]
#      t=Text(rootobj4)
    
#      for i in range(len(namelist)):
#          output.append("\t"+"|"+"\t"+str(namelist[i][0])+"\t\t"+"|"+"\t\t"+ "\t"+str(namelist[i][1]))
         
   
#      for x in output:
#          t.insert(END,x+'\n\n')
#          t.configure(width=120,height=25,font=11)
#      t.place(relx=0.1,rely=0.2)    
#      #print(output)
#      rootobj4.mainloop()                  
     
     
     
     
     
def select():
   rootup=tk.Tk()
   rootup.geometry("1920x1080")
   rootup.configure(background="light yellow") 
   button1= tk.Button(rootup,text="INSURED TABLE",width=30,bg="light blue",fg="black",command=insured)
   button1.place(relx=0.5,rely=0.2,anchor=CENTER)
  
   button2= tk.Button(rootup,text="INSURANCE TABLE",width=30,bg="light blue",fg="black",command=insurance)
   button2.place(relx=0.5,rely=0.275,anchor=CENTER)
   
   button3= tk.Button(rootup,text="NOTICE TABLE",width=30,bg="light blue",fg="black",command=notice)
   button3.place(relx=0.5,rely=0.35,anchor=CENTER)
   
   button4= tk.Button(rootup,text="OBJECT TABLE",width=30,bg="light blue",fg="black",command=Object)
   button4.place(relx=0.5,rely=0.425,anchor=CENTER)
   
    
   button5= tk.Button(rootup,text="PAYMENT TABLE",width=30,bg="light blue",fg="black",command=payment)
   button5.place(relx=0.5,rely=0.5,anchor=CENTER)
   
    
   button5= tk.Button(rootup,text="POLICY TABLE",width=30,bg="light blue",fg="black",command=polic)#,command=insertwindow)
   button5.place(relx=0.5,rely=0.575,anchor=CENTER)
   
    
   button6= tk.Button(rootup,text="ADDRESS TABLE",width=30,bg="light blue",fg="black",command=address)
   button6.place(relx=0.5,rely=0.65,anchor=CENTER)
   
   
   button7= tk.Button(rootup,text="ACCOUNT TABLE",width=30,bg="light blue",fg="black",command=account)
   button7.place(relx=0.5,rely=0.725,anchor=CENTER)
   
      
   button8= tk.Button(rootup,text="REPORT TABLE",width=30,bg="light blue",fg="black",command=report)
   button8.place(relx=0.5,rely=0.8,anchor=CENTER)
   
   rootup.mainloop()   
def accident(ins_client):
    #print("Insert the Record into [ Accident-Table ] of the corresponding client\n")
 ac_id=str(random.randint(9,19999))
 ac_type=""
 ac_reason=""
    
 ac_clientid=ins_client#input("Enter the corresponding client_id\n")
 insert_query="""insert into Accident(Accident_id,Accident_type,Accident_reason,FK_client_id) values (%s,%s,%s,%s)"""
 records=[ac_id,ac_type,ac_reason,ac_clientid]
 cursor.execute(insert_query,records)
 mydb.commit()
     
def insert_values(client_id,f_name, l_name, gen, reff, ins_city1 ,ins_type_fn, ins_plan ,not_id, obj_id_fn, username , pas, rep_id_fn, premeium_fn, payment_id, amount_paid, insured_val, acc_id_fn, res_addr,branch_addr,obj_name_fn):
 root3=tk.Tk()
 
 width=root3.winfo_reqwidth()
 height=root3.winfo_reqheight()
 
 posright=int(root3.winfo_screenwidth()/2-width/2-100)
 posleft=int(root3.winfo_screenheight()/2-height/2)
 root3.geometry("400x150+{}+{}".format(posright,posleft))
 #root3.geometry("500X100")
 #root3.place(relx=0.5,rely=0.5)

 

 n_id=not_id
 n_type="Welcome Notice"
 n_descript="Start of Insurance Policy"
 n_date= str(date.today())
 insert_query="""insert into Notice (Notice_id,Notice_type,Descript,D_ate) values (%s, %s, %s, %s)"""
 records=[n_id,n_type,n_descript,n_date]
 cursor.execute(insert_query,records)
 mydb.commit()    
 ins_client=client_id#input("Enter Client-id\n")
        #ins_notid=input("Enter Notice-id\n")
 ins_fname=f_name#input("Enter FirstName of the client\n")
 ins_lname=l_name#input("Enter LastName of the client\n")
 if gen==1:
     ins_sex="Male"
 else:
     ins_sex="Female"
 
    
 pay_id= payment_id#input("Enter the payment_id\n")
 pay_date=str(date.today())
 pay_amount=amount_paid#input("Enter the premium amount paid by the client\n")
 pay_clientid=ins_client #input("Enter the respective client_id\n")
 insert_query="""insert into payment(Payment_id,Payment_date,Amount,FK_client_id)values(%s,%s,%s,%s)"""
 records=[pay_id,pay_date,pay_amount,pay_clientid]
 cursor.execute(insert_query,records)
 mydb.commit()

 ins_ref=reff#input("Enter the Referrer Agent name\n")
 ins_city=ins_city1#"Mysore" input("Enter the client's resident city\n")
 insert_query="""insert into Insured (Client_id,Notice_id,F_name,L_name,Sex,Contact_person,Address) values(%s, %s, %s, %s, %s, %s, %s)"""
 records=[ins_client,n_id,ins_fname,ins_lname,ins_sex,ins_ref,ins_city]
 cursor.execute(insert_query,records)
 mydb.commit()
 accident(ins_client)

 acc_id=acc_id_fn #input("Enter the Account_id of the client\n")
 acc_user=username#input("Enter the Username\n")
 acc_pass=pas#input("Enter the password\n")
 acc_role="Customer"#input("Enter the role of client with respect to Insurance Management\n")
 acc_client=ins_client # input("Enter the respective client_id\n")
 insert_query="""insert into _Account (Account_id,Username,Pswrd,User_Role,FK_client_id) values(%s, %s, %s, %s,%s)"""
 records=[acc_id,acc_user,acc_pass,acc_role,acc_client]
 cursor.execute(insert_query,records)
 mydb.commit()
 
 if ins_type_fn==1:
     
    
     
    # inu_des2=ins_plan
     insert_query="""insert into Insurance(Insurance_type,Description_ins,FK_client_id)values(%s,%s,%s)"""
     records=["Life Insurance L-"+ins_client,ins_plan,ins_client]
     cursor.execute(insert_query,records)
     mydb.commit()
    #input("Enter the generated Report_id\n")
     rep_date=str(date.today())
     #input("Enter the respective client_id\n")
     insert_query="""insert into Report(Report_id,Report_date,Report_type,FK_client_id)values(%s,%s,%s,%s)"""
     records=[rep_id_fn,rep_date,"Life Insurance Report",ins_client]
     cursor.execute(insert_query,records)
     mydb.commit()         
     
    
     obj_ins=str(date.today())
     #bj_clientid= #input("Enter the respective client-id\n")
     insert_query="""insert into Object (Object_id,Object_name,Object_type,Insured_value,Year_insurance,FKcli_id,FKpay_id) values (%s,%s,%s,%s,%s,%s,%s)"""
     records=[obj_id_fn,obj_name_fn,"Human",insured_val,obj_ins,ins_client,payment_id]
     cursor.execute(insert_query,records)
     mydb.commit()
        
 
    
 elif ins_type_fn==2:
    

    
     insert_query="""insert into Insurance(Insurance_type,Description_ins,FK_client_id)values(%s,%s,%s)"""
     records=["Vehicle Insurance V-"+ins_client,ins_plan,ins_client]
     cursor.execute(insert_query,records)
     mydb.commit()
     
     rep_date=str(date.today())
     #rep_clientid= #input("Enter the respective client_id\n")
     insert_query="""insert into Report(Report_id,Report_date,Report_type,FK_client_id)values(%s,%s,%s,%s)"""
     records=[rep_id_fn,rep_date,"Vehicle Insurance Report",ins_client ]
     cursor.execute(insert_query,records)
     mydb.commit()          
     #obj_id= #input("Enter the object_id\n")
     #obj_type=obj_typer#input("Enter the type of the object associated with the client\n")
     #obj_name=#input("Enter the name of the object\n")
     #obj_value= #input("Enter the total insured amount associated with the object\n")
     obj_ins=str(date.today())
     #obj_clientid= #input("Enter the respective client-id\n")
     
     insert_query="""insert into Object (Object_id,Object_name,Object_type,Insured_value,Year_insurance,FKcli_id,FKpay_id) values (%s,%s,%s,%s,%s,%s,%s)"""
     records=[obj_id_fn,obj_name_fn,"Vehicle",insured_val,obj_ins,ins_client,payment_id]
     cursor.execute(insert_query,records)
     mydb.commit()
        

 
 pol_id=str(random.randint(9,19999))#input("Enter the Policy_no\n")
 
 pol_branch=branch_addr#pol_brancharea + "," + pol_branchcity
 pol_premium=premeium_fn#input("Enter the premium value associated with the insurance policy\n")
 pol_client=ins_client
 insert_query="""insert into Policy(Policy_no,Policy_branch,Premeium_value,FK_client_id) values(%s,%s,%s,%s)"""
 records=[pol_id,pol_branch,pol_premium,pol_client]
 cursor.execute(insert_query,records)
 mydb.commit()
 
 address=res_addr#input("Enter the resident address of the client\n")
 insert_query="""insert into Address(Client_id,Address) values (%s,%s)"""
 records=[ins_client,address]
 cursor.execute(insert_query,records)
 mydb.commit()
 


 text=tk.Label(root3,text="Details Saved Successfully",fg="black")
 text.config(font=("Verdana",10))
 

 text.place(relx=0.5,rely=0.5,anchor=CENTER)
 
 submit=tk.Button(root3,text="OK",bg="light blue",fg="black",command=root3.destroy)
 submit.place(relx=0.4,rely=0.65)
 submit.config(height=1,width=10)
 root3.mainloop()

def update():
 rootsearch=tk.Tk()
 rootsearch.geometry("1920x1080")
 text1=tk.Label(rootsearch,text="Enter Client-id :",fg="black",font=12)
 text1.place(relx=0.04,rely=0.2)
 
 client=Entry(rootsearch,width=20,selectborderwidth=50,font="Arial")
 client.place(relx=0.225,rely=0.2)
 
 
 def uptt():
     cnt_id=str(client.get())
     clienter=cnt_id
     cursor.execute("""select Insured_value from Object where FKcli_id= %s""",(cnt_id,))     
     record=str(cursor.fetchall())
 
     if record=="[]":
         rootnotfound=tk.Tk()
         width=rootnotfound.winfo_reqwidth()
         height=rootnotfound.winfo_reqheight()
         
         #print(record)
         posright=int(rootnotfound.winfo_screenwidth()/2-width/2-100)
         posleft=int(rootnotfound.winfo_screenheight()/2-height/2)
         text2=tk.Label(rootnotfound,text="Record not found",fg="black")
         text2.config(font=("Verdana",12))
         text2.place(relx=0.5,rely=0.5,anchor=CENTER)
         rootnotfound.geometry("400x150+{}+{}".format(posright,posleft))
         rootnotfound.mainloop()    
     else:
         
         
         m=""
       
        
         cursor.execute("""select F_name,L_name from Insured where Client_id= %s""",(cnt_id,))     
         record1=cursor.fetchall()
         j=str(m)
         for i in record:
             if i.isdigit():
                 j=j+str(i)
         text7=tk.Label(rootsearch,text="First name :",fg="black")
         text7.config(font=("Verdana",12))
         text7.place(relx=0.04,rely=0.3)
         text8=tk.Label(rootsearch,text=record1[0][0],fg="black")
         text8.config(font=("Verdana",12)) 
         text8.place(relx=0.245,rely=0.3)
         
         
         text9=tk.Label(rootsearch,text="Last name :",fg="black")
         text9.config(font=("Verdana",12))
         text9.place(relx=0.04,rely=0.35)
         text10=tk.Label(rootsearch,text=record1[0][1],fg="black")
         text10.config(font=("Verdana",12)) 
         text10.place(relx=0.245,rely=0.35)
         
         
         
         
         
         text3=tk.Label(rootsearch,text="Insured Amount(Max) ",fg="black")
         text3.config(font=("Verdana",12))
         text3.place(relx=0.04,rely=0.4)
         text4=tk.Label(rootsearch,text=j,fg="black")
         text4.config(font=("Verdana",12)) 
         text4.place(relx=0.245,rely=0.4)
         text5=tk.Label(rootsearch,text="Enter Accident Type",fg="black",font=11)
         text5.place(relx=0.04,rely=0.45)
         ac_type=Entry(rootsearch,width=20,selectborderwidth=50,font="Arial")
         ac_type.place(relx=0.245,rely=0.45)
         text6=tk.Label(rootsearch,text="Enter Accident Reason",fg="black",font=11)
         text6.place(relx=0.04,rely=0.5)
         
         ac_rea=Entry(rootsearch,width=25,selectborderwidth=50,font="Arial")
         ac_rea.place(relx=0.245,rely=0.5)#0.25
         
         text7=tk.Label(rootsearch,text="Enter Accident Date(YYYY-MM-DD)" ,fg="black",font=11) 
         text7.place(relx=0.04,rely=0.55)
 
         ac_dat=tk.Entry(rootsearch,width=25,selectborderwidth=50,font="Arial")
         ac_dat.place(relx=0.245,rely=0.55)#0.35
         text11=tk.Label(rootsearch,text="Enter Accident Location" ,fg="black",font=11) 
         text11.place(relx=0.04,rely=0.6)
 
         ac_loct=tk.Entry(rootsearch,width=25,selectborderwidth=50,font="Arial")
         ac_loct.place(relx=0.245,rely=0.6)#0.35     
         text8=tk.Label(rootsearch,text="Enter Claim Amount" ,fg="black",font=11) 
         text8.place(relx=0.04,rely=0.65)
 
         ac_claim=tk.Entry(rootsearch,width=25,selectborderwidth=50,font="Arial")
         ac_claim.place(relx=0.245,rely=0.65)#0.35
         def getts():
              ac_ty=ac_type.get()
              ac_date=ac_dat.get()          #=input("Enter the date of Accident in YYYY-MM-DD format\n")
              ac_re=ac_rea.get() #=input("Enter the Accident Reason\n")
              ac_loc=ac_loct.get()#=input("Enter the Accident Location\n")
              ac_claimed=ac_claim.get()
              rootclaim=tk.Tk()
              width=rootclaim.winfo_reqwidth()
              height=rootclaim.winfo_reqheight()            
              posright=int(rootclaim.winfo_screenwidth()/2-width/2-100)
              posleft=int(rootclaim.winfo_screenheight()/2-height/2)
              rootclaim.geometry("400x150+{}+{}".format(posright,posleft))
             
             
              print(ac_ty)
              print(ac_date)

              print(ac_re)
              print(ac_loc)
              print(ac_claimed)
              updatter(ac_ty,ac_re,ac_date,ac_loc,ac_claimed,clienter)
              
              texter=tk.Label(rootclaim,text="Database updated successfully\nAmount of Rs "+ac_claimed+" claimed",fg="black")
              texter.config(font=("Verdana",10))
              texter.place(relx=0.5,rely=0.5,anchor=CENTER)
             
            
              submit=tk.Button(rootclaim,text="OK",bg="light blue",fg="black",command=rootclaim.destroy)
              submit.place(relx=0.4,rely=0.65)
              submit.config(height=1,width=10)
              rootclaim.mainloop()    
             
         
         #rootsearch.mainloop()    
         claim=tk.Button(rootsearch,text="CLAIM",command=getts,bg="light blue")
         claim.place(relx=0.4,rely=0.75)
         claim.configure(width=25,height=1)
         rootsearch.mainloop()           
 
 search=tk.Button(rootsearch,text="SEARCH",command=uptt)
 search.place(relx=0.4,rely=0.2)
 search.configure(width=15,height=1)           
 #rootsearch.mainloop()
 
    
              
 
 
# rootsearch.mainloop()
     
     
     

  

def insertwindow():
 
 root2=tk.Toplevel()
 #oot2.attributes("-fullscreen",True)
 root2.geometry("1920x1080")
 var =IntVar()
 #var.set(1)
 var2=IntVar()
 #var2.set(1)

 text1=tk.Label(root2,text="Client-id :",fg="black",font=11)
 text1.place(relx=0.04,rely=0.1)
 
 client=Entry(root2,width=20,selectborderwidth=50,font="Arial")
 client.place(relx=0.2,rely=0.1)
 
 
 
 #0.15
 text2=tk.Label(root2,text="First name",fg="black",font=11)
 text2.place(relx=0.04,rely=0.2)
 F_name=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 F_name.place(relx=0.2,rely=0.2)#0.25

 
 
 text3=tk.Label(root2,text="Last name",fg="black",font=11)
 text3.place(relx=0.04,rely=0.3)
 
 L_name=tk.Entry(root2,width=25,selectborderwidth=50,font="Arial")
 L_name.place(relx=0.2,rely=0.3)#0.35

 
 
 text4=tk.Label(root2,text="Gender",fg="black",font=11)
 text4.place(relx=0.04,rely=0.4)
 
 text5=tk.Label(root2,text="Referral Agent Name",fg="black",font="Arial")
 text5.place(relx=0.04,rely=0.45)
 
 contact_person=tk.Entry(root2,width=25,selectborderwidth=50,font="Arial")
 contact_person.place(relx=0.2,rely=0.45)#0.45
 
 def sel():
   gender=var.get()
   print(gender)
    
   
   
 male=tk.Radiobutton(root2,text="Male",variable=var,value=1,font=12,command=sel)#,command=gender())
 male.place(relx=0.2,rely=0.4)

 female=tk.Radiobutton(root2,text="Female",variable=var,value=2,font=12,command=sel)#,command=gender())
 female.place(relx=0.25,rely=0.4)
 
 text6=tk.Label(root2,text="Insurance Type",fg="black",font=11)
 text6.place(relx=0.04,rely=0.5)
 
 Lifeins=tk.Radiobutton(root2,text="Life Insurance",variable=var2,value=1,font=12)#,command=init(5))
 Lifeins.place(relx=0.2,rely=0.5)
 
 Healthins=tk.Radiobutton(root2,text="Vehicle Insurance",variable=var2,value=2,font=12)#,command=init(7))
 Healthins.place(relx=0.3,rely=0.5)
 
 text7=tk.Label(root2,text="Insurance Plan",fg="black",font="Arial")
 text7.place(relx=0.04,rely=0.6)
 
 plan=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 plan.place(relx=0.2,rely=0.6)#0.45
 
 
 
 text18=tk.Label(root2,text="Notice-id",fg="black",font=11)
 text18.place(relx=0.04,rely=0.675)
 
 notice_id=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 notice_id.place(relx=0.2,rely=0.675)#0.45


 text19=tk.Label(root2,text="Object-id",fg="black",font=11)
 text19.place(relx=0.04,rely=0.75)

 object_id=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 object_id.place(relx=0.2,rely=0.75)#0.45
 

 text20=tk.Label(root2,text="Account-id",fg="black",font=11)
 text20.place(relx=0.5,rely=0.75)
 
 acc_id=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 acc_id.place(relx=0.6,rely=0.75)#0.45

 
 
 text8=tk.Label(root2,text="Set user name",fg="black",font=11)
 text8.place(relx=0.5,rely=0.1)
 
 user=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 user.place(relx=0.6,rely=0.1)#0.45
 
 text9=tk.Label(root2,text="Set Password",fg="black",font=11)
 text9.place(relx=0.5,rely=0.2)
 
 pas=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 pas.place(relx=0.6,rely=0.2)
 
 
 text10=tk.Label(root2,text="Report id",fg="black",font=11)
 text10.place(relx=0.5,rely=0.3)
 
  
 rep_id=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 rep_id.place(relx=0.6,rely=0.3)
 
 
 
 text11=tk.Label(root2,text="Premeium value",fg="black",font=11)
 text11.place(relx=0.5,rely=0.4)

 prem=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 prem.place(relx=0.6,rely=0.4)
 
 text12=tk.Label(root2,text="Payment id",fg="black",font=11)
 text12.place(relx=0.5,rely=0.5)
 
 pay_id=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 pay_id.place(relx=0.6,rely=0.5)

 text14=tk.Label(root2,text="Amount Paid",fg="black",font=11)
 text14.place(relx=0.5,rely=0.6)
 
 amount=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 amount.place(relx=0.6,rely=0.6)

 
 text15=tk.Label(root2,text="Insured Value",fg="black",font=11)
 text15.place(relx=0.5,rely=0.65)
 
 ins_value=Entry(root2,width=25,selectborderwidth=50,font="Arial")
 ins_value.place(relx=0.6,rely=0.65)


 text16=tk.Label(root2,text="Resident Address",fg="black",font=11)
 text16.place(relx=0.8,rely=0.1)

 res_ad=Entry(root2,width=20,selectborderwidth=50,font="Arial")
 res_ad.place(relx=0.8,rely=0.15)
 
 text16=tk.Label(root2,text="Branch",fg="black",font=11)
 text16.place(relx=0.8,rely=0.210)
 
 branch=Entry(root2,width=20,selectborderwidth=50,font="Arial")
 branch.place(relx=0.8,rely=0.25)
 
   
 text21=tk.Label(root2,text="Object Name",fg="black",font=11)
 text21.place(relx=0.8,rely=0.3)
 
 text22=tk.Label(root2,text="Resident city",fg="black",font=11)
 text22.place(relx=0.8,rely=0.425)
 city1=Entry(root2,width=20,selectborderwidth=50,font="Arial")
 city1.place(relx=0.8,rely=0.475)
 obj_name=Entry(root2,width=20,selectborderwidth=50,font="Arial")
 obj_name.place(relx=0.8,rely=0.35)
 def gett():
   client_id=client.get()   
   
   f_name=F_name.get()
   
   l_name=L_name.get()    
   
   contact=contact_person.get()  
   
   amount_paid=amount.get()
   
   ins_city1=city1.get()
   gen=int(var.get())  
   ins_type=int(var2.get())
   branch_addr=branch.get()
   res_addr=res_ad.get() 
   insured_val=ins_value.get()
   payment_id=pay_id.get() 
   premeium_fn=prem.get()
   rep_id_fn=rep_id.get()  
   password=pas.get()
   username=user.get()
   acc_id_fn=acc_id.get()  
   obj_id_fn=object_id.get()
   not_id=notice_id.get()
   plan_insurance=plan.get() 
   obj_name_fn=obj_name.get()
   insert_values(client_id,f_name, l_name, gen,  contact, ins_city1 ,ins_type,plan_insurance ,not_id, obj_id_fn, username , password, rep_id_fn, premeium_fn, payment_id, amount_paid, insured_val, acc_id_fn, res_addr,branch_addr,obj_name_fn)
 submit=tk.Button(root2,text="SUBMIT",bg="light blue",width=35,fg="black",command=gett)#,command=insert_values(client_id,f_name, l_name, var.get(),  contact, ins_city1 ,var2.get(),plan_insurance ,notice_id.get(), obj_id_fn, username , password, rep_id_fn, premeium_fn, payment_id, amount_paid, insured_val, acc_id_fn, res_addr,branch_addr,obj_name_fn))
 submit.place(relx=0.5,rely=0.85,anchor=CENTER)
 tk.mainloop()   
def startscreen():
 root1=tk.Tk()
 root1.geometry("1920x1080")
 #root1.attributes("-fullscreen",True)
 #root1.configure(bg="blue")
 root1.title("INSURANCE MANAGEMENT SYSTEM")
 w=tk.Label(root1,text="WELCOME TO INSURANCE MANAGEMENT SYSTEM",fg="black",font=30)
 w.config(font="Verdana")
 w.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

 button1= tk.Button(text="INSERT",bg="light blue",width=25,fg="black",command=insertwindow)
 button1.place(relx=0.5,rely=0.35,anchor=CENTER)#,command=insertwindow)

 button2=tk.Button(text="SELECT",bg="light blue",width=25,fg="black",command=select)
 button2.place(relx=0.5,rely=0.5,anchor=CENTER)

 button3=tk.Button(text="DELETE",bg="light blue",width=25,fg="black",command=delete)
 button3.place(relx=0.5,rely=0.65,anchor=CENTER)

 button4=tk.Button(text="UPDATE",bg="light blue",width=25,fg="black",command=update)
 button4.place(relx=0.5,rely=0.8,anchor=CENTER)
 tk.mainloop() 
""" button5=tk.Button(text="QUIT",bg="white",width=25,fg="black",command=close_window(root1))
 button5.place(relx=0.5,rely=0.75,anchor=CENTER)"""
startscreen()


