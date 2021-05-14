from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as db
my_window=Tk()
my_window.title("Enquiry page")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
img2=PhotoImage(file="download.gif")
def Backf():
    my_window.destroy()
    import Login_page
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()

def insertdata():

    if v1.get()=="":
        messagebox.showwarning("name ","name field can not be left blank")
    elif v2.get()=="":
        messagebox.showwarning("Email id ", "email field can not be left blank")
    elif v3.get()=="":
        messagebox.showwarning("Qualification", "Please enter your qualification")
    elif v4.get()=="":
        messagebox.showwarning("Course Fee", "Be confirm about your course fee")
    elif v5.get()=="":
        messagebox.showwarning("Course Duration", "Be confirm about your  course duration")
    else:
        r1 = v1.get()
        r2 = v2.get()
        r3 = v3.get()
        r4 = v4.get()
        r5 = v5.get()
        r6 = v6.get()

        query="INSERT INTO `enquiry`(`Full Name`, `email`, `qualification`, `course_name`, `fee`, `duration`) VALUES ('%s','%s','%s','%s','%s','%s')"%(r1,r2,r3,r4,r5,r6)
        con = db.connect("localhost", "root", "", "enquiry")
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        v1.set("")
        v2.set("")
        v3.set("")
        v4.set("")
        v5.set("")
        v6.set("")
        messagebox.showinfo("info", "Enquiry insertion successfull")
        cur.close()
        con.close()








L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)
L01=Label(my_window,text="National Institute of Electronics & Information Technology",bg="grey",fg="black",font=("cambria",15),width=50)
L01.place(x=340,y=80)
L2=Label(my_window,text="*Full Name",bg="light green", fg="white", font=("arial black",14), width=18)
L2.place(x=320,y=130)
E1 = Entry(my_window, width=40,font="40",bd=5,textvariable=v1)
E1.place(x=560,y=130)
L6=Label(my_window, text="*Email",bg="light green",fg="white",font=("arial black",14), width=18)
L6.place(x=320,y=180)
E5=Entry(my_window, width=40,font="40",bd=5,textvariable=v2)
E5.place(x=560,y=180)
L2=Label(my_window, text=" Required Qualification",bg="light green", fg="white", font=("arial black",14), width=18)
L2.place(x=320,y=230)
CB=ttk.Combobox(my_window,value=("Diploma","B.tech","Graduation","ITI","BCA"),width="52",textvariable=v3)
CB.place(x=590,y=230)
L3=Label(my_window, text="course Interested",bg="light green", fg="white", font=("arial black",14), width=18)
L3.place(x=320,y=280)
CB1=ttk.Combobox(my_window,value=("Python","Java","C++","O level","PHP"),width="52",textvariable=v4)
CB1.place(x=590,y=280)
L7=Label(my_window, text="course Fee",bg="light green", fg="white", font=("arial black",14), width=18)
L7.place(x=320,y=330)
E1 = Entry(my_window, width=40,font="40",bd=5,textvariable=v5)
E1.place(x=560,y=330)
L8=Label(my_window, text="course Duration",bg="light green", fg="white", font=("arial black",14), width=18)
L8.place(x=320,y=380)
E8 = Entry(my_window, width=40,font="40",bd=5,textvariable=v6)
E8.place(x=560,y=380)

L10=Label(my_window,height=200,width=220,image=img2)
L10.place(x=1000,y=140)

B1=Button(my_window,text="Submit",font=("Arial black",15),bg="lightgreen",fg="black",command=insertdata)
B1.place(x=400,y=500)
B2=Button(my_window,text="Reset",font=("Arial black",15),bg="#00f0f0",fg="black")
B2.place(x=600,y=500)
B3=Button(my_window,text="Back",font=("Arial black",15),bg="orange",fg="black",command=Backf)
B3.place(x=800,y=500)

L4=Label(my_window,text="Designed & Developed by                : ",bg="#ffff00",fg="blue",font=("Algerian",20),width="60")
L4.place(y=650)
L5=Label(my_window,text="Pushpa kushwaha",bg="#ffff00",fg="blue",font=("cambria",18),width="44")
L5.place(x=750,y=650)
my_window.mainloop()