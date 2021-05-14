from tkinter import *
from tkinter import messagebox
import pymysql as db
my_window=Tk()
my_window.title("our final project/forget password")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
img2=PhotoImage(file="sad.gif")
def chang():
    my_window.destroy()
    import change_password
u1 = StringVar()
mob = StringVar()
dob = StringVar()
mail = StringVar()
def submitee():
    my_window.destroy()
    if u1.get() == "":
        messagebox.showinfo("error", "User-id feild can not left blank")
    elif mob.get() == "":
        messagebox.showinfo("error", "Mobile no. feild can not left blank")
    elif dob.get() == "":
        messagebox.showinfo("error", "Date Of Birth feild can not left blank")
    elif mail.get() == "":
        messagebox.showinfo("error", "Email feild can not left blank")
    else:
        conn = db.connect("localhost", "root", "", "enquiry")
        cursor = conn.cursor()
        query = "SELECT * from forget where user_id='%s'" % (u1.get())
        cursor.execute(query)

        if cursor.rowcount == 1:
             row = cursor.fetchone()
             messagebox.showinfo("show", "Your password is %s" % (row[2]))
        else:
             messagebox.showinfo("error", "either username or email_id is wrong")
             cursor.close()
             conn.close()

    import our_final_project
L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)

L5=Label(my_window, text="User Id :", bg="light green", fg="white", font=("arial black",15), width=20)
L5.place(x=300,y=100)
E5 = Entry(my_window, width=40,font="40",bd=5,textvariable=u1)
E5.place(x=580, y=100)

L2=Label(my_window, text="Registered mobile no. :", bg="light green", fg="white", font=("arial black",15), width=20)
L2.place(x=300,y=150)
E1 = Entry(my_window, width=40,font="40",bd=5,textvariable=mob)
E1.place(x=580, y=150)
L2=Label(my_window, text="DOB",bg="light green", fg="white", font=("arial black",15), width=20)
L2.place(x=300,y=200)
E2 = Entry(my_window, width=40,font="40",bd=5,textvariable=dob)
E2.place(x=580, y=200)


L4=Label(my_window, text="Email",bg="light green", fg="white", font=("arial black",15), width=20)
L4.place(x=300,y=250)
E3 = Entry(my_window, width=40,font="40",bd=5,textvariable=mail)
E3.place(x=580, y=250)
B1=Button(my_window,text="Submit",font=("Arial black",15),bg="lightgreen",fg="black",command=submitee)
B1.place(x=400,y=400)
B2=Button(my_window,text="Change password",font=("Arial black",15),bg="indianred1",fg="white",command=chang)
B2.place(x=600,y=400)
F1=Frame(my_window,height=50,width=1366,bg="#ffff00")

L10=Label(my_window,height=200,width=220,image=img2)
L10.place(x=1050,y=120)


F1.place(x=0,y=600)
L7=Label(F1,text="Designed & Developed by  : ",fg="red",bg="#ffff00",font=("Algerian",18),width="35")
L7.place(x=550,y=8)
L8=Label(F1,text="Pushpa Kumari",bg="#ffff00",fg="black",font=("arial black",13),width="20")
L8.place(x=1000,y=10)

my_window.mainloop()