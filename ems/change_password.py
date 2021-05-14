from tkinter import *
my_window=Tk()
from tkinter import ttk
from tkinter import messagebox
import pymysql as db
my_window.title("our final project/forget password")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
img2=PhotoImage(file="download (1).gif")
def backf():
    my_window.destroy()
    import Forget_password_page

u1= StringVar()
op=StringVar()
newp= StringVar()
conp = StringVar()
def submitee():
    my_window.destroy()



    if u1.get() == "":
        messagebox.showinfo("Alert", "User-id field can not left blank")
    elif op.get() == "":
        messagebox.showinfo("Alert", "Current password field can not left blank")
    elif newp.get() != conp.get():
        messagebox.showinfo("error", "old password and new password are not same")
    else:
        conn = db.connect("localhost", "root", "", "enquiry")
        cursor = conn.cursor()
        cursor.execute("select * from forget where user_id='%s'" % (u1.get()))
        row = cursor.fetchone()
        if row[2] == op.get():
            cursor.execute("update forget set pass='%s' where user_id='%s'" % (newp.get(), u1.get()))
            conn.commit()
            messagebox.showinfo("message", "password changed successful")
            cursor.close()
            conn.close()
    import Login_page

L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)
L2=Label(my_window, text="Change password :",bg="grey", fg="black", font=("Algerian",20), width=20)
L2.place(x=500,y=70)
F2=Frame(my_window,height=400,width=700,bg="pink")
F2.place(x=280,y=120)
L2 = Label(F2, text="User Id :", bg="green", fg="white", font=("arial black", 15), width=15)
L2.place(x=70, y=50)
E1 = Entry(F2, width=30, font="50", bd=5, textvariable=u1)
E1.place(x=285, y=50)
L2 = Label(F2, text="Old password", bg="green", fg="white", font=("arial black", 15), width=15)
L2.place(x=70, y=100)
E2 = Entry(F2, width=30, font="50", bd=5, textvariable=op)
E2.place(x=285, y=100)
L3 = Label(F2, text="New password", bg="green", fg="white", font=("arial black", 15), width=15)
L3.place(x=70, y=150)
E2 = Entry(F2, width=30, font="50", bd=5, textvariable=newp,show="*")
E2.place(x=285, y=150)
L4 = Label(F2, text="Confirm password", bg="green", fg="white", font=("arial black", 15), width=15)
L4.place(x=70, y=200)
E3 = Entry(F2, width=30, font="50", bd=5, textvariable=conp,show="*")
E3.place(x=285, y=200)
B1 = Button(F2, text="Submit", font=("Arial black", 15), bg="lightgreen", fg="black", command=submitee)
B1.place(x=320, y=250)
B2 = Button(F2, text="Back", font=("Arial black", 15), bg="purple", fg="white", command=backf)
B2.place(x=520, y=250)


F1=Frame(my_window,height=50,width=1366,bg="#ffff00")
L10=Label(my_window,height=200,width=220,image=img2)
L10.place(x=1050,y=120)
F1.place(x=0,y=600)
L7=Label(F1,text="Designed & Developed by  : ",fg="red",bg="#ffff00",font=("Algerian",18),width="35")
L7.place(x=550,y=8)
L8=Label(F1,text="Pushpa Kumari",bg="#ffff00",fg="black",font=("arial black",13),width="20")
L8.place(x=1000,y=10)
my_window.mainloop()