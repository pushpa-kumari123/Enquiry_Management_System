from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as db
my_window=Tk()
my_window.title("our final project/login/registration")
my_window.geometry("1366x768")
img2=PhotoImage(file="reg3.gif")
def backf() :
    my_window.destroy()
    import Login_page

v1 = StringVar()
v2 = StringVar()
dd = StringVar()
mm = StringVar()
yy = StringVar()
v11 = StringVar()
v3 = StringVar()
q = StringVar()
ci = StringVar()
co = StringVar()
v4 = StringVar()
v5 = StringVar()

def insertdata():
    if v1.get()=="":
        messagebox.showwarning("name ","name field can not be left blank")
    elif v2.get()=="":
        messagebox.showwarning("Email id ", "email field can not be left blank")
    elif len(v3.get())!=10:
        v3.set("")
        messagebox.showwarning("mob no. ", "enter 10 digit valid mobile no.")

    elif q.get()=="":
        messagebox.showwarning("qualification", "Qualification field can't left blank")
    elif ci.get()=="":
        messagebox.showwarning("City", "Please select your City")
    elif co.get() == "":
        messagebox.showwarning("Course", "Please select your desired course")
    elif v4.get()=="":
        messagebox.showwarning("Course Duration", "Be confirm about your course duation")
    elif v5.get()=="":
        messagebox.showwarning("Course Fee", "Be confirm about your course fee")
    else:
        r1 = v1.get()
        r2 = v2.get()
        r3 = dd.get()
        r4 = mm.get()
        r5 = yy.get()
        dob1=r5+"-"+r4+"-"+r3
        r6 = v11.get()
        r7 = v3.get()
        r8 = q.get()
        r9 = ci.get()
        r10 = co.get()
        r11 = v4.get()
        r12 = v5.get()

        query="INSERT INTO `registration`(`Full Name`, `email`, `dob`, `Gender`, `Mob_no`, `qualification`, `city`, `Course`, `Duration`,`Fee`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(r1,r2,dob1,r6,r7,r8,r9,r10,r11,r12)
        con = db.connect("localhost", "root", "", "enquiry")
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        v1.set("")
        v2.set("")
        dd.set("")
        mm.set("")
        yy.set("")
        v11.set("")
        v3.set("")
        q.set("")
        ci.set("")
        co.set("")
        v4.set("")
        v5.set("")
        cur.close()
        con.close()

L0=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",30))
L0.pack(fill=X)
F2=Frame(my_window,height=768,width=800,bg="light green")
F2.place(x=280,y=80)
L01=Label(my_window,text="National Institute of Electronics & Information Technology",fg="black",font=("cambria",15))
L01.place(x=395,y=50)

L00=Label(F2,text="REGISTRATION FORM",bg="light green",fg="red",font=("arial black",13))
L00.place(x=270,y=3)

L1=Label(F2,text="*Type your name here :",bg="light green", fg="black", font=7, width=30)
L1.place(x=10,y=25)
L1=Label(F2,text="Full Name",bg="grey", fg="white", font=("arial black",12), width=15)
L1.place(x=30,y=50)
E1 = Entry(F2, width="30",font="12",textvariable=v1,bd=5)
E1.place(x=200,y=50)

L01=Label(F2,text="*Fill your email id :",bg="light green", fg="black", font=7, width=30)
L01.place(x=4,y=85)
L2=Label(F2,text="Email",bg="grey", fg="white", font=("arial black",12), width=15)
L2.place(x=30,y=110)
E2 = Entry(F2, width="30",font="12",textvariable=v2,bd=5)
E2.place(x=200,y=110)

L02=Label(F2,text="*your date of birth :",bg="light green", fg="black", font=7, width=30)
L02.place(x=4,y=145)
L3=Label(F2,text="DOB",bg="grey", fg="white", font=("arial black",12), width=15)
L3.place(x=30,y=170)
CB1=ttk.Combobox(F2,textvariable=dd, value=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),width="8")
CB1.place(x=220,y=170)
CB2=ttk.Combobox(F2,textvariable=mm, value=(1,2,3,4,5,6,7,8,9,10,11,12),width="8")
CB2.place(x=320,y=170)
CB3=ttk.Combobox(F2,textvariable=yy,value=(1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004),width="8")
CB3.place(x=410,y=170)

L3=Label(F2, text="*Gender",bg="grey", fg="white", font=("arial black",12), width=15)
L3.place(x=30,y=210)
R1=Radiobutton(F2, text="Male",bg="lavender",bd=3, fg="black",font=("cambria",13),value="male", width=5,variable=v11)
R1.place(x=220,y=210)
R2=Radiobutton(F2, text="Female",bg="lavender",bd=3, fg="black",font=("cambria",13),value="female", width=5,variable=v11)
R2.place(x=400,y=210)
v11.set(None)



L4=Label(F2,text="Mobile no.",bg="grey", fg="white", font=("arial black",12), width=15)
L4.place(x=30,y=250)
E4 = Entry(F2, width="30",font="12",textvariable=v3,bd=5)
E4.place(x=200,y=250)


L03=Label(F2,text="*Your higher Qualifaction :",bg="light green", fg="black", font=7, width=30)
L03.place(x=4,y=280)
L4=Label(F2,text="Qualification",bg="grey", fg="white", font=("arial black",12), width=15)
L4.place(x=30,y=310)
CB3=ttk.Combobox(F2,value=("12th","diploma","BCA","MCA","B.tech","M.tech","Graduation"),width="39",textvariable=q)
CB3.place(x=220,y=310)

L7=Label(F2,width=120,height=130,bd=5,bg="lavender",image=img2)
L7.place(x=560,y=47)
L05=Label(F2,text="Paste your latest photo here",bg="light green", fg="black", font=5, width=30)
L05.place(x=500,y=200)

L5=Label(F2,text="Select City",bg="grey", fg="white", font=("arial black",12), width=15)
L5.place(x=30,y=348)
CB4=ttk.Combobox(F2,textvariable=ci,value=("Patna","Muzaffarpur","Barauni","chapra","Purniya","orangabaad","Bihta","Motihari","Bhagalpur","Sitamadhi"),width="39")
CB4.place(x=220,y=348)

L05=Label(F2,text="*Please select your desired course :",bg="light green", fg="black", font=7, width=30)
L05.place(x=20,y=375)
L6=Label(F2, text="course",bg="grey", fg="white", font=("arial black",12),width=15)
L6.place(x=30,y=400)
CB5=ttk.Combobox(F2,textvariable=co,value=("Python","core Java","O Level","PHP","C++","C","Computer Network ","Html","Hacking"),width="39")
CB5.place(x=220,y=400)
L7=Label(F2, text="course Duration",bg="grey", fg="white", font=("arial black",12), width=15)
L7.place(x=30,y=435)
E7=Entry(F2, width=30,font="12",textvariable=v4,bd=5)
E7.place(x=200,y=435)


L8=Label(F2, text="*course Fee",bg="grey", fg="white", font=("arial black",12), width=15)
L8.place(x=30,y=470)
E8=Entry(F2, width=30,font="12",textvariable=v5,bd=5)
E8.place(x=200,y=470)

B1=Button(F2,text="Submit",font=("Arial black",15),bg="grey",fg="black",bd=5,command=insertdata,activebackground="grey",activeforeground="blue")
B1.place(x=200,y=510)
B3=Button(F2,text="Back",font=("Arial black",15),bg="orange",fg="black",bd=5,command=backf,activebackground="grey",activeforeground="blue")
B3.place(x=400,y=510)

F1=Frame(my_window,height=50,width=1366,bg="#ffff00")
F1.place(x=0,y=650)
L8=Label(F1,text="Designed & Developed by  : ",fg="red",bg="#ffff00",font=("Algerian",18),width="35")
L8.place(x=550,y=8)
L9=Label(F1,text="Pushpa Kushwaha",bg="#ffff00",fg="black",font=("arial black",13),width="20")
L9.place(x=1000,y=10)
my_window.mainloop()