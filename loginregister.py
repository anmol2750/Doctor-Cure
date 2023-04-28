from tkinter import *
import os
from PIL import ImageTk
from tkinter import *
import tkinter.ttk as tt
import sqlite3
from tkinter import ttk,messagebox
import datetime as dt
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
from fpdf import FPDF
import regex as re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#---------------------------------------------------------------------Database--------------------------------------------------------------------------------##
conn=sqlite3.connect('my_database.db')
c=conn.cursor()
def create():
    c.execute("CREATE TABLE IF NOT EXISTS credentials(fname TEXT,lname TEXT, contact_no TEXT UNIQUE,email_id TEXT UNIQUE,question TEXT,answer TEXT,password TEXT,confirm_password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS medicine_table(name TEXT,date TEXT,phn_no TEXT,medicine TEXT,dosage TEXT,timings TEXT,days TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS record(name TEXT,weight real,height TEXT,date TEXT,phn_no INT,bp TEXT,ong_disease TEXT,add_disease TEXT,precaution TEXT,bmi TEXT,age INT)")
    conn.commit()
create()


##-----------------------------------------------------------------check validity of phn_no-------------------------------------------------------------------##
 
def validNumber(phone_number):
    return all([x.isdigit() for x in phone_number.split("-")])


##----------------------------------------------------------------Menu bar-------------------------------------------------------------------------------------##

def aboutus(t):
        messagebox.showinfo("About Doctor Cure ","This application helps a doctor to Manage Patient History,Diet and Medicine which doctor needs to diagnose patient easily.\n\nCreated By Binary Beast using Python",parent=t)





##-------------------------------------------------------------Saving data in database(Credentials)-------------------------------------------------------------##


def savedata1():
    global email
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    c.execute("SELECT * FROM credentials")
    r=c.fetchall()
    a=0


    ##-----------------------------------------all feilds are required--------------------------------------------##
    
    if var_fname.get()=="" or email.get()=="" or option.get()=="Select"or var_answer.get()==""or password.get()==""or var_cpass.get()==""or var_con.get()=="":
        messagebox.showerror("Error","All Fields Are Required",parent=root)

    ##----------------------------------------matching password----------------------------------------------------##

        
    elif password.get()!=var_cpass.get():
        messagebox.showerror("Error","Password and Confirm Password should be same",parent=root)

    ##----------------------------------------length of password----------------------------------------------------##
        
    elif (len(password.get())<8):
        messagebox.showerror("Error","Password must be of 8 characters",parent=root)

    ##-------------------------------------------validity of password----------------------------------------------##

    
    elif not re.search("[a-z]", password.get()) or not re.search("[A-Z]", password.get()) or not re.search("[0-9]", password.get()) or not re.search("[_@$]",password.get()) or re.search("\s", password.get()):
        messagebox.showerror("Error","Password must have capital letter, number and special character",parent=root)


    ##-----------------------------------tick on terms and conditions-------------------------------------------------##
    
        
    elif var_chk.get()==0:
        messagebox.showerror("Error","Please agree the terms and conditions",parent=root)

    ##-----------------------------------------validity of email----------------------------------------------------##

        
    elif not re.search(regex,email.get()):
        messagebox.showerror("Error","Please Enter the valid Emailid ",parent=root)

    ##------------------------------------validity of phn_no-----------------------------------------------------##

        
    elif not validNumber(var_con.get()):
        messagebox.showerror("Error","Please Enter the valid Contact no ",parent=root)



    ##---------------------------------------------validity of new_pass--------------------------------------------##


    #elif not re.search("[a-z]", pass1.get()) or not re.search("[A-Z]", pass1.get()) or not re.search("[0-9]", pass1.get()) or not re.search("[_@$]",pass1.get()) or re.search("\s", pass1.get()):
        #messagebox.showerror("Error","Password must have capital letter, number and special character",parent=root2)

        
    
    ##--------------------------------------------checking details from database-------------------------------------##
    else:
        
        for i in r:
          if i[3]==email.get() or i[6]==password.get() or i[2]==contact_no.get():
            a=1
            messagebox.showerror("Warning","User already exist",parent=root)
            root.destroy()

    ## ---------------------------------------------if not there then insert-----------------------------------------------##

        
        if a==0:
          c.execute('INSERT INTO credentials(fname,lname,contact_no,email_id,question,answer,password,confirm_password) VALUES(?,?,?,?,?,?,?,?)',(var_fname.get(),var_lname.get(),var_con.get(),email.get(),cmb_question.get(),var_answer.get(),password.get(),var_cpass.get()))
          conn.commit()
          
        
        
        
          messagebox.showinfo("Success","Registration Successful",parent=root)
          var_fname.set("")
          var_lname.set("") 
          email.set("")
          var_con.set("")
          option.set("")
          var_answer.set("")
          password.set("")
          var_cpass.set("")
      

##--------------------------------------------------------------------------------Login Success---------------------------------------------------------------------##



def login_success():
  global email1,password
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  c.execute("SELECT * FROM credentials")
  r=c.fetchall()
  check=0
  for i in r:
    if i[3]==email1.get() and i[6]==password.get():
      check=1
      screen2.destroy()
      session()
  if check!=1:
    messagebox.showerror("Error"," User not found",parent=screen2)
    email1.set("")
    password.set("")



##------------------------------------------------------------------------------------------------------------------------------------------------------------------##      



def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()



def del_mainscreen():
  screen.destroy()

def del_root():
  root.destroy()

def del_screen2():
  screen2.destroy()
  screen.deiconify()

def del_screen8():
  screen8.destroy()


##------------------------------------------------------------------------patient history-------------------------------------------------------------------------------



def delete_win1():
  win1.destroy()
def delete_win2():
  win2.destroy()
def delete_win3():
  win3.destroy()
def delete_win4():
  win4.destroy()
def delete_win1():
  win1.destroy()
def delete_win2():
  win2.destroy()
def delete_win3():
  win3.destroy()
def delete_win4():
  win4.destroy()

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'


class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

        
def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")
    
    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)
        
            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")
    
    entry.placeholder_state = state

    return state

def add_patient():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  global win2
  win2=Toplevel(win1)
  win2.title("NEW PATIENT")
  win2.config(bg="#bbded6")
  x, y = win2.winfo_screenwidth(), win2.winfo_screenheight()
  win2.geometry("%dx%d+0+0" % (x, y))
  Label(win2, text = "ENTER DETAILS",font=("times new roman",35,),bg="#bbded6",fg="black").place(x=480,y=10)
  
  #=====var name===============
  global P_name
  global P_wght,P_height,P_date,p_no,bload_pressure,P_BMI,patient_age

  P_name      =StringVar()
  P_wght      =StringVar() 
  P_height    =StringVar()
  P_date      =StringVar()
  p_no        =StringVar()
  bload_pressure=StringVar()
  P_BMI       =StringVar()
  patient_age =StringVar()
  #=============================
  
  Label(win2, text = "PATIENT NAME *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=20,y=150, height=40,width=130)
  patient_name_entry1 = Entry(win2, textvariable = P_name)
  add_placeholder_to(patient_name_entry1, 'Enter Patient Name...')
  

  patient_name_entry1.place(x=180,y=150, height=40,width=250)
  patient_name_entry1.configure(background="white")
  patient_name_entry1.configure(font="-family {Palatino Linotype} -size 15")
  
  
  Label(win2, text = "WEIGHT(kg) *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=30,y=230, height=40,width=100)
  weight_entry1 = Entry(win2, textvariable = P_wght)
  add_placeholder_to(weight_entry1, 'Enter weight in kg')
  weight_entry1.place(x=180,y=230, height=40,width=250)
  weight_entry1.configure(background="white")
  weight_entry1.configure(font="-family {Palatino Linotype} -size 15")
  
  Label(win2, text = "HEIGHT(m) *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=30,y=310, height=40,width=100)
  HEIGHT_entry1 = Entry(win2, textvariable = P_height)
  add_placeholder_to(HEIGHT_entry1, 'Enter height in metre')
  HEIGHT_entry1.place(x=180,y=310, height=40,width=250)
  HEIGHT_entry1.configure(background="white")
  HEIGHT_entry1.configure(font="-family {Palatino Linotype} -size 15")


  
  Label(win2, text = "DATE *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=20,y=400, height=40,width=150)
  DATE_entry1 = Entry(win2, textvariable =P_date)
  add_placeholder_to(DATE_entry1, 'dd/mm/yy')
  DATE_entry1.place(x=180,y=400, height=40,width=250)
  DATE_entry1.configure(background="white")
  DATE_entry1.configure(font="-family {Palatino Linotype} -size 15")

  
  Label(win2, text = "PHONE NO *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=30,y=490, height=40,width=100)
  PHONE_entry1 = Entry(win2,textvariable=p_no)
  add_placeholder_to(PHONE_entry1, 'xxxxxxxxxx')
  PHONE_entry1.place(x=180,y=490, height=40,width=250)
  PHONE_entry1.configure(background="white")
  PHONE_entry1.configure(disabledforeground="#a3a3a3")
  PHONE_entry1.configure(font="-family {Palatino Linotype} -size 15")
 
 

  Label(win2, text = "BP *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=470,y=490, height=40,width=100)
  global BP_entry
  BP_entry=Entry(win2,textvariable=bload_pressure)
  add_placeholder_to(BP_entry, 'Eg 80-120')
  BP_entry.place(x=660,y=490,height=40,width=250)
  BP_entry.configure(background="white")
  BP_entry.configure(font="-family {Palatino Linotype} -size 15")
 

  Label(win2, text = "PROBLEM *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=450,y=150, height=40,width=200)
  global ONGOING_DISEASE
  ONGOING_DISEASE=Text(win2,height=4,width=25)
  ONGOING_DISEASE.place(x=660,y=150)
  ONGOING_DISEASE.configure(background="white")
  ONGOING_DISEASE.configure(font="-family {Palatino Linotype} -size 15")
 

  Label(win2, text = "DISEASE (if any)",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=457,y=300, height=40,width=200)
  global ADDITIONAL_DISEASE
  ADDITIONAL_DISEASE=Text(win2,height=5,width=25)
  ADDITIONAL_DISEASE.place(x=660,y=300)
  ADDITIONAL_DISEASE.configure(background="white")
  ADDITIONAL_DISEASE.configure(font="-family {Palatino Linotype} -size 15")
 

  Label(win2, text = "PRECAUTIONS",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=930,y=150, height=40,width=150)
  global PRECAUTION_entry
  PRECAUTION_entry=Text(win2,height=4,width=25)
  PRECAUTION_entry.place(x=1100,y=150)
  PRECAUTION_entry.configure(background="white")
  PRECAUTION_entry.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_entry.configure(foreground="#000000")

  Label(win2, text = "Age *",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=930,y=300, height=40,width=100)
  global age_entry
  age_entry=Entry(win2,textvariable=patient_age)
  add_placeholder_to(age_entry,'Enter patient age')
  age_entry.place(x=1100,y=300,height=40,width=250)
  age_entry.configure(background="white")
  age_entry.configure(font="-family {Palatino Linotype} -size 15")
  
  Label(win2, text = "BMI",bg="#bbded6",fg="black",font=("Helvetica",12)).place(x=925,y=400, height=40,width=100)

  BMI_entry=Entry(win2,textvariable=P_BMI)
  BMI_entry.place(x=1100,y=400,height=40,width=250)
  BMI_entry.configure(background="white")
  BMI_entry.configure(font="-family {Palatino Linotype} -size 15")
  BMI_entry.configure(foreground="#000000")
  
  add=HoverButton(win2,text="ADD PATIENT",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",15),command=savedata).place(x=400,y=590)
  n_back=HoverButton(win2,text="BACK",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",15),command=delete_win2).place(x=700,y=590)
  HoverButton(win2,text="CALCULATE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="1",width="12",font=("times new roman",15),command=bmi).place(x=1100,y=450)
  
win2=None
P_name=None
P_wght=None
P_height=None
P_date=None
p_no=None
bload_pressure=None
P_BMI=None
BP_entry=None
ONGOING_DISEASE=None
ADDITIONAL_DISEASE=None
PRECAUTION_entry=None
def bmi():
  if P_wght.get()=="" or P_height.get()=="":
    messagebox.showerror("Enter height and date",parent=win2)
  else:
    b=round(float(P_wght.get())/(float(P_height.get())*float(P_height.get())))
    P_BMI.set(str(b))
    

def savedata():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  #===query=====
  c.execute("SELECT * FROM record")
  #=============
  r=c.fetchall()
  
  if P_name.get()=="" or P_date.get()=="" or P_wght.get()==""or P_height.get()==""or p_no.get()==""or bload_pressure.get()=="" or ONGOING_DISEASE.get("1.0","end-1c")=="":
    messagebox.showerror("Error","Fill necessary Fields",parent=win2)
  elif len(p_no.get())!=10 :
    messagebox.showerror("warning","enter correct no",parent=win2)
    p_no.set("")
  else:
    a=0
    for i in r:
      if i[4]==p_no.get() and i[0]==P_name.get():
        a=1
        messagebox.showerror("warning","already exists",parent=win2)
        win2.destroy()
    if a==0: 
      try:
        d=dt.datetime.strptime(P_date.get(),"%d/%m/%y")
        c.execute('INSERT INTO record(name,weight,height,date,phn_no,bp,ong_disease,add_disease,precaution,bmi,age) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(P_name.get(),P_wght.get(),P_height.get(),P_date.get(),p_no.get(),bload_pressure.get(),ONGOING_DISEASE.get("1.0","end-1c"),ADDITIONAL_DISEASE.get("1.0","end-1c"),PRECAUTION_entry.get("1.0","end-1c"),P_BMI.get(),patient_age.get()))
        conn.commit()
        messagebox.showinfo("Success","Patient Added Successfully",parent=win2)
        win2.destroy()
        win1.deiconify()
      except:
        messagebox.showerror("warning","enter date in correct format",parent=win2)
  

def inner_add():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  updated_ong=ONGOING_DISEASE_update.get("1.0","end-1c")
  updated_additional=ADDITIONAL_DISEASE_update.get("1.0","end-1c")
  updated_prec=PRECAUTION_update.get("1.0","end-1c")
  no=p_no_display.get()
  date=u4.get()  
  if u4.get()=="":
    messagebox.showerror("warning","enter date",parent=win5)
  elif u4.get()==D_display.get():
    messagebox.showerror("warning","patient already exist for current date go to update menu",parent=win5)
  elif u7.get()=="":
    messagebox.showerror("warning","calculate the bmi",parent=win5)
  elif ONGOING_DISEASE_update.get("1.0","end-1c")=="":
    messagebox.showerror("warning","fill the fields",parent=win5)

  else:
    try:
      d=dt.datetime.strptime(u4.get(),"%d/%m/%y")
      #====query====
      c.execute('INSERT INTO record(name,weight,height,date,phn_no,bp,ong_disease,add_disease,precaution,bmi,age)VALUES(?,?,?,?,?,?,?,?,?,?,?)',(u1.get(),u2.get(),u3.get(),u4.get(),u5.get(),u6.get(),updated_ong,updated_additional,updated_prec,u7.get(),u8.get())) 
      conn.commit()
      #====query====
      messagebox.showinfo("Success","Added Successfully",parent=win5)
      win5.destroy()
      win4.destroy()
      win3.destroy()
    except:
      messagebox.showerror("warning","enter date in correct format",parent=win5)
  
def mod_bmi():
  if u2.get()=="" or u3.get()=="":
    messagebox.showerror("Enter height and weight",parent=win2)
  else:
    b=round(float(u2.get())/(float(u3.get())*float(u3.get())))
    u7.set(str(b))     
def modify():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  global win5
  
  global u1,u2,u3,u4,u5,u6,u7,u8

  u1=StringVar()
  u2=StringVar()
  u3=StringVar()
  u4=StringVar()
  u5=StringVar()
  u6=StringVar()
  u7=StringVar()
  u8=StringVar()
  u1.set(P_display.get())
  u2.set(W_display.get())
  u3.set(H_display.get())
  u5.set(p_no_display.get())
  u6.set(bload_pressure_display.get())
  u8.set(age_display.get())
  win5 = Toplevel(win4)
  win5.config(bg='#d6e0f0')
  win5.title("PATIENT RECORD")
  x, y = win5.winfo_screenwidth(), win5.winfo_screenheight()
  win5.geometry("%dx%d+0+0" % (x, y))
  Label(win5, text = "PATIENT NAME",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=50,y=30, height=40,width=150)
  patient_update = Entry(win5,textvariable=u1,justify='center',state='readonly')
  patient_update.place(x=30,y=80, height=40,width=200)
  patient_update.configure(background="white")
  patient_update.configure(font="-family {Palatino Linotype} -size 15")
  patient_update.configure(foreground="#000000")
  

  Label(win5, text = "WEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=310,y=30, height=40,width=100)
  weight_update = Entry(win5,textvariable =u2,justify='center')
  weight_update.place(x=260,y=80, height=40,width=200)
  weight_update.configure(background="white")
  weight_update.configure(font="-family {Palatino Linotype} -size 15")
  weight_update.configure(foreground="#000000")


  Label(win5, text = "HEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=585,y=30, height=40,width=100)
  HEIGHT_update = Entry(win5,textvariable =u3,justify='center')
  HEIGHT_update.place(x=540,y=80, height=40,width=200)
  HEIGHT_update.configure(background="white")
  HEIGHT_update.configure(font="-family {Palatino Linotype} -size 15")
  HEIGHT_update.configure(foreground="#000000")
  
 
  Label(win5, text = "DATE",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1060,y=30, height=40,width=150)
  DATE_update = Entry(win5,textvariable =u4)
  add_placeholder_to(DATE_update, 'dd/mm/yy')
  DATE_update.place(x=1030,y=80, height=40,width=200)
  DATE_update.configure(background="white")
  DATE_update.configure(font="-family {Palatino Linotype} -size 15")
  DATE_update.configure(foreground="#000000")
  

  Label(win5, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=150, height=40,width=100)
  PHONE_update = Entry(win5,textvariable=u5,justify='center',state='readonly')
  PHONE_update.place(x=1030,y=200, height=40,width=200)
  PHONE_update.configure(background="white")
  PHONE_update.configure(font="-family {Palatino Linotype} -size 15")
  PHONE_update.configure(foreground="#000000")
  
  Label(win5, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=550, height=40,width=100)
  BP_update=Entry(win5,textvariable=u6,justify='center')
  BP_update.place(x=1030,y=600,height=40,width=200)
  BP_update.configure(background="white")
  BP_update.configure(font="-family {Palatino Linotype} -size 15")
  BP_update.configure(foreground="#000000")
  
  

  Label(win5, text = "PROBLEM *",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=190,y=200, height=40,width=200)
  global ONGOING_DISEASE_update
  ONGOING_DISEASE_update=Text(win5,height=8,width=32)
  ONGOING_DISEASE_update.place(x=150,y=250)
  ONGOING_DISEASE_update.configure(background="white")
  ONGOING_DISEASE_update.configure(font="-family {Palatino Linotype} -size 15")
  ONGOING_DISEASE_update.configure(foreground="#000000")
 

  Label(win5, text = "DISEASE (if any)",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=550,y=200, height=40,width=200)
  global ADDITIONAL_DISEASE_update
  ADDITIONAL_DISEASE_update=Text(win5,height=8,width=32)
  ADDITIONAL_DISEASE_update.place(x=530,y=250)
  ADDITIONAL_DISEASE_update.configure(background="white")
  ADDITIONAL_DISEASE_update.configure(font="-family {Palatino Linotype} -size 15")
  ADDITIONAL_DISEASE_update.configure(foreground="#000000")
 

  Label(win5, text = "PRECAUTIONS",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=250, height=40,width=120)
  global PRECAUTION_update
  PRECAUTION_update=Text(win5,height=5,width=20)
  PRECAUTION_update.place(x=1030,y=300)
  PRECAUTION_update.configure(background="white")
  PRECAUTION_update.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_update.configure(foreground="#000000")


  Label(win5, text = "Age *",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=815,y=30, height=40,width=100)
  global age_update
  age_update=Entry(win5,textvariable=u8,justify='center')
  age_update.place(x=770,y=80,height=40,width=200)
  age_update.configure(background="white")
  age_update.configure(font="-family {Palatino Linotype} -size 15")

  Label(win5, text = "BMI",bg="#d6e0f0",fg="black",font=("Helvetica",12)).place(x=1080,y=450, height=40,width=100)
  BMI_update=Entry(win5,textvariable=u7,justify='center')
  BMI_update.place(x=1030,y=500,height=40,width=200)
  BMI_update.configure(background="white")
  BMI_update.configure(font="-family {Palatino Linotype} -size 15")
  BMI_update.configure(foreground="#000000")
  
  HoverButton(win5,text="ADD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="20",font=("times new roman",13),command=inner_add).place(x=400,y=570)
  HoverButton(win5,text="CALCULATE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="1",width="12",font=("times new roman",13),command=mod_bmi).place(x=1230,y=504)
  
win5=None
u1=None
u2=None
u3=None
u4=None
u5=None
u6=None
u7=None
u8=None
ONGOING_DISEASE_update=None
ADDITIONAL_DISEASE_update=None
PRECAUTION_update=None

def update_prev_comm():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  updated_prev_ong=ONGOING_DISEASE_update_prev.get("1.0","end-1c")
  updated_prev_additional=ADDITIONAL_DISEASE_update_prev.get("1.0","end-1c")
  updated_prev_prec=PRECAUTION_update_prev.get("1.0","end-1c")
  #===query====
  c.execute("UPDATE record SET ong_disease=?,add_disease=?,precaution=?,bp=? WHERE name=? and date=? and phn_no=?",(updated_prev_ong,updated_prev_additional,updated_prev_prec,bload_pressure_update_prev.get(),P_update_prev.get(),D_update_prev.get(),p_no_update_prev.get()))
  conn.commit()
  #=============
  messagebox.showinfo("Success","updated successully",parent=win10)
  win10.destroy()
  win4.destroy()
  

def update_prev():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  global win10
  win10 = Toplevel(win4)
  win10.config(bg='#d6e0f0')
  win10.title("PATIENT RECORD")
  x, y = win10.winfo_screenwidth(), win10.winfo_screenheight()
  win10.geometry("%dx%d+0+0" % (x, y))
  global P_update_prev,W_update_prev,H_update_prev,D_update_prev,p_no_update_prev,bload_pressure_update_prev,P_BMI_update_prev
  global ONGOING_DISEASE_update_prev,ADDITIONAL_DISEASE_update_prev,PRECAUTION_update_prev,age_field_update
  P_update_prev=StringVar()
  W_update_prev=StringVar()
  H_update_prev=StringVar()
  D_update_prev=StringVar()
  p_no_update_prev=StringVar()
  bload_pressure_update_prev=StringVar()
  P_BMI_update_prev=StringVar()
  age_field_update=StringVar()
  P_update_prev.set(P_display.get())
  W_update_prev.set(W_display.get())
  H_update_prev.set(H_display.get())
  p_no_update_prev.set(p_no_display.get())
  bload_pressure_update_prev.set(bload_pressure_display.get())
  P_BMI_update_prev.set(P_BMI_display.get())
  D_update_prev.set(D_display.get())
  age_field_update.set(age_display.get())

  Label(win10, text = "PATIENT NAME",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=300,y=30, height=40,width=150)
  patient_update_prev = Entry(win10,textvariable=P_update_prev,justify='center',state='readonly')
  patient_update_prev.place(x=270,y=80, height=40,width=200)
  patient_update_prev.configure(background="white")
  patient_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  patient_update_prev.configure(foreground="#000000")
  

  Label(win10, text = "WEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=250, height=40,width=100)
  weight_update_prev = Entry(win10,textvariable =W_update_prev,justify='center',state='readonly')
  weight_update_prev.place(x=1100,y=300, height=40,width=200)
  weight_update_prev.configure(background="white")
  weight_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  weight_update_prev.configure(foreground="#000000")


  Label(win10, text = "HEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=350, height=40,width=100)
  HEIGHT_update_prev = Entry(win10,textvariable =H_update_prev,justify='center',state='readonly')
  HEIGHT_update_prev.place(x=1100,y=400, height=40,width=200)
  HEIGHT_update_prev.configure(background="white")
  HEIGHT_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  HEIGHT_update_prev.configure(foreground="#000000")
  
 
  Label(win10, text = "DATE",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1140,y=30, height=40,width=110)
  DATE_update_prev = Entry(win10,textvariable =D_update_prev,justify='center',state='readonly')
  DATE_update_prev.place(x=1100,y=80, height=40,width=200)
  DATE_update_prev.configure(background="white")
  DATE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  DATE_update_prev.configure(foreground="#000000")
  

  Label(win10, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=150, height=40,width=110)
  PHONE_update_prev = Entry(win10,textvariable=p_no_update_prev,justify='center',state='readonly')
  PHONE_update_prev.place(x=1100,y=200, height=40,width=200)
  PHONE_update_prev.configure(background="white")
  PHONE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  PHONE_update_prev.configure(foreground="#000000")
  
  Label(win10, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=550, height=40,width=100)
  BP_update_prev=Entry(win10,justify='center',textvariable=bload_pressure_update_prev)
  BP_update_prev.place(x=1100,y=600,height=40,width=200)
  BP_update_prev.configure(background="white")
  BP_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  BP_update_prev.configure(foreground="#000000")


  Label(win10, text = "Age",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=715,y=30, height=40,width=100)
  global age_display_entry
  age_update_prev=Entry(win10,textvariable=age_field_update,justify='center',state='readonly')
  age_update_prev.place(x=670,y=80,height=40,width=200)
  age_update_prev.configure(background="white")
  age_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  

  Label(win10, text = "PROBLEM *",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=80,y=150, height=40,width=350)
  ONGOING_DISEASE_update_prev=Text(win10,height=12,width=32)
  ONGOING_DISEASE_update_prev.place(x=80,y=200)
  ONGOING_DISEASE_update_prev.configure(background="white")
  ONGOING_DISEASE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  ONGOING_DISEASE_update_prev.configure(foreground="#000000")
 

  Label(win10, text = "DISEASE (if any)",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=390,y=150, height=40,width=330)
  ADDITIONAL_DISEASE_update_prev=Text(win10,height=12,width=32)
  ADDITIONAL_DISEASE_update_prev.place(x=390,y=200)
  ADDITIONAL_DISEASE_update_prev.configure(background="white")
  ADDITIONAL_DISEASE_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  ADDITIONAL_DISEASE_update_prev.configure(foreground="#000000")
 

  Label(win10, text = "PRECAUTIONS",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=695,y=150, height=40,width=330)
  PRECAUTION_update_prev=Text(win10,height=12,width=32)
  PRECAUTION_update_prev.place(x=700,y=200)
  PRECAUTION_update_prev.configure(background="white")
  PRECAUTION_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_update_prev.configure(foreground="#000000")
  

  Label(win10, text = "BMI",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=450, height=40,width=100)
  BMI_update_prev=Entry(win10,state='readonly',justify='center',textvariable=P_BMI_update_prev)
  BMI_update_prev.place(x=1100,y=500,height=40,width=200)
  BMI_update_prev.configure(background="white")
  BMI_update_prev.configure(font="-family {Palatino Linotype} -size 15")
  BMI_update_prev.configure(foreground="#000000")
  ONGOING_DISEASE_update_prev.insert(END,ONGOING_DISEASE_display.get("1.0","end-1c"))
  ADDITIONAL_DISEASE_update_prev.insert(END,ADDITIONAL_DISEASE_display.get("1.0","end-1c"))
  PRECAUTION_update_prev.insert(END,PRECAUTION_display.get("1.0","end-1c"))
  
  add_problem=HoverButton(win10,text="UPDATE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="30",font=("times new roman",13),command=update_prev_comm).place(x=360,y=570)
  
win10=None
P_update_prev=None
W_update_prev=None
H_update_prev=None
D_update_prev=None
p_no_update_prev=None
bload_pressure_update_prev=None
o_dis_update_prev=None
add_dis_update_prev=None
prec_update_prev=None
P_BMI_update_prev=None
ONGOING_DISEASE_update_prev=None
ADDITIONAL_DISEASE_update_prev=None
PRECAUTION_update_prev=None






def old_patient_show():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  global win4
  global P_display,W_display,H_display,D_display,p_no_display,bload_pressure_display,P_BMI_display,age_display
  P_display=StringVar()
  W_display=StringVar()
  H_display=StringVar()
  D_display=StringVar()
  p_no_display=StringVar()
  bload_pressure_display=StringVar()
  P_BMI_display=StringVar()
  age_display=StringVar()
  
  win4= Toplevel(win3)
  win4.config(bg='#d6e0f0')
  win4.title("PATIENT RECORD")
  x, y = win4.winfo_screenwidth(), win4.winfo_screenheight()
  win4.geometry("%dx%d+0+0" % (x, y))
  Label(win4, text = "PATIENT NAME",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=290,y=30, height=40,width=150)
  patient_display = Entry(win4,textvariable=P_display,justify='center',state='readonly')
  patient_display.place(x=270,y=80, height=40,width=200)
  patient_display.configure(background="white")
  patient_display.configure(font="-family {Palatino Linotype} -size 15")
  patient_display.configure(foreground="#000000")
  

  Label(win4, text = "WEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=250, height=40,width=100)
  weight_display = Entry(win4,textvariable =W_display,justify='center',state='readonly')
  weight_display.place(x=1100,y=300, height=40,width=200)
  weight_display.configure(background="white")
  weight_display.configure(font="-family {Palatino Linotype} -size 15")
  weight_display.configure(foreground="#000000")


  Label(win4, text = "HEIGHT",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=350, height=40,width=100)
  HEIGHT_display = Entry(win4,textvariable =H_display,justify='center',state='readonly')
  HEIGHT_display.place(x=1100,y=400, height=40,width=200)
  HEIGHT_display.configure(background="white")
  HEIGHT_display.configure(font="-family {Palatino Linotype} -size 15")
  HEIGHT_display.configure(foreground="#000000")
  
 
  Label(win4, text = "DATE",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1140,y=30, height=40,width=110)
  DATE_display = Entry(win4,textvariable =D_display,justify='center',state='readonly')
  DATE_display.place(x=1100,y=80, height=40,width=200)
  DATE_display.configure(background="white")
  DATE_display.configure(font="-family {Palatino Linotype} -size 15")
  DATE_display.configure(foreground="#000000")
  

  Label(win4, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=150, height=40,width=110)
  PHONE_display = Entry(win4,textvariable=p_no_display,justify='center',state='readonly')
  PHONE_display.place(x=1100,y=200, height=40,width=200)
  PHONE_display.configure(background="white")
  PHONE_display.configure(font="-family {Palatino Linotype} -size 15")
  PHONE_display.configure(foreground="#000000")
  
  Label(win4, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=550, height=40,width=100)
  BP_display=Entry(win4,justify='center',textvariable=bload_pressure_display,state='readonly')
  BP_display.place(x=1100,y=600,height=40,width=200)
  BP_display.configure(background="white")
  BP_display.configure(font="-family {Palatino Linotype} -size 15")
  BP_display.configure(foreground="#000000")
  
  

  Label(win4, text = "PROBLEM *",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=80,y=150, height=40,width=350)
  global ONGOING_DISEASE_display
  ONGOING_DISEASE_display=Text(win4,height=12,width=32)
  ONGOING_DISEASE_display.place(x=80,y=200)
  ONGOING_DISEASE_display.configure(background="#eeeeee")
  ONGOING_DISEASE_display.configure(font="-family {Palatino Linotype} -size 15")
  ONGOING_DISEASE_display.configure(foreground="#000000")
 

  Label(win4, text = "DISEASE (if any)",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=390,y=150, height=40,width=330)
  global ADDITIONAL_DISEASE_display
  ADDITIONAL_DISEASE_display=Text(win4,height=12,width=32)
  ADDITIONAL_DISEASE_display.place(x=390,y=200)
  ADDITIONAL_DISEASE_display.configure(background="#eeeeee")
  ADDITIONAL_DISEASE_display.configure(font="-family {Palatino Linotype} -size 15")
  ADDITIONAL_DISEASE_display.configure(foreground="#000000")
 

  Label(win4, text = "PRECAUTIONS",bg="#eeeeee",fg="black",font=("Helvetica",15)).place(x=695,y=150, height=40,width=330)
  global PRECAUTION_display
  PRECAUTION_display=Text(win4,height=12,width=32)
  PRECAUTION_display.place(x=700,y=200)
  PRECAUTION_display.configure(background="#eeeeee")
  PRECAUTION_display.configure(font="-family {Palatino Linotype} -size 15")
  PRECAUTION_display.configure(foreground="#000000")

  Label(win4, text = "Age",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=690,y=30, height=40,width=100)
  global age_display_entry
  age_display_entry=Entry(win4,textvariable=age_display,justify='center',state='readonly')
  age_display_entry.place(x=650,y=80,height=40,width=200)
  age_display_entry.configure(background="white")
  age_display_entry.configure(font="-family {Palatino Linotype} -size 15")
  

  Label(win4, text = "BMI",bg="#d6e0f0",fg="black",font=("Helvetica",15)).place(x=1145,y=450, height=40,width=100)
  BMI_display=Entry(win4,state='readonly',justify='center',textvariable=P_BMI_display)
  BMI_display.place(x=1100,y=500,height=40,width=200)
  BMI_display.configure(background="white")
  BMI_display.configure(font="-family {Palatino Linotype} -size 15")
  BMI_display.configure(foreground="#000000")
  

  add_problem=HoverButton(win4,text="ADD ANOTHER RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="30",font=("times new roman",13),command=modify).place(x=200,y=570)
  HoverButton(win4,text="UPDATE THE RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="30",font=("times new roman",13),command=update_prev).place(x=600,y=570)
  
win4=None
P_display=None
W_display=None
H_display=None
D_display=None
p_no_display=None
bload_pressure_display=None
o_dis_display=None
add_dis_display=None
prec_display=None
P_BMI_display=None
ONGOING_DISEASE_display=None
ADDITIONAL_DISEASE_display=None
PRECAUTION_display=None

def update(rows):
  listBox.delete(*listBox.get_children())
  for i in rows:
    listBox.insert("", "end", values=i)

def clear():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  #====query=====
  c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record ")
  #====query=====
  z=c.fetchall()
  conn.commit()
  update(z)
  q.set("")
  



def search():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  global rows
  q2=q.get()
  #====query=====
  c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record WHERE name LIKE '%"+q2+"%'")
  #====query=====
  rows=c.fetchall()
  conn.commit()
  update(rows)
  
rows=None



def view_record():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  selected_item=listBox.selection()
  cur_item=listBox.focus()
  k=listBox.item(cur_item)["values"]
  #====query====
  c.execute("SELECT * FROM record")
  #=============
  r=c.fetchall()
  check=0
  if k=="":
    messagebox.showerror("warning","select the patient",parent=win3)
  else:
    for i in r:
      if i[3]==k[0] and i[0]==k[1]:
        check=1
        old_patient_show()
        P_display.set(i[0])
        W_display.set(i[1])
        H_display.set(i[2])
        p_no_display.set(i[4])
        bload_pressure_display.set(i[5])
        ONGOING_DISEASE_display.insert(END,i[6])
        ADDITIONAL_DISEASE_display.insert(END,i[7])
        PRECAUTION_display.insert(END,i[8])
        P_BMI_display.set(i[9])
        age_display.set(i[10])
        D_display.set(i[3])
        ONGOING_DISEASE_display.configure(state='disabled')
        ADDITIONAL_DISEASE_display.configure(state='disabled')
        PRECAUTION_display.configure(state='disabled')
  
def del_history():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  selected_item=listBox.selection()
  cur_item=listBox.focus()
  k=listBox.item(cur_item)["values"]
  dele=0
  if k=="":
    messagebox.showerror("warning","select the patient",parent=win3)
   
  else:
    if messagebox.askyesno("confirm delete","are you sure patient record will be deleted permenantly",parent=win3):
      #====query=====
      c.execute("DELETE FROM record WHERE date=? and name=? and phn_no=?",(k[0],k[1],k[2]))
      conn.commit()
      #====query=====
      messagebox.showinfo("Success","Deleted Successfully",parent=win3)
      x=listBox.selection()[0]
      listBox.delete(x)
    




def history():
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    global win3
    win3=Toplevel(win1)
    global q,listBox
    q=StringVar()
    x, y =win3.winfo_screenwidth(),win3.winfo_screenheight()
    win3.geometry("%dx%d+0+0" %(x,y))
    win3.config(bg='#e4f9f5')
    cols = ('DATE','NAME' ,'PHONE NO' ,'WEIGHT','HEIGHT','BP','BMI')
    listBox = tt.Treeview(win3, columns=cols, show='headings', selectmode='browse',height=25)
    listBox.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
    for col in cols:
        listBox.heading(col, text=col)
    vsb = tt.Scrollbar(win3, orient="vertical", command=listBox.yview)
    vsb.place(relx=0.937, rely=0.216, relheight=0.580, relwidth=0.012)
    vsb1 = tt.Scrollbar(win3, orient="horizontal", command=listBox.xview)
    vsb1.place(relx=0.046, rely=0.797, relheight=0.025, relwidth=0.896)
    listBox.configure(xscrollcommand=vsb1.set)
    c.execute("select date,name,phn_no,weight,height,bp,bmi from record order by date")
    for i in c:
        listBox.insert("", "end", values=i)
    conn.commit()
    Label(win3,text="PATIENT RECORD",font=("times new roman",30),bg="#e4f9f5").place(x=500,y=50)
    Label(win3,text="Enter name",font=("times new roman",18),bg="#e4f9f5").place(x=60,y=70)
    Entry(win3,textvariable=q).place(x=200,y=65,height=35,width=230)
    Button1 = HoverButton(win3,text="VIEW RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=view_record)
    Button1.place(relx=0.200, rely=0.867, height=60, width=250)
    Button2 = HoverButton(win3,text="search",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=search)
    Button2.place(x=200,y=110, height=40, width=100)
    Button3 = HoverButton(win3,text="DELETE RECORD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=del_history)
    Button3.place(relx=0.400, rely=0.867, height=60, width=250)
    Button4= HoverButton(win3,text="BACK",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=delete_win3)
    Button4.place(relx=0.600, rely=0.867, height=60, width=250)
    Button5 = HoverButton(win3,text="clear",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=clear)
    Button5.place(x=330,y=110, height=40, width=100)
    
win3=None
listBox=None
q=None


    

def Record():
  global win1
  win1=Toplevel(screen8)
  menue(win1)
  win1.title("PATIENT RECORD")
  x, y = win1.winfo_screenwidth(), win1.winfo_screenheight()
  win1.geometry("%dx%d+0+0" %(x,y))
  win1.bg=ImageTk.PhotoImage(file="l5.jpg")
  win1.bg_image=Label(win1,image=win1.bg).place(x=0,y=0,relwidth=1,relheight=1)
    #---bg==== 
  #win1.overrideredirect(True)
  
  title=Label(win1,text="PATIENT RECORD",font=("helvetica",34,"bold"),fg="black",bg="#e6e6e6").place(x=490,y=80)
  new_patient=HoverButton(win1,text="ADD NEW PATIENT",activebackground='#a8e6cf',bg="#61c0bf",fg="black",height="4",bd=3,width="40",font=("helvetica",13),command = add_patient).place(x=500,y=200)
  existing_patient=HoverButton(win1,text="EXISTING PATIENT",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="4",width="40",font=("helvetica",13),command=history).place(x=500,y=310)
  main_close=HoverButton(win1,text="CLOSE",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=delete_win1).place(x=545,y=450)
win1=None


#======================================================================================================================================================================================================================

#=======================   patient medicine   =================================
def del_med():
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    selected_item1=listBox1.selection()
    cur_item1=listBox1.focus()
    k1=listBox1.item(cur_item1)["values"]
    if k1=="":
        messagebox.showerror("warning","select the field",parent=med3)
    
    else:
        if messagebox.askyesno("confirm delete","are you sure patient medicine will be deleted permenantly",parent=med3):
            selected_item=listBox.selection()
            cur_item=listBox.focus()
            k=listBox.item(cur_item)["values"]
            #====query========
            c.execute("DELETE FROM medicine_table WHERE date=? and name=? and phn_no=? and medicine=? and dosage=? and timings=? and days=?",(k[0],k[1],k[2],k1[0],k1[1],k1[2],k1[3]))
            conn.commit()
            #=================
            x=listBox1.selection()[0]
            listBox1.delete(x)
            messagebox.showinfo("Success","Deleted Successfully",parent=med3)
    
   
        
def view_back():
    med3.destroy()


def view_medicine():
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    selected_item=listBox.selection()
    cur_item=listBox.focus()
    k=listBox.item(cur_item)["values"]
    if k=="":
      messagebox.showerror("warning","select the field",parent=med1)
    else:
      r=c.execute("select medicine,dosage,timings,days from medicine_table where name=? and date=? and phn_no=?",(k[1],k[0],k[2]))
      conn.commit()
      l=[]
      for i in r:
        l.append(i)
      global med3
      med3=Toplevel(med1)
      x, y =med3.winfo_screenwidth(),med3.winfo_screenheight()
      med3.geometry("%dx%d+0+0" %(x,y))
      med3.config(bg='#d6e0f0')
      selected_item=listBox.selection()
      cur_item=listBox.focus()
      k=listBox.item(cur_item)["values"]
      s1=StringVar()
      s2=StringVar()
      s3=StringVar()
      s4=StringVar()
      s1.set(k[1])
      s2.set(k[5])
      s3.set(k[0])
      s4.set(k[2])
      Label(med3, text = "Patient name",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=150,y=33)
      patient_name=Entry(med3,justify='center',textvariable=s1,state='readonly')
      patient_name.place(x=310,y=30, height=40,width=150)
      patient_name.configure(background="white")
      patient_name.configure(font="-family {Palatino Linotype} -size 15")
      patient_name.configure(foreground="#000000")

      Label(med3, text = "BP",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=480,y=33)
      patient_bp = Entry(med3,justify='center',state='readonly',textvariable=s2)
      patient_bp.place(x=530,y=30, height=40,width=150)
      patient_bp.configure(background="white")
      patient_bp.configure(font="-family {Palatino Linotype} -size 15")
      patient_bp.configure(foreground="#000000")

      Label(med3, text = "Date",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=700,y=33)
      patient_date = Entry(med3,justify='center',state='readonly',textvariable=s3)
      patient_date.place(x=770,y=30, height=40,width=150)
      patient_date.configure(background="white")
      patient_date.configure(font="-family {Palatino Linotype} -size 15")
      patient_date.configure(foreground="#000000")

      Label(med3, text = "PHONE NO",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=950,y=33)
      patient_n = Entry(med3,justify='center',state='readonly',textvariable=s4)
      patient_n.place(x=1090,y=30, height=40,width=150)
      patient_n.configure(background="white")
      patient_n.configure(font="-family {Palatino Linotype} -size 15")
      patient_n.configure(foreground="#000000")

      cols = ('Medicine Name','dosage' ,'timings' ,'days')
      global listBox1
      listBox1 = tt.Treeview(med3, columns=cols, show='headings', selectmode='browse',height=25)
      listBox1.place(relx=0.046, rely=0.120, relheight=0.550, relwidth=0.896)
      for col in cols:
          listBox1.heading(col, text=col)
      vsb = tt.Scrollbar(med3, orient="vertical", command=listBox1.yview)
      vsb.place(relx=0.935, rely=0.120, relheight=0.550, relwidth=0.012)
      #=====query========
      c.execute("select medicine,dosage,timings,days from medicine_table where name=? and date=? and phn_no=?",(k[1],k[0],k[2]))
      conn.commit()
      #==================
      for i in c:
          listBox1.insert("", "end", values=i)
      conn.commit()
      Button(med3,text="DELETE",bg="#61c0bf",fg="black",bd=3,height="2",width="25",font=("times new roman",13),command=del_med).place(x=570,y=600)
      Button(med3,text="BACK",bg="#61c0bf",fg="black",bd=3,height="2",width="25",font=("times new roman",13),command=view_back).place(x=870,y=600)
      Button(med3,text="ADD MEDICAL PRESCRIPTION",bg="#61c0bf",fg="black",bd=3,height="2",width="28",font=("times new roman",13),command=add_medicine).place(x=260,y=600)
med3=None
listBox1=None   
    

def add():
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    selected_item=listBox.selection()
    cur_item=listBox.focus()
    k=listBox.item(cur_item)["values"]
    
    if t1.get()=="" or t2.get()=="":
        messagebox.showerror("warning","fill the fields",parent=med2)

    else:
        #===query=====
        c.execute('INSERT INTO medicine_table(name,date,phn_no,medicine,dosage,timings,days) VALUES(?,?,?,?,?,?,?)',(k[1],k[0],k[2],t1.get(),t2.get(),t3.get(),t4.get()))
        conn.commit()
        #=============
        messagebox.showinfo("Success","medicine Added",parent=med2)
        t1.set("")
        t2.set("")
        t3.set("")
        t4.set("")
    c.execute("select medicine,dosage,timings,days from medicine_table where name=? and date=? and phn_no=?",(k[1],k[0],k[2]))
    conn.commit()
    #==================
    for i in c:
        listBox1.insert("", "end", values=i)
def add_medicine():
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    selected_item=listBox.selection()
    cur_item=listBox.focus()
    k=listBox.item(cur_item)["values"]
    if k=="":
        messagebox.showerror("warning","select the field",parent=med1)

    else:
        global med2
        med2=Toplevel(med1)
        med2.title("ADD MEDICAL PRESCRIPTION")
        med2.config(bg='#d6e0f0')
        med2.geometry('500x400+300+100')
        global t1,t2,t3,t4
        t1=StringVar()
        t2=StringVar()
        t3=StringVar()
        t4=StringVar()
        Label(med2, text = "Medicine name",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=50)
        patient_name=Entry(med2,justify='center',textvariable=t1)
        add_placeholder_to(patient_name, 'Enter medicine name...')
  

        patient_name.place(x=250,y=50, height=40,width=170)
        patient_name.configure(background="white")
        patient_name.configure(font="-family {Palatino Linotype} -size 15")
        patient_name.configure(foreground="#000000")

        Label(med2, text = "dosage",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=100)
        patient_bp=Entry(med2,justify='center',textvariable=t2)
        add_placeholder_to(patient_bp, '1-1-1')
        patient_bp.place(x=250,y=100, height=40,width=170)
        patient_bp.configure(background="white")
        patient_bp.configure(font="-family {Palatino Linotype} -size 15")
        patient_bp.configure(foreground="#000000")

        Label(med2, text = "timings",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=150)
        patient_date=Entry(med2,justify='center',textvariable=t3)
        add_placeholder_to(patient_date, 'ex morning,evening,night')
        patient_date.place(x=250,y=150, height=40,width=170)
        patient_date.configure(background="white")
        patient_date.configure(font="-family {Palatino Linotype} -size 15")
        patient_date.configure(foreground="#000000")

        Label(med2, text = "days",bg="#d6e0f0",fg="black",font=("Helvetica",18)).place(x=60,y=200)
        patient_n=Entry(med2,justify='center',textvariable=t4)
        add_placeholder_to(patient_n, 'ex 3 days')
        patient_n.place(x=250,y=200, height=40,width=170)
        patient_n.configure(background="white")
        patient_n.configure(font="-family {Palatino Linotype} -size 15")
        patient_n.configure(foreground="#000000")
    
        HoverButton(med2,text="ADD",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=add).place(x=280,y=280, height=40, width=100)
    
t1=None
t2=None
t3=None
t4=None
med2=None
def med_back():
    med1.destroy()
def update_med(rows):
  listBox.delete(*listBox.get_children())
  for i in rows:
    listBox.insert("", "end", values=i)

def clear_med():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  #====query=====
  c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record ")
  #====query=====
  z=c.fetchall()
  conn.commit()
  update_med(z)
  q1.set("")
  



def search_med():
  conn=sqlite3.connect('my_database.db')
  c=conn.cursor()
  global rows
  q2=q1.get()
  #====query=====
  c.execute("SELECT date,name,phn_no,weight,height,bp,bmi FROM record WHERE name LIKE '%"+q2+"%'")
  #====query=====
  rows=c.fetchall()
  conn.commit()
  update_med(rows)
  
rows=None

def medmenue(t):
    def onclosing():
        t.destroy()
        
    t.deiconify()
    t.iconbitmap(r"logo.ico")
    x, y = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (x, y))
    t.resizable(1, 1)

    """if t!=cd:        
        cd.withdraw()
    else:
        root.withdraw()"""
    
    #Menue Bar
    menubar=Menu(t)
    t.config(menu=menubar)
    #Sub Menue
    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=submenu)
    submenu.add_command(label="Exit",command=onclosing)

    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=submenu)
    submenu.add_command(label="Dashboard",command=session)
    submenu.add_command(label="Patient History",command=Record)
    submenu.add_command(label="Patient Medicine",command=medicine)
    submenu.add_command(label="Patient Diet",command=diet)
    submenu.add_command(label="Patient Yoga",command=yogahere)
    

    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=submenu)
    submenu.add_command(label="About Us",command=lambda:aboutus(t))

    t.protocol("WM_DELETE_WINDOW",onclosing)

def medicine():
    conn=sqlite3.connect('my_database.db')
    c=conn.cursor()
    global med1
    med1=Toplevel(screen8)
    medmenue(med1)
    x, y =med1.winfo_screenwidth(),med1.winfo_screenheight()
    med1.geometry("%dx%d+0+0" %(x,y))
    med1.config(bg='#d6e0f0')
    #top.overrideredirect(True) 
    global q1,listBox
    q1=StringVar()
    cols = ('DATE','NAME' ,'PHONE NO' ,'WEIGHT','HEIGHT','BP','BMI')
    listBox = tt.Treeview(med1, columns=cols, show='headings', selectmode='browse',height=25)
    listBox.place(relx=0.020, rely=0.180, relheight=0.680, relwidth=0.750)
    for col in cols:
        listBox.heading(col, text=col)
    vsb = tt.Scrollbar(med1, orient="vertical", command=listBox.yview)
    vsb.place(relx=0.770, rely=0.180, relheight=0.680, relwidth=0.012)
    vsb1 = tt.Scrollbar(med1, orient="horizontal", command=listBox.xview)
    vsb1.place(relx=0.020, rely=0.860, relheight=0.025, relwidth=0.745)
    listBox.configure(xscrollcommand=vsb1.set)
    #====query======
    c.execute("select date,name,phn_no,weight,height,bp,bmi from record ORDER BY date")
    for i in c:
        listBox.insert("", "end", values=i)
    conn.commit()
    #===============
    Label(med1,text="PATIENT MEDICINE",font=("times new roman",30),bg="#d6e0f0").place(x=500,y=25)
    Label(med1,text="Enter name",font=("times new roman",18),bg="#d6e0f0").place(x=60,y=30)
    e1=Entry(med1,textvariable=q1).place(x=200,y=25,height=35,width=230)
    #add_placeholder_to(e1, 'Enter Patient Name...')
  

    #Button1 = HoverButton(med1,text="ADD MEDICAL PRESCRIPTION",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=add_medicine)
    #Button1.place(relx=0.800, rely=0.250, height=60, width=250)
    
    Button3 = HoverButton(med1,text="VIEW MEDICAL PRESCRIPTION",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=view_medicine)
    Button3.place(relx=0.800, rely=0.400, height=60, width=250)
    Button4= HoverButton(med1,text="BACK",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="3",width="28",font=("times new roman",13),command=med_back)
    Button4.place(relx=0.800, rely=0.550, height=60, width=250)

    Button2 = HoverButton(med1,text="search",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=search_med)
    Button2.place(x=200,y=80, height=40, width=100)
    Button5 = HoverButton(med1,text="clear",activebackground='#a8e6cf',bg="#61c0bf",fg="black",bd=3,height="2",width="20",font=("times new roman",13),command=clear_med)
    Button5.place(x=330,y=80, height=40, width=100)
    
med1=None
q1=None
listBox=None






#==============================================================================

#=========================patient diet======================================#
from sqlite3 import *    
conn = connect('my_database.db')
mycursor = conn.cursor()

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as tt

import datetime as dt

listBox,option3,r3,r2,listBox1,r1,r4,option1,fname4,fg,Quantity1,Dimension1,Timetoeat,option2,listBox2,option4=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
foodname1,foodname2,foodname3,foodname4,foodname5,foodname6,foodname7,foodname8,foodname9,foodname10,fgname1,fgname2,fgname3,fgname4,fgname5,fgname6,fgname7,fgname8,fgname9,fgname10=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
fname2,fg1,Quantity2,Dimension2,Timetoeat1,listBox3,option5,r4,r5,g1,g2,g3,g4=None,None,None,None,None,None,None,None,None,None,None,None,None

def diet():
    try:
        mycursor.execute('select * from cm1')
    except(OperationalError):
        mycursor.execute("create table cm1(nameoffooditem text, foodgroup text,Quantity int,Dimensions text,Timetoeat text)")

    try:
        mycursor.execute('select * from cm2')
    except(OperationalError):
        mycursor.execute("create table cm2(nameoffooditem1 text, foodgroup1 text,Quantity1 int,Dimensions1 text,Timetoeat1 text)")

    try:
        mycursor.execute('select * from spd')
    except(OperationalError):
        mycursor.execute("create table spd(nameoffooditem2 text, foodgroup2 text,Quantity2 int,Dimensions2 text,Timetoeat2 text)")

    try:
        mycursor.execute('select * from patientdiet')
    except(OperationalError):
        mycursor.execute("create table patientdiet(pname text,pphno int,pdate date,nameoffooditem3 text, foodgroup3 text,Quantity3 int,Dimensions3 text,Timetoeat3 text)")

    try:
        mycursor.execute('select * from viewdiet')
    except(OperationalError):
        mycursor.execute("create table viewdiet(pname1 text,pphno1 int, pdate1 date,nooffooditem int,weight real)")

    root=Toplevel(screen8)
    x, y = root.winfo_screenwidth(), root.winfo_screenheight()
    root.config(bg="#d6e0f0")
    root.geometry("%dx%d+0+0" % (x, y))
    root.title("DOCTOR CURE : Patient Diet")
    root.iconbitmap(r"logo.ico")
    
    CD=tk.Toplevel(root)
    #CD.config(bg='light blue')
    CD.title("DOCTORCURE: RECOMMENDED DIET")

    cd = tk.Toplevel(root)
    #cd.config(bg='light blue')
    cd.title("DOCTORCURE: CREATE DIET")

    VD=tk.Toplevel(root)
    #VD.config('light blue')
    VD.title("DOCTORCURE: VIEW DIET")

    def clear4():
        r1.set("")
        r2.set("")
        r4.set("")

    def clear3():
        fname4.set("")
        fg.set("")
        Quantity1.set("")
        Dimension1.set("")
        Timetoeat.set("")

    def clear2():
        r6.set("")
        r11.set("")
        r12.set("")

    def clear1():
        fname2.set("")
        fg1.set("")
        Quantity2.set("")
        Dimension2.set("")
        Timetoeat1.set("")

    def menue(t):
        def onclosing():
            root.destroy()
            
        t.deiconify()
        t.iconbitmap(r"logo.ico")
        t.config(bg="#d6e0f0")
        x, y = t.winfo_screenwidth(),t.winfo_screenheight()
        t.geometry("%dx%d+0+0" % (x, y))
        t.resizable(1, 1)

        if t!=cd and t!=CD and t!=VD:        
            cd.withdraw()
            CD.withdraw()
            VD.withdraw()
        elif t!=cd and t!=root and t!=CD:
            root.withdraw()
            cd.withdraw()
            CD.withdraw()
        elif t!=cd and t!=root and t!=VD:
            root.withdraw()
            cd.withdraw()
            VD.withdraw()
        else:
            root.withdraw()
            CD.withdraw()
            VD.withdraw()
        
        #Menue Bar
        menubar=tk.Menu(t)
        t.config(menu=menubar)
        #Sub Menue
        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=submenu)
        submenu.add_command(label="Exit",command=onclosing)

        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=submenu)
        submenu.add_command(label="Dashboard",command=session)
        submenu.add_command(label="Patient History",command=Record)
        submenu.add_command(label="Patient Medicine",command=medicine)
        submenu.add_command(label="Patient Diet",command=lambda:toplevel1(root))
        submenu.add_command(label="Patient Yoga",command=yogahere)
        def aboutus():
            messagebox.showinfo("About Doctor Cure ","This application helps a doctor to Manage Patient History,Diet and Medicine which doctor needs to diagnose patient easily.\n\nCreated By Binary Beast using Python",parent=t)

        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=submenu)
        submenu.add_command(label="About Us",command=aboutus)

        t.protocol("WM_DELETE_WINDOW",onclosing)
        
    ###################################################################################Personal Diet####################################################################################################
        
    def toplevel1(top1):
        global listBox,option3,r3
        menue(top1)
        top1.config(bg="#d6e0f0")
        r3 = tk.StringVar()
        option3 = tk.StringVar()
        Label1 = tk.Label(top1)
        Label1.place(relx=0.375, rely=0.019, height=79, width=492)
        Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold")
        Label1.configure(text='''PATIENT DIET''',bg='#d6e0f0',fg='black')

        Label2 = tk.Label(top1)
        Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.241)
        Label2.configure(font="-family {Palatino Linotype} -size 17")
        Label2.configure(text='''TYPE TO SEARCH -:''',bg='#d6e0f0',fg='black')

        Entry1 = tk.Entry(top1,textvariable=r3)
        Entry1.place(relx=0.195, rely=0.125, height=40, relwidth=0.241)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="-family {Palatino Linotype} -size 15")
        Entry1.configure(foreground="#000000")
        Entry1.configure(highlightbackground="#d9d9d9")
        Entry1.configure(highlightcolor="black")
        Entry1.configure(insertbackground="black")
        Entry1.configure(selectbackground="#c4c4c4")
        Entry1.configure(selectforeground="black")

        TCombobox1 = tt.Combobox(top1, textvariable=option3,state='readonly')
        value_list = ['All Records', "Name of food Items","Food Group","Calories","Fat (g)", "Protein (g)","Carbohydrate (g)","Sugars (g)","Fiber (g)","Cholesterol (mg)","Calcium (mg)","Iron, Fe (mg)","Potassium, K (mg)"]
        TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
        option3.set("Choose Category to Search")

        
        cols = ("Name of food Items","Food Group","Calories","Fat (g)", "Protein (g)","Carbohydrate (g)","Sugars (g)","Fiber (g)","Cholesterol (mg)","Saturated Fats (g)","Calcium (mg)","Iron, Fe (mg)","Potassium, K (mg)","Magnesium (mg)","Vitamin A, IU (IU)", "Vitamin A, RAE (mcg)", "Vitamin C (mg)","Vitamin B-12 (mcg)","Vitamin D (mcg)","Vitamin E (Alpha-Tocopherol) (mg)", "Net-Carbs (g)","Water (g)","Omega 3s (mg)","Omega 6s (mg)","PRAL score ()","Trans Fatty Acids (g)","Sucrose (g)","Glucose (Dextrose) (g)","Fructose (g)","Lactose (g)","Maltose (g)","Galactose (g)","Starch (g)","Phosphorus, P (mg)","Sodium (mg)","Zinc, Zn (mg)", "Copper, Cu (mg)","Manganese (mg)","Selenium, Se (mcg)" ,"Fluoride, F (mcg)","Thiamin (B1) (mg)","Riboflavin (B2) (mg)", "Niacin (B3) (mg)", "Pantothenic acid (B5) (mg)","Vitamin B6 (mg)", "Folate (B9) (mcg)","Folic acid (mcg)", "Food Folate (mcg)","Folate DFE (mcg)", "Choline (mg)","Vitamin D3 (cholecalciferol) (mcg)","Vitamin D (IU) (IU)", "Vitamin K (mcg)","Dihydrophylloquinone (mcg)", "Fatty acids, total monounsaturated (mg)","Fatty acids, total polyunsaturated (mg)","Stigmasterol (mg)","Campesterol (mg)", "Beta-sitosterol (mg)", "Fatty acids, total trans-monoenoic (mg)","Fatty acids, total trans-polyenoic (mg)","Tryptophan (mg)","Threonine (mg)", "Isoleucine (mg)","Leucine (mg)","Lysine (mg)", "Methionine (mg)","Cystine (mg)","Phenylalanine (mg)",  "Tyrosine (mg)","Valine (mg)",  "Alanine (mg)", "Aspartic acid (mg)",  "Glutamic acid (mg)","Glycine (mg)",	"Hydroxyproline (mg)","Alcohol (g)","Caffeine (mg)","Theobromine (mg)",	"200 Calorie Weight (g)")
        listBox = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox.heading(col, text=col)
        listBox.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
        vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox.xview)
        vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
        listBox.configure(xscrollcommand=vsb.set)

        vsb = tt.Scrollbar(top1, orient="vertical", command=listBox.yview)
        vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
        listBox.configure(yscrollcommand=vsb.set)

        Button1 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:search_btn())
        Button1.place(relx=0.021, rely=0.867, height=60, width=250)
        Button1.configure(font="-family {Palatino Linotype} -size 16")
        Button1.configure(foreground="#000000")
        Button1.configure(pady="0")
        Button1.configure(text='''SEARCH''')

        Button2 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:toplevel2(cd))
        Button2.place(relx=0.200, rely=0.867, height=60, width=250)
        Button2.configure(font="-family {Palatino Linotype} -size 16")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''CUSTOM DIET''')

        Button3 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:delete_btn(top1))
        Button3.place(relx=0.415, rely=0.867, height=60, width=250)
        Button3.configure(font="-family {Palatino Linotype} -size 16")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightcolor="black")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(pady="0")
        Button3.configure(text='''DELETE''')

        Button4 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:viewdiet(VD))
        Button4.place(relx=0.627, rely=0.867, height=60, width=250)
        Button4.configure(font="-family {Palatino Linotype} -size 14")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text='''VIEW ALL PATIENT DIET''')

        Button5 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:commondiet(CD))
        Button5.place(relx=0.809, rely=0.867, height=60, width=250)
        Button5.configure(font="-family {Palatino Linotype} -size 14")
        Button5.configure(foreground="#000000")
        Button5.configure(highlightbackground="#d9d9d9")
        Button5.configure(highlightcolor="black")
        Button5.configure(pady="0")
        Button5.configure(text='''RECOMMENDED DIET''')

        mycursor.execute("select count(*) from MyFood1 order by Name asc ")
        for i in mycursor:
            if i[0]>=50:
                mycursor.execute("select * from MyFood1 order by Name asc limit 50")
                for j in mycursor:
                    listBox.insert("", "end", values=j)
            else:
                mycursor.execute("select * from MyFood1 order by Name asc ")
                for i in mycursor:
                    listBox.insert("", "end", values=i)
    def delete_btn(tp):
        try:
            global listBox
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=tp)
            if MsgBox == "yes":
                selected_items = listBox.selection()
                cur_item=listBox.focus()
                k=listBox.item(cur_item)["values"]
                mycursor.execute("DELETE FROM MyFood1 WHERE Name=? AND FoodGroup=? AND Calories=? AND Fat=? AND Protein=? AND Carbohydrate=? AND Sugars=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),str(k[5]),str(k[6])))
                listBox.delete(*listBox.get_children())
                mycursor.execute("select count(*) from MyFood1 order by Name asc ")
                for i in mycursor:
                    if i[0]>=50:
                        mycursor.execute("select * from MyFood1 order by Name asc limit 50")
                        for j in mycursor:
                            listBox.insert("", "end", values=j)
                    else:
                        mycursor.execute("select * from MyFood1 order by Name asc ")
                        for i in mycursor:
                            listBox.insert("", "end", values=i)
                conn.commit()
            else:
                pass
        except:
            pass
        
    def search_btn():
        global listBox,option3,r3
        _entry = r3.get()
        _option = option3.get()

        if (_option == 'Name of food Items'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Name like "%{0}%" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Food Group'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where FoodGroup like "%{0}%" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == "Calories"):
            listBox.delete(*listBox.get_children())
            mycursor.execute("select * from MyFood1 where Calories like '{0}' order by Name asc".format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Fat (g)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Fat like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Protein (g)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Protein like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Carbohydrate (g)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Carbohydrate like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Sugars (g)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Sugars like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Fiber (g)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Fiber like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Cholesterol (mg)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Cholesterol like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Calcium (mg)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where Calcium like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Iron, Fe (mg)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where IronFe like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Potassium, K (mg)'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from MyFood1 where PotassiumK like "{0}" order by Name asc'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == "All Records"):
            listBox.delete(*listBox.get_children())
            mycursor.execute("select * from MyFood1 order by Name asc ")
            for i in mycursor:
                listBox.insert("", "end", values=i)     
        else:
            option3.set("Choose Category Correctly!")

    def toplevel2(top2):
        global listBox2,r1,r2,r4
        top2.config(bg="#d6e0f0")

        top2.iconbitmap(r"logo.ico")
        x, y = root.winfo_screenwidth(), root.winfo_screenheight()
        top2.geometry("%dx%d+0+0" % (x, y))
        top2.deiconify()

        def onclosings():
            mycursor.execute("Drop table if exists spd")
            top2.withdraw()
            Add2.withdraw()
            Mdd1.withdraw()
            sug1.withdraw()

        def onclosing():
            clear1()
            Add2.withdraw()

        def onclosings1():
            Mdd1.withdraw()

        def onclosings2():
            sug1.withdraw()

        Add2 = tk.Toplevel(cd)
        Add2.config(bg='#d6e0f0')
        Add2.title("DOCTOR CURE: ADD TO PATIENT DIET")
        Add2.withdraw()
        Add2.protocol("WM_DELETE_WINDOW",onclosing)

        container = tt.Frame(Add2)
        canvas = tk.Canvas(container,height=500,width=450)
        scrollbar = tt.Scrollbar(container, orient="vertical", command=canvas.yview)
        top = tt.Frame(canvas)

        top.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=top, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        Mdd1 = tk.Toplevel(cd)
        Mdd1.title("STOCK UP: MODIFY ENTRY")
        Mdd1.withdraw()
        Mdd1.protocol("WM_DELETE_WINDOW",onclosings1)

        sug1 = tk.Toplevel(cd)
        sug1.title("STOCK UP: FOOD ITEMS SUGGESTIONS")
        sug1.withdraw()
        sug1.protocol("WM_DELETE_WINDOW",onclosings2)
        
        Label1 = tk.Label(top2)
        Label1.place(relx=0.375, rely=0.009, height=79, width=492)
        Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold",bg='#d6e0f0',fg='black')
        Label1.configure(text='''CREATE DIET''')

        Label2 = tk.Label(top2)
        Label2.place(relx=0.001, rely=0.095, height=40, relwidth=0.241)
        Label2.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label2.configure(text='''NAME -:''')
        
        r1 = tk.StringVar()
        Entry1 = tk.Entry(top,width=28, textvariable=fname2)
        Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg1)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity2)
        Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension2)
        Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        Entry1 = tk.Entry(top2,textvariable=r1)
        Entry1.place(relx=0.155, rely=0.095, height=30, relwidth=0.211)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="-family {Palatino Linotype} -size 15")
        Entry1.configure(foreground="#000000")
        Entry1.configure(highlightbackground="#d9d9d9")
        Entry1.configure(highlightcolor="black")
        Entry1.configure(insertbackground="black")
        Entry1.configure(selectbackground="#c4c4c4")
        Entry1.configure(selectforeground="black")

        Label4 = tk.Label(top2)
        Label4.place(relx=0.035, rely=0.145, height=40, relwidth=0.241)
        Label4.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label4.configure(text='''DATE(dd/mm/yy) -:''')
        
        r4 = tk.StringVar()
        Entry4 = tk.Entry(top2,textvariable=r4)
        Entry4.place(relx=0.225, rely=0.145, height=30, relwidth=0.141)
        Entry4.configure(background="white")
        Entry4.configure(disabledforeground="#a3a3a3")
        Entry4.configure(font="-family {Palatino Linotype} -size 15")
        Entry4.configure(foreground="#000000")
        Entry4.configure(highlightbackground="#d9d9d9")
        Entry4.configure(highlightcolor="black")
        Entry4.configure(insertbackground="black")
        Entry4.configure(selectbackground="#c4c4c4")
        Entry4.configure(selectforeground="black")

        Label3 = tk.Label(top2)
        Label3.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
        Label3.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label3.configure(text='''PH.NO -:''')

        r2 = tk.StringVar()
        Entry2 = tk.Entry(top2,textvariable=r2)
        Entry2.place(relx=0.735, rely=0.125, relheight=0.049, relwidth=0.169)
        Entry2.configure(background="white")
        Entry2.configure(disabledforeground="#a3a3a3")
        Entry2.configure(font="-family {Palatino Linotype} -size 15")
        Entry2.configure(foreground="#000000")
        Entry2.configure(highlightbackground="#d9d9d9")
        Entry2.configure(highlightcolor="black")
        Entry2.configure(insertbackground="black")
        Entry2.configure(selectbackground="#c4c4c4")
        Entry2.configure(selectforeground="black")
        
        cols = ("Name of food Items","Food Group","Quantity","Dimensions","Time to eat")
        listBox2 = tt.Treeview(top2, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox2.heading(col, text=col)
        listBox2.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.627)
        vsb = tt.Scrollbar(top2, orient="horizontal", command=listBox2.xview)
        vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.627)
        listBox2.configure(xscrollcommand=vsb.set)

        vsb1 = tt.Scrollbar(top2, orient="vertical", command=listBox2.yview)
        vsb1.place(relx=0.674, rely=0.216, relheight=0.580, relwidth=0.012)
        listBox2.configure(yscrollcommand=vsb1.set)

        sbframe=tk.Frame(top2)
        sbframe.config(bg='#d6e0f0')
        sbframe.place(relx=0.748, rely=0.224, relheight=0.669, relwidth=0.179)

        Button1 = HoverButton(sbframe,padx=98,pady=5,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:add_btn(top,Add2))
        Button1.pack(side="top",pady=15)
        Button1.configure(font="-family {Palatino Linotype} -size 12 -weight bold")
        Button1.configure(foreground="#000000")
        Button1.configure(highlightbackground="#d9d9d9")
        Button1.configure(highlightcolor="black")
        Button1.configure(text='''ADD FOOD ITEM''')

        Button2 = HoverButton(sbframe,padx=110,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:delete_btn2())
        Button2.pack(side="top",pady=15)
        Button2.configure(font="-family {Palatino Linotype} -size 14 ")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''DELETE''')

        Button3 = HoverButton(sbframe,padx=100,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:modi_btn(Mdd1))
        Button3.pack(side="top",pady=25) 
        Button3.configure(font="-family {Palatino Linotype} -size 15 ")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightcolor="black")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(pady="0")
        Button3.configure(text='''MODIFY''')

        Button4 = HoverButton(sbframe,padx=99,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:Assign1(top2))
        Button4.pack(side="top",pady=15)
        Button4.configure(font="-family {Palatino Linotype} -size 14 ")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text='''SAVE AND ASSIGN''')

        Button5 = HoverButton(sbframe,padx=72,pady=20,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",command=lambda:Suggestions(sug1))
        Button5.pack(side="top",pady=15)
        Button5.configure(font="-family {Palatino Linotype} -size 14")
        Button5.configure(foreground="#000000")
        Button5.configure(highlightbackground="#d9d9d9")
        Button5.configure(highlightcolor="black")
        Button5.configure(pady="0")
        Button5.configure(text='''DIET SUGGESTIONS''')
        
        try:
            t=mycursor.execute("select * from record").fetchall()[-1]
            r1.set(t[0])
            r4.set(t[3])
            r2.set(t[4])
        except:
            pass

        top2.protocol("WM_DELETE_WINDOW",onclosings)

    def add_btn(top,top1):
        mycursor.execute("create table if not exists spd(nameoffooditem2 text, foodgroup2 text,Quantity2 int,Dimensions2 text,Timetoeat2 text)")
        
        top1.deiconify()
        top1.geometry("470x500")

        global fname2,fg1,Quantity2,Dimension2,Timetoeat1
        
        def onclosing():
            clear1()
            top1.withdraw()

        fname2=tk.StringVar()
        fg1=tk.StringVar()
        Quantity2=tk.StringVar()
        Dimension2=tk.StringVar()
        Timetoeat1=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Diet Record Entry")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Name of food Items")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=3,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Food Group")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=4,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Quantity")
        
        Label3 = tk.Label(top)
        Label3.grid(row=5,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Dimensions")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=6,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Time to eat")

        Entry1 = tk.Entry(top,width=28, textvariable=fname2)
        Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg1)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity2)
        Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension2)
        Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat1)
        Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=HoverButton(top,text="ADD",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=lambda:saveadd2(top1))
        button6.grid(row=8,column=1,pady=20)

        button7=HoverButton(top,text="CANCEL",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=onclosing)
        button7.grid(row=8,column=0,pady=20)

    def saveadd2(tp):
        try:
            global fname2,fg1,Quantity2,Dimension2,Timetoeat1,listBox2
            
            if (fname2.get() == "" or fg1.get() == "" or Quantity2.get() == "" or Dimension2.get() == "" or Timetoeat1.get() == ""):
                clear1()
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                if(fname2.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fname2.get())
                if (fg1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fg1.get())
                if (Quantity2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    num=Quantity2.get()
                    if(num.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                    else:
                        list1.append(num)
                if (Dimension2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(Dimension2.get())
                if (Timetoeat1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    num2=Timetoeat1.get()
                    list1.append(num2)
                
                mycursor.execute("select * from spd where nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                x1=[]
                for y in mycursor:
                    x1.append(y)
                if len(x1)==0:
                    mycursor.execute("INSERT INTO spd VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                    conn.commit()
                    clear1()
                    tp.withdraw()
                else:
                    tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp)
            listBox2.delete(*listBox2.get_children())
            mycursor.execute("select * from spd order by Timetoeat2 asc")
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        except:
            pass

    def delete_btn2():
        global listBox2
        try:
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=cd)
            if MsgBox == "yes":
                selected_items = listBox2.selection()
                cur_item=listBox2.focus()
                k=listBox2.item(cur_item)["values"]
                mycursor.execute("DELETE FROM spd WHERE nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
                conn.commit()
                for selected_item in selected_items:
                    listBox2.delete(selected_item)
            else:
                pass
        except:
            pass

    def modi_btn(top):
        global listBox2
        selected_items1 = listBox2.selection()
        cur_item1=listBox2.focus()
        k=listBox2.item(cur_item1)["values"]
        if(len(k)==0):
            tk.messagebox.showerror("No Record Selected","Please select a record to Modify",parent=top)
        else:
            def onclosing():
                top.withdraw()
                
            global  fname2,fg1,Quantity2,Dimension2,Timetoeat1
            
            top.deiconify()
            top.geometry("500x550")
            
            fname2 = tk.StringVar()
            fg1 =tk.StringVar()
            Quantity2=tk.StringVar()
            Dimension2=tk.StringVar()
            Timetoeat1=tk.StringVar()

            Label2 = tk.Label(top)
            Label2.grid(row=0,column=1,pady=20,sticky="nw")
            Label2.configure(font="-family {Palatino Linotype} -size 18",bg='#d6e0f0',fg='black')
            Label2.configure(text="Record Entry")

            Label2 = tk.Label(top)
            Label2.grid(row=2,column=0,pady=20,sticky="w")
            Label2.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label2.configure(text="SR.NO")

            Label2_1 = tk.Label(top)
            Label2_1.grid(row=3,column=0,pady=20,sticky="w")
            Label2_1.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label2_1.configure(text="PRODUCT NAME")

            Label2_2 = tk.Label(top)
            Label2_2.grid(row=4,column=0,pady=20,sticky="w")
            Label2_2.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label2_2.configure(text="QUANTITY")
            
            Label3 = tk.Label(top)
            Label3.grid(row=5,column=0,pady=20,sticky="w")
            Label3.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label3.configure(text="MEASUREMENT")

            Label3_5 = tk.Label(top)
            Label3_5.grid(row=6,column=0,pady=20,sticky="w")
            Label3_5.configure(font="-family {Palatino Linotype} -size 12",bg='#d6e0f0',fg='black')
            Label3_5.configure(text="PRICE INVESTED")

            Entry1 = tk.Entry(top,width=28, textvariable=fname2)
            Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
            Entry1.configure(font="-family {Palatino Linotype} -size 12")

            Entry2 = tk.Entry(top,width=28, textvariable=fg1)
            Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
            Entry2.configure(font="-family {Palatino Linotype} -size 12")

            Entry3 = tk.Entry(top,width=28, textvariable=Quantity2)
            Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
            Entry3.configure(font="-family {Palatino Linotype} -size 12")

            Entry4 = tk.Entry(top,width=28, textvariable=Dimension2)
            Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
            Entry4.configure(font="-family {Palatino Linotype} -size 12")

            Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat1)
            Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
            Entry5.configure(font="-family {Palatino Linotype} -size 12")
            

            button6=HoverButton(top,text="SAVE",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=lambda:savemodi2(k,top))
            button6.grid(row=7,column=1,pady=20)

            button7=HoverButton(top,text="CANCEL",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("arial",10,"bold"),command=lambda:onclosing())
            button7.grid(row=7,column=0,pady=20)

            fname2.set(k[0])
            fg1.set(k[1])
            Quantity2.set(k[2])
            Dimension2.set(k[3])
            Timetoeat1.set(k[4])

    def savemodi2(k3,top2):
        global listBox2,fname2,fg1,Quantity2,Dimension2,Timetoeat1
        
        try:
            if (fname2.get() == "" or fg1.get() == "" or Quantity2.get() == "" or Dimension2.get() == "" or Timetoeat1.get() == ""):
                clear1()
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
            else:
                list1=[]
                if(fname2.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    list1.append(fname2.get())
                if (fg1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    list1.append(fg1.get())
                if (Quantity2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    num=Quantity2.get()
                    if(num.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                    else:
                        list1.append(num)
                if (Dimension2.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    list1.append(Dimension2.get())
                if (Timetoeat1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=top2)
                else:
                    num2=Timetoeat1.get()
                    list1.append(num2)
                
                mycursor.execute("select * from spd where nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                x1=[]
                for y in mycursor:
                    x1.append(y)
                if len(x1)==0:
                    mycursor.execute("UPDATE spd SET nameoffooditem2=?,foodgroup2=?,Quantity2=?,Dimensions2=?,Timetoeat2=? WHERE nameoffooditem2=? AND foodgroup2=? AND Quantity2=? AND Dimensions2=? AND Timetoeat2=?",(list1[0],list1[1],list1[2],list1[3],list1[4],k3[0],k3[1],k3[2],k3[3],k3[4]))
                    conn.commit()
                    top2.withdraw()
                else:
                    tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=top2)
                        
                listBox2.delete(*listBox2.get_children())
                mycursor.execute("select * from spd order by Timetoeat2 asc")
                for i in mycursor:
                    listBox2.insert("", "end", values=i)
        except:
            pass

    def Assign1(tp):
        try:
            global r1,r2,r4
            u=0
            if r1.get()=="" or r2.get()=="" or r4.get()=="":
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                d=["1","2","3","4","5","6","7","8","9","0"]
                if(r1.get()==""):
                    tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
                    u+=1
                else:
                    list1.append(r1.get())
                if (r2.get() == ""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                else:
                    num=r2.get()
                    c=0
                    if(len(num)==10):
                        for i in num:
                            if(i not in d and u==0):
                               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                               c+=1
                               u+=1
                               break
                        if(c==0):
                            list1.append(r2.get())
                    else:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                        
                if(r4.get()==""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
                else:
                    try:            
                        da=r4.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                        z=[]
                        mycursor.execute("select * from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(list1[0],list1[1],list1[2]))
                        for b in mycursor:
                            z.append(b)
                        if len(z)!=0:
                           tk.messagebox.showerror("Error","You have already assign diet at this date!",parent=tp)
                           list1.pop(2)
                        
                    except:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill all Date correctly!",parent=tp)

                mycursor.execute("select * from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
                r=[]
                for w in mycursor:
                    r.append(w)
                if len(r)>0:
                        
                    mycursor.execute("select * from spd")
                    m=[]
                    for j in mycursor:
                        m.append(j)
                    if len(m)>0:
                        for i in m:
                            mycursor.execute("INSERT INTO patientdiet VALUES(?,?,?,?,?,?,?,?)",(list1[0],list1[1],list1[2],i[0],i[1],i[2],i[3],i[4]))
                        mycursor.execute("select count(*) from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(list1[0],list1[1],list1[2]))
                        o=[]
                        for q in mycursor:
                            o.append(q)
                                
                        mycursor.execute("select weight from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
                        for t in mycursor:
                            o.append(t)
                            
                        mycursor.execute("INSERT INTO viewdiet VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],o[0][0],o[1][0]))
                        tk.messagebox.showinfo("DIET ASSIGNED","Patient Diet has been assigned successfully!",parent=tp)
                        conn.commit()
                        clear4()
                    else:
                        tk.messagebox.showerror("Error","There is no Diet to Assign!",parent=tp)
                else:
                    tk.messagebox.showerror("Error","Please Create Patient History First!",parent=tp)
        except:
            pass
       
       
    #########################################################################################common diet################################################################################################        
    def commondiet(top1):
        top1.config(bg="#d6e0f0")
        top1.iconbitmap(r"logo.ico")
        x, y = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.geometry("%dx%d+0+0" % (x, y))
        top1.deiconify()

        def onclosings():
            top1.withdraw()
            Add1.withdraw()
            Mdd.withdraw()
            sug.withdraw()
            Ass.withdraw()
            
        def onclosing():
            clear3()
            Add1.withdraw()

        def onclosings1():
            Mdd.withdraw()

        def onclosings2():
            sug.withdraw()

        def onclosing3():
            Ass.withdraw()
            
        global listBox1,r6,r7,r9,r10,r12,r11,option1

        Add1 = tk.Toplevel(CD)
        Add1.config(bg='#d6e0f0')
        Add1.title("DOCTOR CURE: ADD TO PATIENT DIET")
        Add1.withdraw()
        Add1.protocol("WM_DELETE_WINDOW",onclosing)

        Mdd = tk.Toplevel(CD)
        Mdd.title("DOCTOR CURE: MODIFY ENTRY")
        Mdd.withdraw()
        Mdd.protocol("WM_DELETE_WINDOW",onclosings1)

        sug = tk.Toplevel(CD)
        sug.title("DOCTOR CURE: FOOD ITEMS SUGGESTIONS")
        sug.withdraw()
        sug.protocol("WM_DELETE_WINDOW",onclosings2)

        Ass = tk.Toplevel(CD)
        Ass.title("DOCTOR CURE: Question")
        Ass.withdraw()
        Ass.protocol("WM_DELETE_WINDOW",onclosing3)
        
        l4=tk.Label(top1,text="RECOMMENDED DIET",font=("Palatino Linotype",35,"bold"),bg='#d6e0f0',fg='black')
        l4.place(relx=0.365, rely=0.019, height=79, width=525)

        option1 = tk.StringVar()
        TCombobox1 = tt.Combobox(top1, textvariable=option1,state='readonly')
        TCombobox1.bind("<<ComboboxSelected>>",getdiet1)
        value_list = ["On Dialysis","Not on Dialysis"]
        TCombobox1.place(relx=0.005, rely=0.114, relheight=0.054, relwidth=0.172)
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option1.set("Choose Patient Condition for Diet")
        
        cols = ("Name of food Items","Food Group","Quantity","Dimensions","Time to eat")
        
        listBox1 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse',height=25)
        listBox1.place(relx=0.005, rely=0.187, relheight=0.462, relwidth=0.750)
        for col in cols:
            listBox1.heading(col, text=col)

        vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox1.xview)
        vsb.place(relx=0.005, rely=0.649, relheight=0.025, relwidth=0.750)
        listBox1.configure(xscrollcommand=vsb.set)
            
        vsb = tt.Scrollbar(top1, orient="vertical", command=listBox1.yview)
        vsb.place(relx=0.755, rely=0.187, relheight=0.462, relwidth=0.012)
        listBox1.configure(yscrollcommand = vsb.set)

        l11=tk.Label(top1,text="FILL DETAILS TO ASSIGN DIET TO A PATIENT -:",font=("Palatino Linotype",18,"bold"),bg='#d6e0f0',fg='black')
        l11.place(relx=0.255, rely=0.700, relheight=0.031, relwidth=0.512)
        
        sbframe1=tk.Frame(top1)
        sbframe1.config(bg='#d6e0f0')
        sbframe1.place(relx=0.021, rely=0.777, height=40, width=2000)

        l8=tk.Label(sbframe1,text="NAME   :",font=("Palatino Linotype",16),bg='#d6e0f0',fg='black')
        l8.pack(side="left")
        r6=tk.StringVar()
        Entry2=tk.Entry(sbframe1,width=28,textvariable=r6)
        Entry2.pack(side="left",padx=20)
        Entry2.configure(background="white")
        Entry2.configure(disabledforeground="#a3a3a3")
        Entry2.configure(font="-family {Palatino Linotype} -size 15")
        Entry2.configure(foreground="#000000")
        Entry2.configure(highlightbackground="#d9d9d9")
        Entry2.configure(highlightcolor="black")
        Entry2.configure(insertbackground="black")
        Entry2.configure(selectbackground="#c4c4c4")
        Entry2.configure(selectforeground="black")

        l9=tk.Label(sbframe1,text="PHONE NO :",font=("Palatino Linotype",16),bg='#d6e0f0',fg='black')
        l9.pack(side="left")
        r11=tk.StringVar()
        Entry3=tk.Entry(sbframe1,width=28,textvariable=r11)
        Entry3.pack(side="left",padx=20)
        Entry3.configure(background="white")
        Entry3.configure(disabledforeground="#a3a3a3")
        Entry3.configure(font="-family {Palatino Linotype} -size 15")
        Entry3.configure(foreground="#000000")
        Entry3.configure(highlightbackground="#d9d9d9")
        Entry3.configure(highlightcolor="black")
        Entry3.configure(insertbackground="black")
        Entry3.configure(selectbackground="#c4c4c4")
        Entry3.configure(selectforeground="black")

        l10=tk.Label(sbframe1,text="DATE(dd/mm/yy):",font=("Palatino Linotype",16),bg='#d6e0f0',fg='black')
        l10.pack(side="left")
        r12=tk.StringVar()
        Entry4=tk.Entry(sbframe1,width=20,textvariable=r12)
        Entry4.pack(side="left",padx=20)
        Entry4.configure(background="white")
        Entry4.configure(disabledforeground="#a3a3a3")
        Entry4.configure(font="-family {Palatino Linotype} -size 15")
        Entry4.configure(foreground="#000000")
        Entry4.configure(highlightbackground="#d9d9d9")
        Entry4.configure(highlightcolor="black")
        Entry4.configure(insertbackground="black")
        Entry4.configure(selectbackground="#c4c4c4")
        Entry4.configure(selectforeground="black")

        
        sbframe=tk.Frame(top1)
        sbframe.config(bg='#d6e0f0')
        sbframe.place(relx=0.788, rely=0.190, relheight=0.547, relwidth=0.179)

        button1=HoverButton(sbframe,text="ADD FOOD ITEM",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",padx=94,pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:add_cmd_button(Add1))
        button1.pack(side="top",pady=10)

        button2=HoverButton(sbframe,text="DELETE",padx=110,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:delete_btn1())
        button2.pack(side="top",pady=10)

        button3=HoverButton(sbframe,text="MODIFY",padx=110,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:modi_cmd_button(Mdd))
        button3.pack(side="top",pady=10)

        button4=HoverButton(sbframe,text="ASSIGN DIET",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",padx=92,pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:Assign_cmd(Ass))
        button4.pack(side="top",pady=10)

        button6=HoverButton(sbframe,text="DIET SUGGESTIONS",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",padx=67,pady=10,bd=4,font=("Palatino Linotype",11,"bold"),command=lambda:Suggestions(sug))
        button6.pack(side="top",pady=10)
        
        try:
            t=mycursor.execute("select * from record").fetchall()[-1]
            r6.set(t[0])
            r12.set(t[3])
            r11.set(t[4])
        except:
            pass

        top1.protocol("WM_DELETE_WINDOW",onclosings)

    def add_cmd_button(top):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2
        def onclosing():
            clear3()
            top.withdraw()
        
        top.deiconify()
        top.geometry("460x600")

        fname4=tk.StringVar()
        fg=tk.StringVar()
        Quantity1=tk.StringVar()
        Dimension1=tk.StringVar()
        Timetoeat=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Diet Record Entry")

        Label1 = tk.Label(top)
        Label1.grid(row=2,column=0,pady=20,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Diet Type")

        Label2 = tk.Label(top)
        Label2.grid(row=3,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Name of food Items")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=4,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Food Group")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=5,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Quantity")
        
        Label3 = tk.Label(top)
        Label3.grid(row=6,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Dimensions")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=7,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Time to eat")

        option2 = tk.StringVar()
        TCombobox1 = tt.Combobox(top,width=28,textvariable=option2,state='readonly')
        value_list = ["On Dialysis","Not on Dialysis"]
        TCombobox1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option2.set("Choose Patient Condition for Diet")

        Entry1 = tk.Entry(top,width=28, textvariable=fname4)
        Entry1.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg)
        Entry2.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity1)
        Entry3.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension1)
        Entry4.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat)
        Entry5.grid(row=7,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=HoverButton(top,text="ADD",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=lambda:saveadd1(top))
        button6.grid(row=9,column=1,pady=20)

        button7=HoverButton(top,text="CANCEL",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=onclosing)
        button7.grid(row=9,column=0,pady=20)


    def saveadd1(tp):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2,option1,listbox1
        try:
       
            if (fname4.get() == "" or fg.get() == "" or Quantity1.get() == "" or Dimension1.get() == "" or Timetoeat.get() == ""):
                clear3()
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                if(fname4.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fname4.get())
                if (fg.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(fg.get())
                if (Quantity1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    f=[]
                    num2=Quantity1.get()
                    if(num2.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                    else:
                        list1.append(num2)
                if (Dimension1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(Dimension1.get())
                if (Timetoeat.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
                else:
                    list1.append(Timetoeat.get())
                    
                if(option2.get()=="On Dialysis"):
                    p=[]
                    mycursor.execute("select * from cm1 where nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                    for i in mycursor:
                        p.append(i)
                    if len(p)==0:
                        mycursor.execute("INSERT INTO cm1 VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                        conn.commit()
                        clear3()
                    else:
                        tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp)
                elif(option2.get()=="Not on Dialysis"):
                    p1=[]
                    mycursor.execute("select * from cm2 where nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                    for i in mycursor:
                        p1.append(i)
                    if len(p1)==0:
                        mycursor.execute("INSERT INTO cm2 VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                        conn.commit()
                        clear3()
                    else:
                       tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp)

                if(option1.get()=="On Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor.execute("select * from cm1 order by Timetoeat asc")
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                        
                elif(option1.get()=="Not on Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor.execute("select * from cm2 order by Timetoeat1 asc")
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                else:
                    pass

                tp.withdraw()
        except:
            pass
                
    def modi_cmd_button(top):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2,option1
        def onclosing():
            clear3()
            top.withdraw()

        selected_items = listBox1.selection()
        cur_item=listBox1.focus()
        k=listBox1.item(cur_item)["values"]

        if len(k)>0:
            top.deiconify()
            top.geometry("460x600")

            fname4=tk.StringVar()
            fg=tk.StringVar()
            Quantity1=tk.StringVar()
            Dimension1=tk.StringVar()
            Timetoeat=tk.StringVar()

            Label2 = tk.Label(top)
            Label2.grid(row=0,column=1,pady=20,sticky="nw")
            Label2.configure(font="-family {Palatino Linotype} -size 18")
            Label2.configure(text="Diet Record Entery")

            Label1 = tk.Label(top)
            Label1.grid(row=2,column=0,pady=20,sticky="w")
            Label1.configure(font="-family {Palatino Linotype} -size 12")
            Label1.configure(text="Diet Type")

            Label2 = tk.Label(top)
            Label2.grid(row=3,column=0,pady=20,sticky="w")
            Label2.configure(font="-family {Palatino Linotype} -size 12")
            Label2.configure(text="Name of food Items")

            Label2_1 = tk.Label(top)
            Label2_1.grid(row=4,column=0,pady=20,sticky="w")
            Label2_1.configure(font="-family {Palatino Linotype} -size 12")
            Label2_1.configure(text="Food Group")

            Label2_2 = tk.Label(top)
            Label2_2.grid(row=5,column=0,pady=20,sticky="w")
            Label2_2.configure(font="-family {Palatino Linotype} -size 12")
            Label2_2.configure(text="Quantity")
            
            Label3 = tk.Label(top)
            Label3.grid(row=6,column=0,pady=20,sticky="w")
            Label3.configure(font="-family {Palatino Linotype} -size 12")
            Label3.configure(text="Dimensions")

            Label3_5 = tk.Label(top)
            Label3_5.grid(row=7,column=0,pady=20,sticky="w")
            Label3_5.configure(font="-family {Palatino Linotype} -size 12")
            Label3_5.configure(text="Time to eat")

            option2 = tk.StringVar()
            TCombobox1 = tt.Combobox(top,width=28,textvariable=option2,state='readonly')
            value_list = ["On Dialysis","Not on Dialysis"]
            TCombobox1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
            TCombobox1.configure(values=value_list)
            TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
            option2.set("Choose Patient Condition for Diet")

            Entry1 = tk.Entry(top,width=28, textvariable=fname4)
            Entry1.grid(row=3,column=1,pady=20,padx=20,sticky="w")
            Entry1.configure(font="-family {Palatino Linotype} -size 12")
            
            Entry2 = tk.Entry(top,width=28, textvariable=fg)
            Entry2.grid(row=4,column=1,pady=20,padx=20,sticky="w")
            Entry2.configure(font="-family {Palatino Linotype} -size 12")

            Entry3 = tk.Entry(top,width=28, textvariable=Quantity1)
            Entry3.grid(row=5,column=1,pady=20,padx=20,sticky="w")
            Entry3.configure(font="-family {Palatino Linotype} -size 12")

            Entry4 = tk.Entry(top,width=28, textvariable=Dimension1)
            Entry4.grid(row=6,column=1,pady=20,padx=20,sticky="w")
            Entry4.configure(font="-family {Palatino Linotype} -size 12")
            
            Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat)
            Entry5.grid(row=7,column=1,pady=20,padx=20,sticky="w")
            Entry5.configure(font="-family {Palatino Linotype} -size 12")

            
            button6=HoverButton(top,text="MODIFY",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=lambda:savemodi1(top,k))
            button6.grid(row=9,column=1,pady=20)

            button7=HoverButton(top,text="CANCEL",padx=60,pady=10,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=4,font=("arial",10,"bold"),command=onclosing)
            button7.grid(row=9,column=0,pady=20)

            if option1.get()=="On Dialysis":
                option2.set("On Dialysis")
                fname4.set(k[0])
                fg.set(k[1])
                Quantity1.set(str(k[2]))
                Dimension1.set(k[3])
                Timetoeat.set(k[4])
            elif option1.get()=="Not on Dialysis":
                option2.set("Not on Dialysis")
                fname4.set(k[0])
                fg.set(k[1])
                Quantity1.set(str(k[2]))
                Dimension1.set(k[3])
                Timetoeat.set(k[4])
            else:
                pass
            
        else:
            tk.messagebox.showerror("Error","Please choose an item to Modify",parent=CD)

    def savemodi1(tp1,k1):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2,option1,listbox1
        
        try:
            if (fname4.get() == "" or fg.get() == "" or Quantity1.get() == "" or Dimension1.get() == "" or Timetoeat.get() == ""):
                messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
            else:
                list1=[]
                if(fname4.get()==""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(fname4.get())
                if (fg.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(fg.get())
                if (Quantity1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    f=[]
                    num2=Quantity1.get()
                    if(num2.isalpha()==True):
                        tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                    else:
                        list1.append(num2)
                if (Dimension1.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(Dimension1.get())
                if (Timetoeat.get() == ""):
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)
                else:
                    list1.append(Timetoeat.get())
                    
                if(option2.get()=="On Dialysis"):
                    p=[]
                    mycursor.execute("select * from cm1 where nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                    for i in mycursor:
                        p.append(i)
                    if len(p)==0:
                        mycursor.execute("UPDATE cm1 SET nameoffooditem=?,foodgroup=?,Quantity=?,Dimensions=?,Timetoeat=? WHERE nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(list1[0],list1[1],list1[2],list1[3],list1[4],k1[0],k1[1],k1[2],k1[3],k1[4]))
                        conn.commit()
                    else:
                        tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp1)
                    
                elif(option2.get()=="Not on Dialysis"):
                    p1=[]
                    mycursor.execute("select * from cm2 where nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(list1[0],list1[1],list1[2],list1[3],list1[4]))
                    for i in mycursor:
                        p1.append(i)
                    if len(p1)==0:
                        mycursor.execute("UPDATE cm2 SET nameoffooditem1=?,foodgroup1=?,Quantity1=?,Dimensions1=?,Timetoeat1=? WHERE nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(list1[0],list1[1],list1[2],list1[3],list1[4],k1[0],k1[1],k1[2],k1[3],k1[4]))
                        conn.commit()
                    else:
                        tk.messagebox.showerror("Error","You have already added this food item in this Diet",parent=tp1)
                else:
                    tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp1)

                if(option1.get()=="On Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor.execute("select * from cm1 order by Timetoeat asc")
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                        
                elif(option1.get()=="Not on Dialysis"):
                    listBox1.delete(*listBox1.get_children())
                    mycursor.execute("select * from cm2 order by Timetoeat1 asc")
                    for i in mycursor:
                        listBox1.insert("", "end", values=i)
                else:
                    pass

                tp1.withdraw()
        except:
            pass
        

    def delete_btn1():
        global listBox1,option1
        try:
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=CD)
            if MsgBox == "yes":
                selected_items = listBox1.selection()
                cur_item=listBox1.focus()
                k=listBox1.item(cur_item)["values"]
                
                if(option1.get()=="On Dialysis"):
                    mycursor.execute("select * from cm1 WHERE nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
                    a=[]
                    for i in mycursor:
                        a.append(i)
                    if len(a)>0:
                        mycursor.execute("DELETE FROM cm1 WHERE nameoffooditem=? AND foodgroup=? AND Quantity=? AND Dimensions=? AND Timetoeat=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
                        listBox1.delete(*listBox1.get_children())
                        mycursor.execute("select * from cm1 order by Timetoeat asc ")
                        for i in mycursor:
                            listBox1.insert("", "end", values=i)
                        conn.commit()
                        
                        
                    else:
                        tk.messagebox.showerror("Error","Choose Correct Patient Condition for Diet",parent=CD)
                        
                elif(option1.get()=="Not on Dialysis"):
                    mycursor.execute("select * from cm2 WHERE nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
                    a=[]
                    for i in mycursor:
                        a.append(i)
                    if len(a)>0:
                        mycursor.execute("DELETE FROM cm2 WHERE nameoffooditem1=? AND foodgroup1=? AND Quantity1=? AND Dimensions1=? AND Timetoeat1=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
                        listBox1.delete(*listBox1.get_children())
                        mycursor.execute("select * from cm2 order by Timetoeat1 asc ")
                        for i in mycursor:
                            listBox1.insert("", "end", values=i)
                        conn.commit()
                        
                       
                    else:
                        tk.messagebox.showerror("Error","Choose Correct Patient Condition for Diet",parent=CD)
                else:
                    
                    pass
                    
            else:
                
                pass
        except:
            pass


    def add_cmd_button(top):
        global fname4,fg,Quantity1,Dimension1,Timetoeat,option2
        def onclosing():
            clear3()
            top.withdraw()
        
        top.deiconify()
        top.geometry("460x600")

        fname4=tk.StringVar()
        fg=tk.StringVar()
        Quantity1=tk.StringVar()
        Dimension1=tk.StringVar()
        Timetoeat=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Record Entery")

        Label1 = tk.Label(top)
        Label1.grid(row=2,column=0,pady=20,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Diet Type")

        Label2 = tk.Label(top)
        Label2.grid(row=3,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Name of food Items")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=4,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Food Group")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=5,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Quantity")
        
        Label3 = tk.Label(top)
        Label3.grid(row=6,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Dimensions")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=7,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Time to eat")

        option2 = tk.StringVar()
        TCombobox1 = tt.Combobox(top,width=28,textvariable=option2,state='readonly')
        value_list = ["On Dialysis","Not on Dialysis"]
        TCombobox1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option2.set("Choose Patient Condition for Diet")

        Entry1 = tk.Entry(top,width=28, textvariable=fname4)
        Entry1.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry2 = tk.Entry(top,width=28, textvariable=fg)
        Entry2.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=Quantity1)
        Entry3.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=Dimension1)
        Entry4.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry5 = tk.Entry(top,width=28, textvariable=Timetoeat)
        Entry5.grid(row=7,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=HoverButton(top,text="ADD",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("Palatino Linotype",10,"bold"),command=lambda:saveadd1(top))
        button6.grid(row=9,column=1,pady=20)

        button7=HoverButton(top,text="CANCEL",padx=60,pady=10,bd=4,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",font=("Palatino Linotype",10,"bold"),command=onclosing)
        button7.grid(row=9,column=0,pady=20)

    def getdiet1(event):
        global listbox1,option1
        if(option1.get()=="On Dialysis"):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute("select * from cm1 order by Timetoeat asc")
            for i in mycursor:
                listBox1.insert("", "end", values=i)
                        
        elif(option1.get()=="Not on Dialysis"):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute("select * from cm2 order by Timetoeat1 asc")
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        else:
            pass

    def Suggestions(top):
        global option4,foodname1,foodname2,foodname3,foodname4,foodname5,foodname6,foodname7,foodname8,foodname9,foodname10,fgname1,fgname2,fgname3,fgname4,fgname5,fgname6,fgname7,fgname8,fgname9,fgname10
        top.geometry("480x600")
        top.deiconify()
        option4 = tk.StringVar()
        TCombobox1 = tt.Combobox(top,width=30,textvariable=option4,state='readonly')
        value_list = ["High Protein Food Items","Low Protein Food Items","High Potassium Food Items","Low Potassium Food Items","High Phosphorus Food Items","Low Phosphorus Food Items"]
        TCombobox1.grid(row=1,column=0,pady=20,padx=20,sticky="w")
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 12")
        option4.set("Select type of Food Items to search")
        button1=tk.Button(top,text="Search",bd=2,bg="sky blue",fg="black",font=("Palatino Linotype",10,"bold"),padx=20,command=lambda:getsuggestion())
        button1.grid(row=1,column=0,padx=300,sticky="w")

        Label1 = tk.Label(top)
        Label1.grid(row=2,column=0,padx=20,pady=10,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Food Items")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,padx=260,pady=10,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Food Group")

        foodname1=tk.StringVar()
        foodname2= tk.StringVar()
        foodname3= tk.StringVar()
        foodname4= tk.StringVar()
        foodname5= tk.StringVar()
        foodname6= tk.StringVar()
        foodname7= tk.StringVar()
        foodname8= tk.StringVar()
        foodname9= tk.StringVar()
        foodname10= tk.StringVar()
        fgname1= tk.StringVar()
        fgname2= tk.StringVar()
        fgname3= tk.StringVar()
        fgname4= tk.StringVar()
        fgname5= tk.StringVar()
        fgname6= tk.StringVar()
        fgname7= tk.StringVar()
        fgname8= tk.StringVar()
        fgname9= tk.StringVar()
        fgname10= tk.StringVar()
        

        Entry1 = tk.Entry(top,width=28, textvariable=foodname1,state="readonly",readonlybackground="white")
        Entry1.grid(row=3,column=0,padx=20,pady=10,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 10")

        Entry2 = tk.Entry(top,width=28, textvariable=fgname1,state="readonly",readonlybackground="white")
        Entry2.grid(row=3,column=0,padx=260,pady=10,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 10")

        Entry3 = tk.Entry(top,width=28, textvariable=foodname2,state="readonly",readonlybackground="white")
        Entry3.grid(row=4,column=0,padx=20,pady=10,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 10")

        Entry4 = tk.Entry(top,width=28, textvariable=fgname2,state="readonly",readonlybackground="white")
        Entry4.grid(row=4,column=0,padx=260,pady=10,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 10")

        Entry5 = tk.Entry(top,width=28, textvariable=foodname3,state="readonly",readonlybackground="white") 
        Entry5.grid(row=5,column=0,padx=20,pady=10,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 10")

        Entry6 = tk.Entry(top,width=28, textvariable=fgname3,state="readonly",readonlybackground="white")
        Entry6.grid(row=5,column=0,padx=260,pady=10,sticky="w")
        Entry6.configure(font="-family {Palatino Linotype} -size 10")

        Entry7 = tk.Entry(top,width=28, textvariable=foodname4,state="readonly",readonlybackground="white")
        Entry7.grid(row=6,column=0,padx=20,pady=10,sticky="w")
        Entry7.configure(font="-family {Palatino Linotype} -size 10")

        Entry8 = tk.Entry(top,width=28, textvariable=fgname4,state="readonly",readonlybackground="white")
        Entry8.grid(row=6,column=0,padx=260,pady=10,sticky="w")
        Entry8.configure(font="-family {Palatino Linotype} -size 10")

        Entry9 = tk.Entry(top,width=28, textvariable=foodname5,state="readonly",readonlybackground="white")
        Entry9.grid(row=7,column=0,padx=20,pady=10,sticky="w")
        Entry9.configure(font="-family {Palatino Linotype} -size 10")

        Entry10 = tk.Entry(top,width=28, textvariable=fgname5,state="readonly",readonlybackground="white")
        Entry10.grid(row=7,column=0,padx=260,pady=10,sticky="w")
        Entry10.configure(font="-family {Palatino Linotype} -size 10")

        Entry11 = tk.Entry(top,width=28, textvariable=foodname6,state="readonly",readonlybackground="white")
        Entry11.grid(row=8,column=0,padx=20,pady=10,sticky="w")
        Entry11.configure(font="-family {Palatino Linotype} -size 10")

        Entry12 = tk.Entry(top,width=28, textvariable=fgname6,state="readonly",readonlybackground="white")
        Entry12.grid(row=8,column=0,padx=260,pady=10,sticky="w")
        Entry12.configure(font="-family {Palatino Linotype} -size 10")

        Entry13 = tk.Entry(top,width=28, textvariable=foodname7,state="readonly",readonlybackground="white")
        Entry13.grid(row=9,column=0,padx=20,pady=10,sticky="w")
        Entry13.configure(font="-family {Palatino Linotype} -size 10")

        Entry14 = tk.Entry(top,width=28, textvariable=fgname7,state="readonly",readonlybackground="white")
        Entry14.grid(row=9,column=0,padx=260,pady=10,sticky="w")
        Entry14.configure(font="-family {Palatino Linotype} -size 10")

        Entry15 = tk.Entry(top,width=28, textvariable=foodname8,state="readonly",readonlybackground="white")
        Entry15.grid(row=10,column=0,padx=20,pady=10,sticky="w")
        Entry15.configure(font="-family {Palatino Linotype} -size 10")

        Entry16 = tk.Entry(top,width=28, textvariable=fgname8,state="readonly",readonlybackground="white")
        Entry16.grid(row=10,column=0,padx=260,pady=10,sticky="w")
        Entry16.configure(font="-family {Palatino Linotype} -size 10")

        Entry17 = tk.Entry(top,width=28, textvariable=foodname9,state="readonly",readonlybackground="white")
        Entry17.grid(row=11,column=0,padx=20,pady=10,sticky="w")
        Entry17.configure(font="-family {Palatino Linotype} -size 10")

        Entry18 = tk.Entry(top,width=28, textvariable=fgname9,state="readonly",readonlybackground="white")
        Entry18.grid(row=11,column=0,padx=260,pady=10,sticky="w")
        Entry18.configure(font="-family {Palatino Linotype} -size 10")

        Entry19 = tk.Entry(top,width=28, textvariable=foodname10,state="readonly",readonlybackground="white")
        Entry19.grid(row=12,column=0,padx=20,pady=10,sticky="w")
        Entry19.configure(font="-family {Palatino Linotype} -size 10")

        Entry20 = tk.Entry(top,width=28, textvariable=fgname10,state="readonly",readonlybackground="white")
        Entry20.grid(row=12,column=0,padx=260,pady=10,sticky="w")
        Entry20.configure(font="-family {Palatino Linotype} -size 10")

    def Assign_cmd(top):
        top.deiconify()
        top.geometry("270x110")
        Label1 = tk.Label(top)
        Label1.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        Label1.configure(font="-family {Palatino Linotype} -size 12")
        Label1.configure(text="Which diet you want to Assign ?")
        
        button1=tt.Button(top,text="On Dialysis",command=lambda:ondass(top))
        button1.grid(row=1,column=0,pady=20,padx=40,sticky="w")
        
        button2=tt.Button(top,text="Not on Dialysis",command=lambda:nondass(top))
        button2.grid(row=1,columnspan=1,padx=120,pady=20,sticky="w")

    def ondass(tp):
        try:
            tp.withdraw()
            global r6,r11,r12,listbox1
            u=0

            if r6.get()=="" or r11.get()=="" or r12.get()=="":
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                d=["1","2","3","4","5","6","7","8","9","0"]
                if(r6.get()==""):
                    tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
                    u+=1
                else:
                    list1.append(r6.get())
                if (r11.get() == ""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                else:
                    num=r11.get()
                    c=0
                    if(len(num)==10):
                        for i in num:
                            if(i not in d and u==0):
                               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                               c+=1
                               u+=1
                               break
                        if(c==0):
                            list1.append(r11.get())
                    else:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                        
                if(r12.get()==""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
                else:
                    try:
                        da=r12.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                        z=[]
                        mycursor.execute("select * from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(list1[0],list1[1],list1[2]))
                        for b in mycursor:
                            z.append(b)
                        if len(z)!=0:
                           tk.messagebox.showerror("Error","You have already assign diet at this date!",parent=tp)
                           list1.pop(2)
                        
                    except:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)

                mycursor.execute("select * from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
                r=[]
                for w in mycursor:
                    r.append(w)
                if len(r)>0:
                    mycursor.execute("select * from cm1")
                    m=[]
                    for j in mycursor:
                        m.append(j)
                    if len(m)>0:
                        for i in m:
                            mycursor.execute("INSERT INTO patientdiet VALUES(?,?,?,?,?,?,?,?)",(list1[0],list1[1],list1[2],i[0],i[1],i[2],i[3],i[4]))

                        mycursor.execute("select count(*) from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(list1[0],list1[1],list1[2]))
                        o=[]
                        for q in mycursor:
                            o.append(q)
                            
                        mycursor.execute("select weight from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
                        for t in mycursor:
                            o.append(t)
                        
                        mycursor.execute("INSERT INTO viewdiet VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],o[0][0],o[1][0]))
                        conn.commit()
                        tk.messagebox.showinfo("DIET ASSIGNED","Patient Diet has been assigned successfully!",parent=tp)
                        clear2()
                    else:
                        tk.messagebox.showerror("Error","There is no Diet to Assign!",parent=tp)
                else:
                    tk.messagebox.showerror("Error","Please Create Patient History First!",parent=tp)
        except:
            pass
            
       
            
    def nondass(tp):
        try:
            tp.withdraw()
            global r6,r11,r12,listbox1
            u=0
            if r6.get()=="" or r11.get()=="" or r12.get()=="":
                tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
            else:
                list1=[]
                d=["1","2","3","4","5","6","7","8","9","0"]
                if(r6.get()==""):
                    tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
                    u+=1
                else:
                    list1.append(r6.get())
                if (r11.get() == ""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                else:
                    num=r11.get()
                    c=0
                    if(len(num)==10):
                        for i in num:
                            if(i not in d and u==0):
                               tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                               c+=1
                               u+=1
                               break
                        if(c==0):
                            list1.append(r11.get())
                    else:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                        
                if(r12.get()==""):
                    if(u==0):
                        u+=1
                        tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
                else:
                    try:
                        da=r12.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                        z=[]
                        mycursor.execute("select * from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(list1[0],list1[1],list1[2]))
                        for b in mycursor:
                            z.append(b)
                        if len(z)!=0:
                           tk.messagebox.showerror("Error","You have already assign diet at this date!",parent=tp)
                           list1.pop(2)
                    except:
                        if(u==0):
                            u+=1
                            tk.messagebox.showerror("Error","Please fill all Date correctly!",parent=tp)
                mycursor.execute("select * from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
                r=[]
                for w in mycursor:
                    r.append(w)
                if len(r)>0:
                    mycursor.execute("select * from cm2")
                    m=[]
                    for j in mycursor:
                        m.append(j)
                    if len(m)>0:
                        for i in m:
                            mycursor.execute("INSERT INTO patientdiet VALUES(?,?,?,?,?,?,?,?)",(list1[0],list1[1],list1[2],i[0],i[1],i[2],i[3],i[4]))
                            
                        mycursor.execute("select count(*) from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(list1[0],list1[1],list1[2]))
                        o=[]
                        for q in mycursor:
                            o.append(q)
                            
                        mycursor.execute("select weight from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
                        for t in mycursor:
                            o.append(t)
                        
                        mycursor.execute("INSERT INTO viewdiet VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],o[0][0],o[1][0]))
                        tk.messagebox.showinfo("DIET ASSIGNED","Patient Diet has been assigned successfully!",parent=tp)
                        conn.commit()
                        clear2()
                    else:
                        tk.messagebox.showerror("Error","There is no Diet to Assign!",parent=tp)
                else:
                    tk.messagebox.showerror("Error","Please Create Patient History First!",parent=tp)
                
        except:
            pass
        
    ################################################################Suggesstion###################################################################################
    def getsuggestion():
        global option4,foodname1,foodname2,foodname3,foodname4,foodname5,foodname6,foodname7,foodname8,foodname9,foodname10,fgname1,fgname2,fgname3,fgname4,fgname5,fgname6,fgname7,fgname8,fgname9,fgname10
        op=option4.get()
        if(op=="High Protein Food Items"):
            foodname1.set("Cocoa")
            foodname2.set("Wheat")
            foodname3.set("Peanuts")
            foodname4.set("Soya")
            foodname5.set("Yeast")
            foodname6.set("Flounder")
            foodname7.set("Prawns")
            foodname8.set("Gelatin")
            foodname9.set("Chic. Leg Roasted")
            foodname10.set("Cheddar")
            fgname1.set("Beverages")
            fgname2.set("Grains")
            fgname3.set("Nuts")
            fgname4.set("Cereal Grains")
            fgname5.set("Cakes&Biscuits")
            fgname6.set("Meat&Fish")
            fgname7.set("Meat&Fish")
            fgname8.set("Meat&Fish")
            fgname9.set("Meat&Fish")
            fgname10.set("Milk Products")

        elif(op=="Low Protein Food Items"):
            foodname1.set("Cream")
            foodname2.set("Yogurt")
            foodname3.set("Spring Roll")
            foodname4.set("Irish Stew")
            foodname5.set("Watermelon")
            foodname6.set("Apple")
            foodname7.set("Jelly")
            foodname8.set("Porridge")
            foodname9.set("Beer")
            foodname10.set("Tea")
            fgname1.set("Milk Products")
            fgname2.set("Milk Products")
            fgname3.set("Meat&Fish")
            fgname4.set("Meat&Fish")
            fgname5.set("Fruits")
            fgname6.set("Fruits")
            fgname7.set("Desserts")
            fgname8.set("Desserts")
            fgname9.set("Beverages")
            fgname10.set("Beverages")

        elif(op=="High Potassium Food Items"):
            foodname1.set("Avocado(1/4 whole)")
            foodname2.set("Dates(5 whole)")
            foodname3.set("Artichoke")
            foodname4.set("Brussels Sprouts")
            foodname5.set("Chocolate(1.5-2ounces)")
            foodname6.set("Yogurt")
            foodname7.set("Peanut Butter(2tbs.)")
            foodname8.set("Grapefruit Juice")
            foodname9.set("White Mushrooms(1/2cup)")
            foodname10.set("Pomegranate")
            fgname1.set("Fruits")
            fgname2.set("Fruits")
            fgname3.set("Vegetables")
            fgname4.set("Vegetables")
            fgname5.set("Sweets")
            fgname6.set("Milk Products")
            fgname7.set("Fats&Oils")
            fgname8.set("Fruits")
            fgname9.set("Vegetables")
            fgname10.set("Fruits")

        elif(op=="Low Potassium Food Items"):
            foodname1.set("Blueberries")
            foodname2.set("Mandarin Oranges")
            foodname3.set("Cauliflower")
            foodname4.set("Cucumber")
            foodname5.set("Noodles")
            foodname6.set("Cake")
            foodname7.set("Rice")
            foodname8.set("Apple")
            foodname9.set("Radish")
            foodname10.set("Watermelon")
            fgname1.set("Fruits")
            fgname2.set("Fruits")
            fgname3.set("Vegetables")
            fgname4.set("Vegetables")
            fgname5.set("Grains")
            fgname6.set("Sweets")
            fgname7.set("Grains")
            fgname8.set("Fruits")
            fgname9.set("Vegetables")
            fgname10.set("Fruits")

        elif(op=="High Phosphorus Food Items"):
            foodname1.set("Cheese")
            foodname2.set("Custard")
            foodname3.set("Nuts")
            foodname4.set("Kidey Beans")
            foodname5.set("Chick Peas")
            foodname6.set("Bran cereals")
            foodname7.set("Beer")
            foodname8.set("Cocoa")
            foodname9.set("Chocolte Drinks")
            foodname10.set("Pudding")
            fgname1.set("Milk Products")
            fgname2.set("Milk Products")
            fgname3.set("Nuts&Seeds")
            fgname4.set("Beans")
            fgname5.set("Beans")
            fgname6.set("Whole Grains")
            fgname7.set("Beverages")
            fgname8.set("Beverages")
            fgname9.set("Beverages")
            fgname10.set("Milk Products")

        elif(op=="Low Phosphorus Food Items"):
            foodname1.set("Apricot")
            foodname2.set("Tangerine")
            foodname3.set("Peaches")
            foodname4.set("Carrots")
            foodname5.set("Broccoli")
            foodname6.set("Popcorn")
            foodname7.set("Rice Cereal")
            foodname8.set("Fruit Juices")
            foodname9.set("Sodas")
            foodname10.set("Strawberries")
            fgname1.set("Fruits")
            fgname2.set("Fruits")
            fgname3.set("Fruits")
            fgname4.set("Vegetables")
            fgname5.set("Vegetables")
            fgname6.set("Cereal Grain")
            fgname7.set("Cereal Grain")
            fgname8.set("Beverages")
            fgname9.set("Beverages")
            fgname10.set("Fruits")

        else:
            pass

    ####################################################################View Diet#####################################################################################################
    def viewdiet(top1):
        top1.iconbitmap(r"logo.ico")
        top1.config(bg='#d6e0f0')
        x, y = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.geometry("%dx%d+0+0" % (x, y))
        top1.deiconify()

        def onclosing():
            vd1.withdraw()

        vd1 = tk.Toplevel(VD)
        vd1.title("STOCK UP: VIED DIET")
        vd1.withdraw()
        vd1.protocol("WM_DELETE_WINDOW",onclosing)

        def onclosings():
            top1.withdraw()
            vd1.withdraw()
        
        global listBox3,option5,r5
        
        r5 = tk.StringVar()
        option5 = tk.StringVar()
        Label1 = tk.Label(top1)
        Label1.place(relx=0.320, rely=0.019, height=79, width=492)
        Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold",bg='#d6e0f0',fg='black')
        Label1.configure(text='''VIEW PATIENT DIET''')

        Label2 = tk.Label(top1)
        Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.241)
        Label2.configure(font="-family {Palatino Linotype} -size 17",bg='#d6e0f0',fg='black')
        Label2.configure(text='''TYPE TO SEARCH -:''')

        Entry1 = tk.Entry(top1,textvariable=r5)
        Entry1.place(relx=0.195, rely=0.125, height=40, relwidth=0.241)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="-family {Palatino Linotype} -size 15")
        Entry1.configure(foreground="#000000")
        Entry1.configure(highlightbackground="#d9d9d9")
        Entry1.configure(highlightcolor="black")
        Entry1.configure(insertbackground="black")
        Entry1.configure(selectbackground="#c4c4c4")
        Entry1.configure(selectforeground="black")

        TCombobox1 = tt.Combobox(top1, textvariable=option5,state='readonly')
        value_list = ['All Records',"Name","Phone No.","Date"]
        TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
        TCombobox1.configure(values=value_list)
        TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
        option5.set("Choose Category to Search")

        
        cols = ("Name of Patient","Patient Phone No.","Date Diet Given","No of food items","Weight of Patient(Kg)")
        listBox3 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox3.heading(col, text=col)
        listBox3.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
        vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox3.xview)
        vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
        listBox3.configure(xscrollcommand=vsb.set)

        vsb = tt.Scrollbar(top1, orient="vertical", command=listBox3.yview)
        vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
        listBox3.configure(yscrollcommand=vsb.set)


        Button2 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:search_btn_view())
        Button2.place(relx=0.200, rely=0.867, height=60, width=250)
        Button2.configure(font="-family {Palatino Linotype} -size 16")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''SEARCH''')

        Button3 =HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:patient_view_diet(vd1))
        Button3.place(relx=0.415, rely=0.867, height=60, width=250)
        Button3.configure(font="-family {Palatino Linotype} -size 16")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightcolor="black")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(pady="0")
        Button3.configure(text='''VIEW DIET''')

        Button4 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:delete_btn3(top1))
        Button4.place(relx=0.627, rely=0.867, height=60, width=250)
        Button4.configure(font="-family {Palatino Linotype} -size 14")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text='''DELETE''')

        listBox3.delete(*listBox3.get_children())
        mycursor.execute("select * from viewdiet order by pdate1 desc")
        for i in mycursor:
            listBox3.insert("", "end", values=i)

        top1.protocol("WM_DELETE_WINDOW",onclosings)

    def search_btn_view():
        global listBox3,option5,r5
        _entry = r5.get()
        _option = option5.get()

        if (_option == 'Name'):
            listBox3.delete(*listBox3.get_children())
            mycursor.execute('select * from viewdiet where pname1 like "%{0}%" order by pdate1 desc'.format(_entry))
            for i in mycursor:
                listBox3.insert("", "end", values=i)
                
        elif (_option == 'Phone No.'):
            listBox3.delete(*listBox3.get_children())
            mycursor.execute('select * from viewdiet where pphno1 like "%{0}%" order by pdate1 desc'.format(_entry))
            for i in mycursor:
                listBox3.insert("", "end", values=i)
                
        elif (_option == "Date"):
            listBox3.delete(*listBox3.get_children())
            mycursor.execute("select * from viewdiet where pdate1 like '%{0}%' order by pdate1 desc".format(_entry))
            for i in mycursor:
                listBox3.insert("", "end", values=i)
       
        elif (_option == "All Records"):
            listBox3.delete(*listBox3.get_children())
            mycursor.execute("select * from viewdiet order by pdate1 desc")
            for i in mycursor:
                listBox3.insert("", "end", values=i)     
        else:
            option3.set("Choose Category Correctly!")


    def delete_btn3(tp):
        global listBox3
        try:
            MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=tp)
            if MsgBox == "yes":
                selected_items = listBox3.selection()
                cur_item=listBox3.focus()
                k=listBox3.item(cur_item)["values"]
                mycursor.execute("DELETE FROM viewdiet WHERE pname1=? AND pphno1=? AND pdate1=? AND nooffooditem=? AND weight=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
                mycursor.execute("DELETE FROM patientdiet WHERE pname=? AND pphno=? AND pdate=?",(str(k[0]),str(k[1]),str(k[2])))
                conn.commit()
                for selected_item in selected_items:
                    listBox3.delete(selected_item)
            else:
                pass
        except:
            pass

    def patient_view_diet(top1):
        top1.iconbitmap(r"logo.ico")
        x, y = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.geometry("%dx%d+0+0" % (x, y))
        
        
        global listBox3,listBox4,g1,g2,g3,g4

        def onclosings():
            top1.withdraw()

        selected_items = listBox3.selection()
        cur_item=listBox3.focus()
        k=listBox3.item(cur_item)["values"]

        if(len(k)==0):
            messagebox.showerror("No Record Selected","Please select a record to View",parent=top1)
        else:
            top1.deiconify()
            Label1 = tk.Label(top1)
            Label1.place(relx=0.375, rely=0.009, height=79, width=492)
            Label1.configure(font="-family {Palatino Linotype} -size 28 -weight bold")
            Label1.configure(text='''DIET GIVEN''')

            Label2 = tk.Label(top1)
            Label2.place(relx=0.001, rely=0.095, height=40, relwidth=0.241)
            Label2.configure(font="-family {Palatino Linotype} -size 17")
            Label2.configure(text='''NAME -:''')
            
            g1 = tk.StringVar()
            Entry1 = tk.Entry(top1,textvariable=g1,state="readonly")
            Entry1.place(relx=0.155, rely=0.095, height=30, relwidth=0.241)
            Entry1.configure(background="white")
            Entry1.configure(disabledforeground="#a3a3a3")
            Entry1.configure(font="-family {Palatino Linotype} -size 15")
            Entry1.configure(foreground="#000000")
            Entry1.configure(highlightbackground="#d9d9d9")
            Entry1.configure(highlightcolor="black")
            Entry1.configure(insertbackground="black")
            Entry1.configure(selectbackground="#c4c4c4")
            Entry1.configure(selectforeground="black")

            Label4 = tk.Label(top1)
            Label4.place(relx=0.001, rely=0.145, height=40, relwidth=0.241)
            Label4.configure(font="-family {Palatino Linotype} -size 17")
            Label4.configure(text='''DATE -:''')
            
            g2 = tk.StringVar()
            Entry4 = tk.Entry(top1,textvariable=g2,state="readonly")
            Entry4.place(relx=0.155, rely=0.145, height=30, relwidth=0.141)
            Entry4.configure(background="white")
            Entry4.configure(disabledforeground="#a3a3a3")
            Entry4.configure(font="-family {Palatino Linotype} -size 15")
            Entry4.configure(foreground="#000000")
            Entry4.configure(highlightbackground="#d9d9d9")
            Entry4.configure(highlightcolor="black")
            Entry4.configure(insertbackground="black")
            Entry4.configure(selectbackground="#c4c4c4")
            Entry4.configure(selectforeground="black")

            Label3 = tk.Label(top1)
            Label3.place(relx=0.548, rely=0.085, relheight=0.069, relwidth=0.269)
            Label3.configure(font="-family {Palatino Linotype} -size 17")
            Label3.configure(text='''PH.NO -:''')

            g3 = tk.StringVar()
            Entry2 = tk.Entry(top1,textvariable=g3,state="readonly")
            Entry2.place(relx=0.735, rely=0.095, height=30, relwidth=0.169)
            Entry2.configure(background="white")
            Entry2.configure(disabledforeground="#a3a3a3")
            Entry2.configure(font="-family {Palatino Linotype} -size 15")
            Entry2.configure(foreground="#000000")
            Entry2.configure(highlightbackground="#d9d9d9")
            Entry2.configure(highlightcolor="black")
            Entry2.configure(insertbackground="black")
            Entry2.configure(selectbackground="#c4c4c4")
            Entry2.configure(selectforeground="black")

            Label5 = tk.Label(top1)
            Label5.place(relx=0.548, rely=0.134, relheight=0.069, relwidth=0.269)
            Label5.configure(font="-family {Palatino Linotype} -size 17")
            Label5.configure(text='''WEIGHT(kg) -:''')

            g4 = tk.StringVar()
            Entry3 = tk.Entry(top1,textvariable=g4,state="readonly")
            Entry3.place(relx=0.735, rely=0.145, height=30, relwidth=0.169)
            Entry3.configure(background="white")
            Entry3.configure(disabledforeground="#a3a3a3")
            Entry3.configure(font="-family {Palatino Linotype} -size 15")
            Entry3.configure(foreground="#000000")
            Entry3.configure(highlightbackground="#d9d9d9")
            Entry3.configure(highlightcolor="black")
            Entry3.configure(insertbackground="black")
            Entry3.configure(selectbackground="#c4c4c4")
            Entry3.configure(selectforeground="black")
            
            cols = ("Name of food Items","Food Group","Quantity","Dimensions","Time to eat")
            listBox4 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
            for col in cols:
                listBox4.heading(col, text=col)
            listBox4.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
            
            vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox4.xview)
            vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
            listBox4.configure(xscrollcommand=vsb.set)

            vsb = tt.Scrollbar(top1, orient="vertical", command=listBox4.yview)
            vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
            listBox4.configure(yscrollcommand=vsb.set)

            Label6 = tk.Label(top1)
            Label6.place(relx=0.046, rely=0.825, relheight=0.035, relwidth=0.896)
            Label6.configure(font="-family {Palatino Linotype} -size 17")
            Label6.configure(text='''Note - This Diet is now non-modifiable you have to delete and assign the diet again for any changes.''')


            g1.set(k[0])
            g2.set(k[1])
            g3.set(k[2])
            g4.set(k[3])

            mycursor.execute("select nameoffooditem3,foodgroup3,Quantity3,Dimensions3,Timetoeat3 from patientdiet WHERE pname=? AND pphno=? AND pdate=?",(k[0],k[1],k[2]))

            for i in mycursor:
                listBox4.insert("", "end", values=i)

            top1.protocol("WM_DELETE_WINDOW",onclosings)

        
            
    
    toplevel1(root)

#===========================================================================patient Yoga==================================================================================

import tkinter as tk
import tkinter.ttk as tt
from tkinter import messagebox
import datetime as dt

from sqlite3 import *    
conn = connect('my_database.db')
mycursor = conn.cursor()

cb,cb1,cb2,Cb2,cb3,Cb3,cb4,Cb4,cb5,Cb5,cb6,Cb6,cb7,Cb7,cb8,Cb8,cb9,Cb9,cb10,Cb10,cb11,Cb11,cb12,Cb12,cb13,Cb13,cb14,Cb14,cb15,Cb15,cb16,Cb16,cb17,Cb17,cb18,Cb18,cb19,Cb19,cb20,Cb20,cb21,Cb21,cb22,Cb22,cb23,Cb23,cb24,Cb24,cb25,Cb25,cb26,Cb26,cb27,Cb27,cb28,Cb28,cb29,Cb29,cb30,Cb30,cb31,Cb31,cb32,Cb32,cb33,Cb33,cb34,Cb34,cb35,Cb35,cb36,Cb36,cb37,Cb37,cb38,Cb38,cb39,Cb39,cb40,Cb40=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
t1,t2,t3,listBox5,option6,k1,k,w=None,None,None,None,None,None,None,None



def yogahere():
  try:
    mycursor.execute('select * from yoga')
  except(OperationalError):
    mycursor.execute("create table yoga(patientname text,patientphno int, patientdate date,imagepath text)")

  try:
    mycursor.execute('select * from yoga1')
  except(OperationalError):
    mycursor.execute("create table yoga1(patientname1 text,patientphno1 int, patientdate1 date,noofimage text)")

  def menueyoga(t):
        def onclosing():
            t.destroy()
            
        
        
        #Menue Bar
        menubar=tk.Menu(t)
        t.config(menu=menubar)
        #Sub Menue
        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=submenu)
        submenu.add_command(label="Exit",command=onclosing)

        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit",menu=submenu)
        submenu.add_command(label="Dashboard",command=session)
        #submenu.add_command(label="Patient History",command=Record)
        #submenu.add_command(label="Patient Medicine",command=medicine)
        #submenu.add_command(label="Patient Diet",command=lambda:diet)
        submenu.add_command(label="Patient Yoga",command=lambda:toplevel1_yoga(t))
        def aboutus():
            messagebox.showinfo("About Doctor Cure ","This application helps a doctor to Manage Patient History,Diet and Medicine which doctor needs to diagnose patient easily.\n\nCreated By Binary Beast using Python",parent=t)

        submenu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help",menu=submenu)
        submenu.add_command(label="About Us",command=aboutus)

        t.protocol("WM_DELETE_WINDOW",onclosing)

  def view_yoga(tops,top1):
    global listBox5,k,w

    def onclosings():
      top1.destroy()
      
    top1.deiconify()
    top1.resizable(0,0)
    
    Label1 = tk.Label(tops)
    Label1.grid(row=0,column=0)
    Label1.configure(font="-family {Palatino Linotype} -size 18")
    Label1.configure(text="VIEW ASSIGNED YOGA")
    
    for g in range(len(w)):
      Img=tk.Label(tops,image=w[g])
      Img.grid(row=g+1,column=0,pady=10)
      
    top1.protocol("WM_DELETE_WINDOW",onclosings)

 

  root1=Toplevel(screen8)
  x, y = root1.winfo_screenwidth(), root1.winfo_screenheight()
  root1.geometry("%dx%d+0+0" % (x, y))
  root1.title("DOCTOR CURE : PATIENT YOGA")
  root1.iconbitmap(r"logo.ico")

  def toplevel1_yoga(top1):
      global listBox5,option6,k1,k   
      def onclosing():
         pic.withdraw()
         
      def onclosing1():
         ypic.withdraw()

      def onclosings():
         top1.withdraw()
         pic.withdraw()

      pic = tk.Toplevel(root1)
      pic.title("DOCTOR CURE: ASSIGN YOGA")
      pic.withdraw()
      pic.protocol("WM_DELETE_WINDOW",onclosing)

      x, y = pic.winfo_screenwidth(), pic.winfo_screenheight()
      pic.geometry("%dx%d+0+0" % (x, y))

      def _on_mousewheel(event):
          canvas.yview_scroll(int(-1*(event.delta/120)),"units")

      container = tt.Frame(pic)
      canvas = tk.Canvas(container,height=y,width=x-25)
      scrollbar = tt.Scrollbar(container, orient="vertical", command=canvas.yview)
      scrollbar1 = tt.Scrollbar(container, orient="horizontal", command=canvas.xview)
      canvas.bind_all("<MouseWheel>",_on_mousewheel)
      
      top = tt.Frame(canvas)

      top.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

      canvas.create_window((0, 0), window=top, anchor="nw")

      canvas.configure(yscrollcommand=scrollbar.set)
      canvas.configure(xscrollcommand=scrollbar1.set)

      container.pack()
      canvas.pack(side="left", fill="both", expand=True)
      scrollbar.pack(side="right", fill="y")
      scrollbar1.place(relx=0.001, rely=0.977, relheight=0.025, relwidth=0.989)

      img1 =tk.PhotoImage(file="images/1.png")
      img2 =tk.PhotoImage(file="images/2.png")
      img3 =tk.PhotoImage(file="images/3.png")
      img4 =tk.PhotoImage(file="images/4.png")
      img5 =tk.PhotoImage(file="images/5.png")
      img6 =tk.PhotoImage(file="images/6.png")
      img7 =tk.PhotoImage(file="images/7.png")
      img8 =tk.PhotoImage(file="images/8.png")
      img9 =tk.PhotoImage(file="images/9.png")
      img10 =tk.PhotoImage(file="images/10.png")
      img11 =tk.PhotoImage(file="images/11.png")
      img12 =tk.PhotoImage(file="images/12.png")
      img13 =tk.PhotoImage(file="images/13.png")
      img14 =tk.PhotoImage(file="images/14.png")
      img15 =tk.PhotoImage(file="images/15.png")
      img16 =tk.PhotoImage(file="images/16.png")
      img17 =tk.PhotoImage(file="images/17.png")
      img18 =tk.PhotoImage(file="images/18.png")
      img19 =tk.PhotoImage(file="images/19.png")
      img20 =tk.PhotoImage(file="images/20.png")
      img21 =tk.PhotoImage(file="images/21.png")
      img22 =tk.PhotoImage(file="images/22.png")
      img23 =tk.PhotoImage(file="images/23.png")
      img24 =tk.PhotoImage(file="images/24.png")
      img25 =tk.PhotoImage(file="images/25.png")
      img26 =tk.PhotoImage(file="images/26.png")
      img27 =tk.PhotoImage(file="images/27.png")
      img28 =tk.PhotoImage(file="images/28.png")
      img29 =tk.PhotoImage(file="images/29.png")
      img30 =tk.PhotoImage(file="images/30.png")
      img31 =tk.PhotoImage(file="images/31.png")
      img32 =tk.PhotoImage(file="images/32.png")
      img33 =tk.PhotoImage(file="images/33.png")
      img34 =tk.PhotoImage(file="images/34.png")
      img35 =tk.PhotoImage(file="images/35.png")
      img36 =tk.PhotoImage(file="images/36.png")
      img37 =tk.PhotoImage(file="images/37.png")
      img38 =tk.PhotoImage(file="images/38.png")
      img39 =tk.PhotoImage(file="images/39.png")
      img40 =tk.PhotoImage(file="images/40.png")

      menueyoga(top1)
      k1 = tk.StringVar()
      option6 = tk.StringVar()
      Label1 = tk.Label(top1)
      Label1.place(relx=0.375, rely=0.019, height=79, width=492)
      Label1.configure(font="-family {Palatino Linotype} -size 26 -weight bold")
      Label1.configure(text='''YOGA ASSIGNED PATIENTS''')

      Label2 = tk.Label(top1)
      Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.241)
      Label2.configure(font="-family {Palatino Linotype} -size 17")
      Label2.configure(text='''TYPE TO SEARCH -:''')

      Entry1 = tk.Entry(top1,textvariable=k1)
      Entry1.place(relx=0.195, rely=0.125, height=40, relwidth=0.241)
      Entry1.configure(background="white")
      Entry1.configure(disabledforeground="#a3a3a3")
      Entry1.configure(font="-family {Palatino Linotype} -size 15")
      Entry1.configure(foreground="#000000")
      Entry1.configure(highlightbackground="#d9d9d9")
      Entry1.configure(highlightcolor="black")
      Entry1.configure(insertbackground="black")
      Entry1.configure(selectbackground="#c4c4c4")
      Entry1.configure(selectforeground="black")

      TCombobox1 = tt.Combobox(top1, textvariable=option6,state='readonly')
      value_list = ['All Records','Name of Patient','Phone Number','Date']
      TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
      TCombobox1.configure(values=value_list)
      TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
      option6.set("Choose Category to Search")

      
      cols = ('Name of Patient','Phone Number','Date of yoga assigning','No of Yoga Assigned')
      listBox5 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
      for col in cols:
          listBox5.heading(col, text=col)
      listBox5.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
      vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox5.xview)
      vsb.place(relx=0.046, rely=0.799, relheight=0.025, relwidth=0.896)
      listBox5.configure(xscrollcommand=vsb.set)

      vsb = tt.Scrollbar(top1, orient="vertical", command=listBox5.yview)
      vsb.place(relx=0.942, rely=0.218, relheight=0.580, relwidth=0.012)
      listBox5.configure(yscrollcommand=vsb.set)

      Button2 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:search_yoga_btn())
      Button2.place(relx=0.100, rely=0.867, height=60, width=250)
      Button2.configure(font="-family {Palatino Linotype} -size 16")
      Button2.configure(foreground="#000000")
      Button2.configure(highlightbackground="#d9d9d9")
      Button2.configure(highlightcolor="black")
      Button2.configure(pady="0")
      Button2.configure(text='''SEARCH''')

      Button3 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:yoga(top,pic,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24,img25,img26,img27,img28,img29,img30,img31,img32,img33,img34,img35,img36,img37,img38,img39,img40))
      Button3.place(relx=0.315, rely=0.867, height=60, width=250)
      Button3.configure(font="-family {Palatino Linotype} -size 16")
      Button3.configure(foreground="#000000")
      Button3.configure(highlightcolor="black")
      Button3.configure(highlightbackground="#d9d9d9")
      Button3.configure(pady="0")
      Button3.configure(text='''ASSIGN YOGA''')

      Button4 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:delete_yoga_patient(top1))
      Button4.place(relx=0.527, rely=0.867, height=60, width=250)
      Button4.configure(font="-family {Palatino Linotype} -size 14")
      Button4.configure(foreground="#000000")
      Button4.configure(highlightbackground="#d9d9d9")
      Button4.configure(highlightcolor="black")
      Button4.configure(pady="0")
      Button4.configure(text='''DELETE YOGA PATIENT''')

      selected_items = listBox5.selection()
      cur_item=listBox5.focus()
      k=listBox5.item(cur_item)["values"]

      Button5 = HoverButton(top1,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,command=lambda:yoga_view_btn())
      Button5.place(relx=0.745, rely=0.867, height=60, width=250)
      Button5.configure(font="-family {Palatino Linotype} -size 14")
      Button5.configure(foreground="#000000")
      Button5.configure(highlightbackground="#d9d9d9")
      Button5.configure(highlightcolor="black")
      Button5.configure(pady="0")
      Button5.configure(text='''VIEW ASSIGNED YOGA''')

      listBox5.delete(*listBox5.get_children())
      mycursor.execute("select * from yoga1 order by patientdate1 desc")
      for i in mycursor:
          listBox5.insert("", "end", values=i)

      top1.protocol("WM_DELETE_WINDOW",onclosings)

  def yoga(top,top1,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24,img25,img26,img27,img28,img29,img30,img31,img32,img33,img34,img35,img36,img37,img38,img39,img40):
     top1.deiconify()
     global t1,t2,t3
     global cb,cb1,cb2,Cb2,cb3,Cb3,cb4,Cb4,cb5,Cb5,cb6,Cb6,cb7,Cb7,cb8,Cb8,cb9,Cb9,cb10,Cb10,cb11,Cb11,cb12,Cb12,cb13,Cb13,cb14,Cb14,cb15,Cb15,cb16,Cb16,cb17,Cb17,cb18,Cb18,cb19,Cb19,cb20,Cb20,cb21,Cb21,cb22,Cb22,cb23,Cb23,cb24,Cb24,cb25,Cb25,cb26,Cb26,cb27,Cb27,cb28,Cb28,cb29,Cb29,cb30,Cb30,cb31,Cb31,cb32,Cb32,cb33,Cb33,cb34,Cb34,cb35,Cb35,cb36,Cb36,cb37,Cb37,cb38,Cb38,cb39,Cb39,cb40,Cb40
     def onclosing():
        top1.withdraw()

     Label1 = tk.Label(top)
     Label1.grid(row=0,column=2,pady=20)
     Label1.configure(font="-family {Palatino Linotype} -size 32 -weight bold")
     Label1.configure(text='''PATIENT YOGA AND EXERCISE''')
     
     cb1=tk.BooleanVar()
     cb = tk.Checkbutton(top,var=cb1)
     cb.grid(row=1,column=0,sticky="w")
     Img1=tk.Label(top,image=img1)
     Img1.grid(row=1,column=1,padx=20,pady=20,sticky="e")
     
     cb2=tk.BooleanVar()
     Cb2= tk.Checkbutton(top,var=cb2)
     Cb2.grid(row=1,column=2,columnspan=1,padx=20,sticky="w")
     Img2=tk.Label(top,image=img2)
     Img2.grid(row=1,column=2,sticky="w",padx=70)

     cb3=tk.BooleanVar()
     Cb3= tk.Checkbutton(top,var=cb3)
     Cb3.grid(row=1,column=2,padx=410,sticky="w")
     Img3=tk.Label(top,image=img3)
     Img3.grid(row=1,column=2,padx=80,sticky="e")

     cb4=tk.BooleanVar()
     Cb4 = tk.Checkbutton(top,var=cb4)
     Cb4.grid(row=1,column=3,sticky="w")
     Img4=tk.Label(top,image=img4)
     Img4.grid(row=1,column=3,padx=40,sticky="e")

     cb5=tk.BooleanVar()
     Cb5 = tk.Checkbutton(top,var=cb5)
     Cb5.grid(row=2,column=0,sticky="w")
     Img5=tk.Label(top,image=img5)
     Img5.grid(row=2,column=1,padx=20,pady=20,sticky="e")
     
     cb6=tk.BooleanVar()
     Cb6= tk.Checkbutton(top,var=cb6)
     Cb6.grid(row=2,column=2,columnspan=1,padx=20,sticky="w")
     Img6=tk.Label(top,image=img6)
     Img6.grid(row=2,column=2,sticky="w",padx=70)

     cb7=tk.BooleanVar()
     Cb7= tk.Checkbutton(top,var=cb7)
     Cb7.grid(row=2,column=2,padx=410,sticky="w")
     Img7=tk.Label(top,image=img7)
     Img7.grid(row=2,column=2,padx=80,sticky="e")

     cb8=tk.BooleanVar()
     Cb8 = tk.Checkbutton(top,var=cb8)
     Cb8.grid(row=2,column=3,sticky="w")
     Img8=tk.Label(top,image=img8)
     Img8.grid(row=2,column=3,padx=40,sticky="e")

     cb9=tk.BooleanVar()
     Cb9= tk.Checkbutton(top,var=cb9)
     Cb9.grid(row=3,column=0,sticky="w")
     Img9=tk.Label(top,image=img9)
     Img9.grid(row=3,column=1,padx=20,pady=20,sticky="e")
     
     cb10=tk.BooleanVar()
     Cb10= tk.Checkbutton(top,var=cb10)
     Cb10.grid(row=3,column=2,columnspan=1,padx=20,sticky="w")
     Img10=tk.Label(top,image=img10)
     Img10.grid(row=3,column=2,sticky="w",padx=70)

     cb11=tk.BooleanVar()
     Cb11 = tk.Checkbutton(top,var=cb11)
     Cb11.grid(row=3,column=2,padx=410,sticky="w")
     Img11=tk.Label(top,image=img11)
     Img11.grid(row=3,column=2,padx=80,sticky="e")

     cb12=tk.BooleanVar()
     Cb12= tk.Checkbutton(top,var=cb12)
     Cb12.grid(row=3,column=3,sticky="w")
     Img12=tk.Label(top,image=img12)
     Img12.grid(row=3,column=3,padx=40,sticky="e")

     cb13=tk.BooleanVar()
     Cb13 = tk.Checkbutton(top,var=cb13)
     Cb13.grid(row=4,column=0,sticky="w")
     Img13=tk.Label(top,image=img13)
     Img13.grid(row=4,column=1,padx=20,pady=20,sticky="e")
     
     cb14=tk.BooleanVar()
     Cb14 = tk.Checkbutton(top,var=cb14)
     Cb14.grid(row=4,column=2,columnspan=1,padx=20,sticky="w")
     Img14=tk.Label(top,image=img14)
     Img14.grid(row=4,column=2,sticky="w",padx=70)

     cb15=tk.BooleanVar()
     Cb15 = tk.Checkbutton(top,var=cb15)
     Cb15.grid(row=4,column=2,padx=410,sticky="w")
     Img15=tk.Label(top,image=img15)
     Img15.grid(row=4,column=2,padx=80,sticky="e")

     cb16=tk.BooleanVar()
     Cb16= tk.Checkbutton(top,var=cb16)
     Cb16.grid(row=4,column=3,sticky="w")
     Img16=tk.Label(top,image=img16)
     Img16.grid(row=4,column=3,padx=40,sticky="e")

     cb17=tk.BooleanVar()
     Cb17= tk.Checkbutton(top,var=cb17)
     Cb17.grid(row=5,column=0,sticky="w")
     Img17=tk.Label(top,image=img17)
     Img17.grid(row=5,column=1,padx=20,pady=20,sticky="e")
     
     cb18=tk.BooleanVar()
     Cb18 = tk.Checkbutton(top,var=cb18)
     Cb18.grid(row=5,column=2,columnspan=1,padx=20,sticky="w")
     Img18=tk.Label(top,image=img18)
     Img18.grid(row=5,column=2,sticky="w",padx=70)

     cb19=tk.BooleanVar()
     Cb19 = tk.Checkbutton(top,var=cb19)
     Cb19.grid(row=5,column=2,padx=410,sticky="w")
     Img19=tk.Label(top,image=img19)
     Img19.grid(row=5,column=2,padx=80,sticky="e")

     cb20=tk.BooleanVar()
     Cb20= tk.Checkbutton(top,var=cb20)
     Cb20.grid(row=5,column=3,sticky="w")
     Img20=tk.Label(top,image=img20)
     Img20.grid(row=5,column=3,padx=40,sticky="e")

     cb21=tk.BooleanVar()
     Cb21= tk.Checkbutton(top,var=cb21)
     Cb21.grid(row=6,column=0,sticky="w")
     Img21=tk.Label(top,image=img21)
     Img21.grid(row=6,column=1,padx=20,pady=20,sticky="e")
     
     cb22=tk.BooleanVar()
     Cb22= tk.Checkbutton(top,var=cb22)
     Cb22.grid(row=6,column=2,columnspan=1,padx=20,sticky="w")
     Img22=tk.Label(top,image=img22)
     Img22.grid(row=6,column=2,sticky="w",padx=70)

     cb23=tk.BooleanVar()
     Cb23= tk.Checkbutton(top,var=cb23)
     Cb23.grid(row=6,column=2,padx=410,sticky="w")
     Img23=tk.Label(top,image=img23)
     Img23.grid(row=6,column=2,padx=80,sticky="e")

     cb24=tk.BooleanVar()
     Cb24= tk.Checkbutton(top,var=cb24)
     Cb24.grid(row=6,column=3,sticky="w")
     Img24=tk.Label(top,image=img24)
     Img24.grid(row=6,column=3,padx=40,sticky="e")

     cb25=tk.BooleanVar()
     Cb25= tk.Checkbutton(top,var=cb25)
     Cb25.grid(row=7,column=0,sticky="w")
     Img25=tk.Label(top,image=img25)
     Img25.grid(row=7,column=1,padx=20,pady=20,sticky="e")
     
     cb26=tk.BooleanVar()
     Cb26= tk.Checkbutton(top,var=cb26)
     Cb26.grid(row=7,column=2,columnspan=1,padx=20,sticky="w")
     Img26=tk.Label(top,image=img26)
     Img26.grid(row=7,column=2,sticky="w",padx=70)

     cb27=tk.BooleanVar()
     Cb27= tk.Checkbutton(top,var=cb27)
     Cb27.grid(row=7,column=2,padx=410,sticky="w")
     Img27=tk.Label(top,image=img27)
     Img27.grid(row=7,column=2,padx=80,sticky="e")

     cb28=tk.BooleanVar()
     Cb28= tk.Checkbutton(top,var=cb28)
     Cb28.grid(row=7,column=3,sticky="w")
     Img28=tk.Label(top,image=img28)
     Img28.grid(row=7,column=3,padx=40,sticky="e")

     cb29=tk.BooleanVar()
     Cb29= tk.Checkbutton(top,var=cb29)
     Cb29.grid(row=8,column=0,sticky="w")
     Img29=tk.Label(top,image=img29)
     Img29.grid(row=8,column=1,padx=20,pady=20,sticky="e")
     
     cb30=tk.BooleanVar()
     Cb30= tk.Checkbutton(top,var=cb30)
     Cb30.grid(row=8,column=2,columnspan=1,padx=20,sticky="w")
     Img30=tk.Label(top,image=img30)
     Img30.grid(row=8,column=2,sticky="w",padx=70)

     cb31=tk.BooleanVar()
     Cb31= tk.Checkbutton(top,var=cb31)
     Cb31.grid(row=8,column=2,padx=410,sticky="w")
     Img31=tk.Label(top,image=img31)
     Img31.grid(row=8,column=2,padx=80,sticky="e")

     cb32=tk.BooleanVar()
     Cb32= tk.Checkbutton(top,var=cb32)
     Cb32.grid(row=8,column=3,sticky="w")
     Img32=tk.Label(top,image=img32)
     Img32.grid(row=8,column=3,padx=40,sticky="e")

     cb33=tk.BooleanVar()
     Cb33= tk.Checkbutton(top,var=cb33)
     Cb33.grid(row=9,column=0,sticky="w")
     Img33=tk.Label(top,image=img33)
     Img33.grid(row=9,column=1,padx=20,pady=20,sticky="e")
     
     cb34=tk.BooleanVar()
     Cb34= tk.Checkbutton(top,var=cb34)
     Cb34.grid(row=9,column=2,columnspan=1,padx=20,sticky="w")
     Img34=tk.Label(top,image=img34)
     Img34.grid(row=9,column=2,sticky="w",padx=70)

     cb35=tk.BooleanVar()
     Cb35= tk.Checkbutton(top,var=cb35)
     Cb35.grid(row=9,column=2,padx=410,sticky="w")
     Img35=tk.Label(top,image=img35)
     Img35.grid(row=9,column=2,padx=80,sticky="e")

     cb36=tk.BooleanVar()
     Cb36= tk.Checkbutton(top,var=cb36)
     Cb36.grid(row=9,column=3,sticky="w")
     Img36=tk.Label(top,image=img36)
     Img36.grid(row=9,column=3,padx=40,sticky="e")

     cb37=tk.BooleanVar()
     Cb37= tk.Checkbutton(top,var=cb37)
     Cb37.grid(row=10,column=0,sticky="w")
     Img37=tk.Label(top,image=img37)
     Img37.grid(row=10,column=1,padx=20,pady=20,sticky="e")
     
     cb38=tk.BooleanVar()
     Cb38 = tk.Checkbutton(top,var=cb38)
     Cb38.grid(row=10,column=2,columnspan=1,padx=20,sticky="w")
     Img38=tk.Label(top,image=img38)
     Img38.grid(row=10,column=2,sticky="w",padx=70)

     cb39=tk.BooleanVar()
     Cb39= tk.Checkbutton(top,var=cb39)
     Cb39.grid(row=10,column=2,padx=410,sticky="w")
     Img39=tk.Label(top,image=img39)
     Img39.grid(row=10,column=2,padx=80,sticky="e")

     cb40=tk.BooleanVar()
     Cb40= tk.Checkbutton(top,var=cb40)
     Cb40.grid(row=10,column=3,sticky="w")
     Img40=tk.Label(top,image=img40)
     Img40.grid(row=10,column=3,padx=40,sticky="e")

     l1=tk.Label(top,text="Name :")
     l1.configure(font="-family {Palatino Linotype} -size 15 -weight bold")
     l1.grid(row=11,column=1,pady=20,sticky="w")

     t1=tk.StringVar()
     e1=tk.Entry(top,width=26,textvariable=t1)
     e1.configure(font="-family {Palatino Linotype} -size 15")
     e1.grid(row=11,column=1,pady=20,sticky="e")

     l2=tk.Label(top,text="Phone No :")
     l2.configure(font="-family {Palatino Linotype} -size 15 -weight bold")
     l2.grid(row=11,column=2,padx=20,pady=20,sticky="w")

     t2=tk.StringVar()
     e2=tk.Entry(top,width=24,textvariable=t2)
     e2.configure(font="-family {Palatino Linotype} -size 15")
     e2.grid(row=11,column=2,padx=140,pady=20,sticky="w")

     l3=tk.Label(top,text="Date(dd/mm/yy):")
     l3.configure(font="-family {Palatino Linotype} -size 15 -weight bold")
     l3.grid(row=11,column=2,columnspan=2,padx=420,pady=20,sticky="w")

     t3=tk.StringVar()
     e3=tk.Entry(top,width=26,textvariable=t3)
     e3.configure(font="-family {Palatino Linotype} -size 15")
     e3.grid(row=11,column=2,columnspan=1,pady=20,sticky="e")

     b1=tk.Button(top,text="Submit",bg="#61c0bf",command=lambda:f1(top),padx=80)
     b1.configure(font="-family {Palatino Linotype} -size 15")
     b1.grid(row=11,column=3,pady=20)

     try:   
         w=mycursor.execute("select * from record").fetchall()[-1]
         t1.set(w[0])
         t2.set(w[4])
         t3.set(w[3])
     except:
         pass

  def clears():
     global t1,t2,t3
     t1.set("")
     t2.set("")
     t3.set("")

  def f1(tp):
     try:
       global t1,t2,t3,listBox5
       q1=[]
       d1=[cb1,cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9,cb10,cb11,cb12,cb13,cb14,cb15,cb16,cb17,cb18,cb19,cb20,cb21,cb22,cb23,cb24,cb25,cb26,cb27,cb28,cb29,cb30,cb31,cb32,cb33,cb34,cb35,cb36,cb37,cb38,cb39,cb40]
       for i in range(1,41):
          if d1[i-1].get()==True:
             q1.append("images/"+str(i)+".png")
          else:
             pass
       u=0
       if(t1.get()=="" or t2.get()=="" or t3.get()==""):
           tk.messagebox.showerror("Error","Please fill all the fields correctly!",parent=tp)
       else:
           list1=[]
           d=["1","2","3","4","5","6","7","8","9","0"]
           if(t1.get()==""):
               tk.messagebox.showerror("Error","Please fill name correctly!",parent=tp)
               u+=1
           else:
               list1.append(t1.get())
           if (t2.get() == ""):
               if(u==0):
                   u+=1
                   tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
           else:
               num=t2.get()
               c=0
               if(len(num)==10):
                   for i in num:
                       if(i not in d and u==0):
                          tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp)
                          c+=1
                          u+=1
                          break
                   if(c==0):
                       list1.append(t2.get())
               else:
                   if(u==0):
                       u+=1
                       tk.messagebox.showerror("Error","Please fill Phone Number correctly!",parent=tp) 
                   
           if(t3.get()==""):
               if(u==0):
                   u+=1
                   tk.messagebox.showerror("Error","Please fill Date correctly!",parent=tp)
           else:
               try:
                   da=t3.get()
                   d1=dt.datetime.strptime(da,"%d/%m/%y")
                   list1.append(da)
                   
                   z=[]
                   mycursor.execute("select * from yoga WHERE patientname=? AND patientphno=? AND patientdate=?",(list1[0],list1[1],list1[2]))
                   for b in mycursor:
                       z.append(b)
                   if len(z)!=0:
                      tk.messagebox.showerror("Error","You have already assign yoga at this date!",parent=tp)
                      list1.pop(2)
                   
               except:
                   if(u==0):
                       u+=1
                       tk.messagebox.showerror("Error","Please fill the Date correctly!",parent=tp)
           mycursor.execute("select * from record WHERE name=? AND phn_no=? AND date=?",(list1[0],list1[1],list1[2]))
           r=[]
           for w in mycursor:
              r.append(w)

           if len(r)>0:    
              if len(q1)>0:
                 for i in range(len(q1)):
                    mycursor.execute("INSERT INTO yoga VALUES(?,?,?,?)",(list1[0],list1[1],list1[2],q1[i]))
                 mycursor.execute("INSERT INTO yoga1 VALUES(?,?,?,?)",(list1[0],list1[1],list1[2],len(q1)))
                 tk.messagebox.showinfo("YOGA ASSIGNED","Patient Yoga has been assigned successfully!",parent=tp)
                 conn.commit()
                 clears()
                 listBox5.delete(*listBox5.get_children())
                 mycursor.execute("select * from yoga1 order by patientdate1 desc")
                 for i in mycursor:
                     listBox5.insert("", "end", values=i)
              else:
                 tk.messagebox.showerror("Error","No yoga images Assigned!",parent=tp)
           else:
              tk.messagebox.showerror("Error","Please create Patient History First!",parent=tp)
     except:
       pass
    
  def delete_yoga_patient(tp):
      global listBox5
      try:
          MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning",parent=tp)
          if MsgBox == "yes":
              selected_items = listBox5.selection()
              cur_item=listBox5.focus()
              k=listBox5.item(cur_item)["values"]
              mycursor.execute("DELETE FROM yoga WHERE patientname=? AND patientphno=? AND patientdate=? ",(str(k[0]),str(k[1]),str(k[2])))
              mycursor.execute("DELETE FROM yoga1 WHERE patientname1=? AND patientphno1=? AND patientdate1=? AND noofimage=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3])))
              conn.commit()
              for selected_item in selected_items:
                  listBox5.delete(selected_item)
          else:
              pass
      except:
          pass
      
  def search_yoga_btn():
      global listBox5,option6,k1
      _entry = k1.get()
      _option = option6.get()

      if (_option == 'Name of Patient'):
          listBox5.delete(*listBox5.get_children())
          mycursor.execute('select * from yoga1 where patientname1 like "%{0}%" order by patientdate1 desc'.format(_entry))
          for i in mycursor:
              listBox5.insert("", "end", values=i)
              
      elif (_option == 'Phone Number'):
          listBox5.delete(*listBox5.get_children())
          mycursor.execute('select * from yoga1 where patientphno1 like "%{0}%" order by patientdate1 desc'.format(_entry))
          for i in mycursor:
              listBox5.insert("", "end", values=i)
              
      elif (_option == 'Date'):
          listBox5.delete(*listBox5.get_children())
          mycursor.execute("select * from yoga1 where patientdate1 like '%{0}%' order by patientdate1 desc".format(_entry))
          for i in mycursor:
              listBox5.insert("", "end", values=i)
     
      elif (_option == "All Records"):
          listBox5.delete(*listBox5.get_children())
          mycursor.execute("select * from yoga1 order by patientdate1 desc")
          for i in mycursor:
              listBox5.insert("", "end", values=i)     
      else:
          option6.set("Choose Category Correctly!")
          
  def yoga_view_btn():
    global listBox5,k,w

    def onclosing1():
         ypic.withdraw()
         
    ypic = tk.Toplevel(root1)
    ypic.title("DOCTOR CURE: VIEW YOGA")
    ypic.withdraw()
    ypic.protocol("WM_DELETE_WINDOW",onclosing1)
    ypic.geometry("350x500+200+200")

    container1 = tt.Frame(ypic)
    canvas1 = tk.Canvas(container1,height=500,width=324)
    scrollbar3 = tt.Scrollbar(container1, orient="vertical", command=canvas1.yview)
    top2 = tt.Frame(canvas1)

    top2.bind("<Configure>",lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))



    canvas1.create_window((0, 0), window=top2, anchor="nw")

    canvas1.configure(yscrollcommand=scrollbar3.set)
    

    container1.pack()
    canvas1.pack(side="left", fill="both", expand=True)
    scrollbar3.pack(side="right", fill="y")
    
    selected_items = listBox5.selection()
    cur_item=listBox5.focus()
    k=listBox5.item(cur_item)["values"]
    
    if len(k)>0:
        mycursor.execute("select imagepath from yoga WHERE patientname=? AND patientphno=? AND patientdate=? ",(k[0],k[1],k[2]))
        x=[]
        w=[]
        for i in mycursor:
          x.append(i)
          
        for g in x:
          img =tk.PhotoImage(file=g[0])
          w.append(img)
          
        view_yoga(top2,ypic)
    else:
      tk.messagebox.showerror("Error","Please choose a record to View",parent=root1)
      
   
  toplevel1_yoga(root1)

#=============================print============================================    
import os
import tkinter as tk
import tkinter.ttk as tt
from tkinter import messagebox
import datetime as dt
from shutil import copy2
from tkinter import filedialog
import webbrowser
from tabulate import tabulate
from fpdf import FPDF

from sqlite3 import *    
conn = connect('my_database.db')
mycursor = conn.cursor()
x1,x2,x3,x4,fp=None,None,None,None,None

def web2():
    webbrowser.open("www.gmail.com")

def web1():
    webbrowser.open("https://web.whatsapp.com/")

def print_btn(screen9,photo,photo1):
    global x1,x2,x3,x4,fp

    def onclosings():
        screen9.withdraw()
    
    
    screen9.deiconify()

    x1=tk.StringVar()
    x2=tk.StringVar()
    x3=tk.StringVar()
    x4=tk.StringVar()
    
    Label2 = tk.Label(screen9)
    Label2.grid(row=0,column=0,padx=120,pady=20,sticky="nw")
    Label2.configure(font="-family {Palatino Linotype} -size 18")
    Label2.configure(text="Print Record Entry")
 
    Label2 = tk.Label(screen9)
    Label2.grid(row=2,column=0,pady=20,sticky="w")
    Label2.configure(font="-family {Palatino Linotype} -size 12")
    Label2.configure(text="Name of the Patient :")

    Label2_1 = tk.Label(screen9)
    Label2_1.grid(row=3,column=0,pady=20,sticky="w")
    Label2_1.configure(font="-family {Palatino Linotype} -size 12")
    Label2_1.configure(text="Phone Number :")

    Label2_2 = tk.Label(screen9)
    Label2_2.grid(row=4,column=0,pady=20,sticky="w")
    Label2_2.configure(font="-family {Palatino Linotype} -size 12")
    Label2_2.configure(text="Date :")

    Entry1 = tk.Entry(screen9,width=28,textvariable=x1)
    Entry1.grid(row=2,column=0,columnspan=1,padx=200,pady=20,sticky="w")
    Entry1.configure(font="-family {Palatino Linotype} -size 12")

    Entry2 = tk.Entry(screen9,width=28,textvariable=x2)
    Entry2.grid(row=3,column=0,pady=20,padx=200,sticky="w")
    Entry2.configure(font="-family {Palatino Linotype} -size 12")

    Entry3 = tk.Entry(screen9,width=28,textvariable=x3)
    Entry3.grid(row=4,column=0,pady=20,padx=200,sticky="w")
    Entry3.configure(font="-family {Palatino Linotype} -size 12")


    button61=tk.Button(screen9,text="Cancel",padx=60,pady=10,bd=4,font=("arial",10,"bold"),bg="#61c0bf",command=lambda:onclosings())
    button61.grid(row=7,column=0,pady=20 )

    button71=tk.Button(screen9,text="Print",padx=60,pady=10,bd=4,font=("arial",10,"bold"),bg="#61c0bf",command=lambda:print_record(screen9))
    button71.grid(row=7,column=0,padx=10,pady=20,sticky="w")

    Label2_3 = tk.Label(screen9)
    Label2_3.grid(row=9,column=0,pady=20,sticky="w")
    Label2_3.configure(font="-family {Palatino Linotype} -size 12")
    Label2_3.configure(text="Share file on :")

    b6=tt.Button(screen9,command=web1)
    b6.grid(row=9,column=0,padx=110,pady=10,sticky="w")
    b6.configure(image=photo)

    b7=tt.Button(screen9,command=web2)
    b7.grid(row=9,column=0,padx=160,pady=10,sticky="w")
    b7.configure(image=photo1)
    
    try:
        w=mycursor.execute("select * from record").fetchall()[-1]
        x1.set(w[0])
        x2.set(w[4])
        x3.set(w[3])
    except:
        pass
    screen9.protocol("WM_DELETE_WINDOW",onclosings)


def print_record(tp):
    try:
        global x1,x2,x3,x4,fp,filename

        def onclosings():
            os.remove("LastRecord.pdf")
            tp.destroy()
        
        if str(x1.get())=="" or str(x2.get())=="" or str(x3.get())=="":
            messagebox.showerror("Error","Please fill all the details correctly!",parent=tp)
        else:
            files=[("Pdf Document","*.pdf")]
            fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf",parent=tp)
            fw= open("temp.txt","w")
            fw1= open("temp1.txt","w")

            if fp is None:
                messagebox.showerror("Invalid file Name","Please enter valid Name",parent=tp)
            else:
                l1=[]
            h=()
            st="\n"
            b1=mycursor.execute("select fname,lname,contact_no from credentials").fetchall()[-1]
            b2=mycursor.execute("select age from record where name=? AND date=? AND phn_no=?",(x1.get(),x3.get(),x2.get())).fetchall()
           
            st+="Doctor's Details\n"
            st+="Doctor's Name: "+b1[0]+" "+b1[1]+"\n"
            st+="Doctor's Ph.no: "+b1[2]+"\n\n"
            st+="Patient Details\n"
            st+="Patient Name: "+x1.get()+"\n"
            st+="Patient Age: "+str(b2[0][0])+"\n"
            st+="Patient Ph.no: "+x2.get()+"\n"
            st+="Patient Diagnosis Date: "+x3.get()+"\n\n"
            st+="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPATIENT MEDICINE\n\n"
            mycursor.execute("select medicine,dosage,timings,days from medicine_table where name=? AND phn_no=? AND date=?",(str(x1.get()),str(x2.get()),str(x3.get())))
            
            for i in mycursor:
                m=list(i)
                d=[]
                for j in m:
                    r=j.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
                
            head=["NAME OF\nTHE MEDICINE","DOSAGE TAKEN","TIME TO\nEAT","NO. OF\nDAYS"]
            st+=tabulate(l1,headers=head,tablefmt="grid")
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=9)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(-1,5,txt = x, ln = 1)
            f.close()
            l2=[]

            s1="\n"
            s1+="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPATIENT DIET\n\n"
            mycursor.execute("select nameoffooditem3,foodgroup3,Quantity3,Dimensions3,Timetoeat3 from patientdiet where pname=? AND pphno=? AND pdate=?",(str(x1.get()),str(x2.get()),str(x3.get())))
            for i in mycursor:
                m=list(i)
                d=[]
                for j in m:
                    
                    r=(str(j)).replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l2.append(h)
            head1=["NAME OF\nFOOD ITEMS","FOOD GROUP","QUANTTY","DIMENSIONS","TIME TO\nEAT"]
            s1+=tabulate(l2,headers=head1,tablefmt="grid")
            fw1.write(s1)
            fw1.close()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=9)
            pdf.set_margins(0,0,0)
            f1=open("temp1.txt","r")
            for x in f1:
                pdf.cell(-1,5,txt = x, ln = 1)
            f1.close()

            l3=[]
            s2="\n"
            s2+="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPATIENT YOGA\n\n"
            mycursor.execute("select imagepath from yoga where patientname=? AND patientphno=? AND patientdate=?",(str(x1.get()),str(x2.get()),str(x3.get())))
            for i in mycursor:
                l3.append(i[0])
            
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=15)
            s3="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYOGA TIMINGS\t\t\t\t\t\t\t\t\tYOGA DURATION\n\n"
            pdf.cell(-1,15,txt = s2, ln = 1)
            pdf.cell(-1,15,txt =s3,ln=2)
            x=0
            y=20
            for image in range(1,len(l3)+1):
                pdf.image(l3[image-1],x=x,y=y+image,w=60,h=70,type= "PNG")
                y=y+70
                if (image%3==0):
                    if(image==len(l3)):
                        break
                    else:
                        pdf.add_page()
                        pdf.cell(-1,15,txt =s3,ln=1)
                        y=20
                    
                    
            
            pdf.output(fp.name)
            filename=os.path.basename(fp.name)
            copy2(fp.name,"LastRecord.pdf")
            
            os.startfile("LastRecord.pdf")
            
            os.remove("temp.txt")
            os.remove("temp1.txt")
            tp.protocol("WM_DELETE_WINDOW",onclosings)
    except PermissionError:
        messagebox.showinfo("Permission Error","Please close all the file then try again",parent=tp)
    except:
        pass
        
    
    




#==============================================================================
#=============================dashbord========================================================================

def session():
  screen.destroy()
  global screen8,screen9
  #screen8 = Toplevel(screen)
  screen8=Tk()
  x, y = screen8.winfo_screenwidth(), screen8.winfo_screenheight()
  screen8.geometry("%dx%d+0+0" % (x, y))
  
  screen8.bg=ImageTk.PhotoImage(file="201.jpg")
  
  screen8.bg_image=Label(screen8,image=screen8.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen8.config(bg="white")
  screen8.title("Dashboard")
  screen8.iconbitmap(r"logo.ico")

  menue(screen8)

  screen9=Toplevel(screen8)
  screen9.geometry("450x450")
  screen9.resizable(0,0)
  screen9.withdraw()

  photo=tk.PhotoImage(file="Whatsapp-icon.png")
  photo1=tk.PhotoImage(file="Gmail-icon.png")
    
  title=Label(screen8,text=" Welcome to the Dashboard!",font=("times new roman",40),fg="#2d6187",bg="#bedcfa").place(x=100,y=50)
  HoverButton(screen8,text="Patient History",font=("times new roman",18,),activebackground='#a8e6cf',bg="#a3d8f4",bd=3,fg="black",command=Record,width=18,height=2).place(x=280,y=150)
  HoverButton(screen8,text="Patient Diet",font=("times new roman",18,),fg="black",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",width=18,height=2,command=diet).place(x=280,y=350)
  HoverButton(screen8,text="Patient Medicine",fg="black",bd=3,height=2,width=18,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",18),command=medicine).place(x=450,y=250)
  HoverButton(screen8,text="Patient Yoga",fg="black",bd=3,height=2,width=18,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",18),command=yogahere).place(x=450,y=450)
  HoverButton(screen8,text="Print",fg="black",bd=3,height=2,width=18,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",18),command=lambda:print_btn(screen9,photo,photo1)).place(x=280,y=550)


  
screen8=None
screen2=None
screen9=None


##---------------------------------------------------------------------Updating Details------------------------------------------------------------------------------#



def pass_match():

    if cmb_question.get()=='Select' or var_answer.get()=="" or pass1.get()=="":
        messagebox.showerror("Error","All feilds are required",parent=root2)
    else:
        
    
            
        conn=sqlite3.connect('my_database.db')
        c1=conn.cursor()
        c1.execute("SELECT * FROM credentials ")
        r1=c1.fetchall()
        check2=0
        for j in r1:
            if j[4]==cmb_question.get() and j[5]==var_answer.get():
                check2=1
        if check2!=1:
            messagebox.showerror("Error","Enter the correct details",parent=root2)
        else:
           
            c1.execute("UPDATE credentials SET password=?,confirm_password=? WHERE email_id=?",(pass1.get(),pass1.get(),email1.get()))
            conn.commit()
            
            messagebox.showinfo("Success","Password updated successfully. Login Again",parent=root2)
            root2.destroy()
            email1.set("")

        


##-----------------------------------------------------------------------------update password window---------------------------------------------------------------##

 

def forgot_password():
    global email1,cmb_question,var_answer,pass1,root2
    if email1.get()=="":
        messagebox.showerror("Error","Please enter  email to reset your password",parent=screen2)

    else:
      conn=sqlite3.connect('my_database.db')
      c=conn.cursor()
      c.execute("SELECT * FROM credentials ")
      r=c.fetchall()
      check1=0
      for i in r:
        if i[3]==email1.get() : 
          check1=1
      if check1!=1:
         messagebox.showerror("Error","Enter the valid email to reset your password",parent=screen2)
      else:
        if check1==1:
          
          root2=Toplevel(screen)
          root2.title("Forgot Password")
          root2.iconbitmap(r"logo.ico")
          root2.geometry("350x400+470+150")
          root2.config(bg="white")
          root2.focus_force()
          root2.grab_set()
          Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
          #option=StringVar()
          question=Label(root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
          cmb_question=ttk.Combobox(root2,font=("times new roman",13),state='readonly',justify=CENTER)
          cmb_question['values']=("Select","Your Pet name","Your previous school name","Your previous college","Your Birth Place","Your Bestfriend Name","Your Favourite place","Your favourite holiday destination ")
          cmb_question.place(x=50,y=130,width=250)
          cmb_question.current(0)
          var_answer=StringVar()
          answer=Label(root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=180)
          txt_answer=Entry(root2,font=("times new roman",15),bg="light gray",textvariable=var_answer).place(x=50,y=210,width=250)
          global pass1
          pass1=StringVar()
          Label(root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=260)
          new_pass=Entry(root2,font=("times new roman",15),bg="light gray",textvariable=pass1,show=".").place(x=50,y=290,width=250)
          HoverButton(root2,text="Reset Password",activebackground='#a8e6cf',bg="#a3d8f4",fg="white",font=("times new roman",15,"bold"),command=pass_match).place(x=100,y=340)

email1=None
cmb_question=None
var_answer=None
pass1=None
root2=None         
##---------------------------------------------------------------------------------Registration---------------------------------------------------------------------##



def register():
  c.execute("select count(*) from credentials")
  for i in c:
    if i[0]==0:
  
      global var_fname,var_lname,var_con,email,password,var_cpass,var_answer,cmb_question,var_chk,root,option
      root=Toplevel(screen)
      root.title("Registration form")
      root.iconbitmap(r"logo.ico")
      
      x, y = root.winfo_screenwidth(), root.winfo_screenheight()
      root.geometry("%dx%d+0+0" % (x, y))
      root.bg=ImageTk.PhotoImage(file="l1.jpg")
      root.bg_image=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
      frame0=Frame(root,width=400,height=500)
      frame0.place(x=150,y=100,width=400,height=500)

      frame0.bg=ImageTk.PhotoImage(file="l4.jpg")
      frame0.bg_image=Label(frame0,image=frame0.bg).place(x=0,y=0,width=350,height=500)

        

      frame1=Frame(root,bg="#eff8ff")
      frame1.place(x=480,y=100,width=700,height=500)
      title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=50)
      var_fname=StringVar()
      f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=100)
      txt_fname=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_fname).place(x=50,y=130,width=250)

      var_lname=StringVar()
      l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=100)
      txt_lname=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_lname).place(x=370,y=130,width=250)
        

      var_con=StringVar()
      c_name=Label(frame1,text="Contact Number",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=170)
      txt_cname=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_con).place(x=50,y=200,width=250) 

      email=StringVar()
      e_name=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=170)
      email_entry=Entry(frame1,font=("times new roman",15),bg="white",textvariable=email).place(x=370,y=200,width=250) 

      option=StringVar()
      question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=240)
      cmb_question=ttk.Combobox(frame1,font=("times new roman",13),textvariable=option,state='readonly',justify=CENTER)
      cmb_question['values']=("Select","Your Pet name","Your previous school name","Your previous college","Your Birth Place","Your Bestfriend Name","Your Favourite place","Your favourite holiday destination ")
      cmb_question.place(x=50,y=270,width=250)
      cmb_question.current(0)

      var_answer=StringVar()
      answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=240)
      txt_answer=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_answer).place(x=370,y=270,width=250)


       
      password=StringVar()
      password2=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=50,y=310)
      password_entry=Entry(frame1,font=("times new roman",15),bg="white",textvariable=password,show=".").place(x=50,y=340,width=250)

      var_cpass=StringVar()
      cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="#eff8ff",fg="#07689f").place(x=370,y=310)
      txt_cpassword=Entry(frame1,font=("times new roman",15),bg="white",textvariable=var_cpass,show=".").place(x=370,y=340,width=250)

      var_chk=IntVar()
      chk=Checkbutton(frame1,text="I Agree The Terms and Conditions",variable=var_chk,onvalue=1,offvalue=0,bg="#eff8ff",font=("times new roman",12)).place(x=50,y=380)
        
      btn_register=HoverButton(frame1,text = "Register Now",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",fg="black",cursor="hand2",command=savedata1,height="1",width="30",font=("times new roman",13)).place(x=50,y=420)
      HoverButton(root,text = "Sign In",activebackground='#a8e6cf',bd=3,bg="#a3d8f4",fg="black",cursor="hand2",height="1",width="30",font=("times new roman",20),command=login).place(x=230,y=530,width=180)
      HoverButton(frame1,text="Back",activebackground='#a8e6cf',bg="#a3d8f4",fg="black",bd=3,height="1",width="15",font=("times new roman",13),command=del_root).place(x=370,y=420)

    else:
      messagebox.showerror("Error","You are already registered go to login and try Forgot Password",parent=screen)
  
var_fname=None
var_lname=None
var_con=None
email=None
password=None
var_cpass=None
var_chk=None
root=None
option=None

##---------------------------------------------------------------------------------Login -----------------------------------------------------------------------##


def login():
  global screen2,email_entry1,password_entry1,email1,password,password_verify,email_entry1,password_entry1,email1,password
  
  def onclosings():
      screen2.destroy()
      screen.destroy()
      
  screen.withdraw()
  screen2 = Toplevel(screen)

  x, y = screen2.winfo_screenwidth(), screen2.winfo_screenheight()
  screen2.geometry("%dx%d+0+0" % (x, y))
  
  screen2.title("Login")
  screen2.iconbitmap(r"logo.ico")

  screen2.bg=ImageTk.PhotoImage(file="l3.jpg")
  screen2.bg_image=Label(screen2,image=screen2.bg).place(x=0,y=0,relwidth=1,relheight=1)

  frame3=Frame(screen2)
  frame3.place(x=130,y=230,width=250,height=210)
  frame3.bg=ImageTk.PhotoImage(file="l4.jpg")
  frame3.bg_image=Label(frame3,image=frame3.bg).place(x=0,y=0,relwidth=1,relheight=1)
  
  title=Label(screen2,text="LOGIN HERE",font=("helvetica",34,"bold"),bg="#d0e8f2",fg="#07689f").place(x=700,y=100)

  e1=mycursor.execute("Select email_id from credentials")
  v1=[]
  for i in mycursor:
      v1.append(i)
  email1=StringVar()
  email=Label(screen2,text="Email Address",font=("times new roman",20,"bold"),bg="#d0e8f2",fg="#07689f").place(x=700,y=200)
  email_entry1=tt.Combobox(screen2,values=v1,textvariable=email1,font=('Fixed', 12,'bold')).place(x=700,y=250,height=28, width=405)
  
   
  password=StringVar()
  password1=Label(screen2,text="Password",font=("times new roman",20,"bold"),bg="#d0e8f2",fg="#07689f").place(x=700,y=300)
  password_entry1=Entry(screen2,font=("times new roman",15),bg="white",width=40,textvariable=password,show=".").place(x=700,y=350)

  HoverButton(screen2,text="Forgot Password?",font=("times new roman",14),bd=3,activebackground='#a8e6cf',bg="#a3d8f4",command=forgot_password).place(x=700,y=380)
  HoverButton(screen2,text="Login",font=("times new roman",16,),fg="black",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",width=15,height=2,command=login_success).place(x=700,y=470)
  HoverButton(screen2,text="Back",fg="black",bd=3,height=2,width=15,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",16),command=del_screen2).place(x=950,y=470)

  screen2.protocol("WM_DELETE_WINDOW",onclosings)

  
email_entry1=None
password_entry1=None
email1=None
password=None
password_verify=None
email_entry1=None
password_entry1=None
screen2=None


##-----------------------------------------------------------------Main Screen-------------------------------------------------------------------------------------##
import os
    
def main_screen():
  global screen
  screen = Tk()
  x, y = screen.winfo_screenwidth(), screen.winfo_screenheight()
  screen.geometry("%dx%d+0+0" % (x, y))
  screen.bg=ImageTk.PhotoImage(file="l1.jpg")
  screen.bg_image=Label(screen,image=screen.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen.title("DOCTOR CURE")
  screen.iconbitmap(r"logo.ico")
  title=Label(screen,text="DOCTOR CURE",font=("impact",60,"bold"),fg="#2d6187",bg="#bedcfa").place(x=270,y=50)
  HoverButton(screen,text="Login",font=("times new roman",14,),activebackground='#a8e6cf',bg="#a3d8f4",bd=3,fg="black",command=login,width=40,height=4).place(x=280,y=250)
  HoverButton(screen,text="Register",font=("times new roman",14,),fg="black",bd=3,activebackground='#a8e6cf',bg="#a3d8f4",width=40,height=4,command=register).place(x=280,y=390)
  HoverButton(screen,text="Close",fg="black",bd=3,height=2,width=15,activebackground='#a8e6cf',bg="#a3d8f4",font=("times new roman",16),command=del_mainscreen).place(x=390,y=530)



  screen.mainloop()
  screen=None

def menue(t):
    def onclosing():
        t.destroy()
        
    t.deiconify()
    t.iconbitmap(r"logo.ico")
    x, y = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (x, y))
    t.resizable(1, 1)

    
    
    #Menue Bar
    menubar=Menu(t)
    t.config(menu=menubar)
    #Sub Menue
    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=submenu)
    submenu.add_command(label="Exit",command=onclosing)

    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=submenu)
    submenu.add_command(label="Dashboard",command=session)
    submenu.add_command(label="Patient History",command=Record)
    submenu.add_command(label="Patient Medicine",command=medicine)
    submenu.add_command(label="Patient Diet",command=diet)
    submenu.add_command(label="Patient Yoga",command=yogahere)
    

    submenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=submenu)
    submenu.add_command(label="About Us",command=lambda:aboutus(t))

    t.protocol("WM_DELETE_WINDOW",onclosing)

    
main_screen()

