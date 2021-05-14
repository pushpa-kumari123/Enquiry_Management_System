from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as db
my_window=Tk()
my_window.title("Entry page")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
img2=PhotoImage(file="img2.gif")

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
#v7 = StringVar()



def insertdata():

    if v1.get()=="":
        messagebox.showwarning("name ","name field can not be left blank")
    elif v2.get()=="":
        messagebox.showwarning("Purpose ", "Please enter your entry purpose")
    elif v3.get()=="":
        messagebox.showwarning("Gender ", "Gender field can not be left blank")
    elif len(v4.get())!=10:
        v3.set("")
        messagebox.showwarning("mob no. ", "enter 10 digit valid mobile no.")
    elif v4.get()=="":
        messagebox.showwarning("In time", "Please type your in time ")
    elif v5.get()=="":
        messagebox.showwarning("Out", "Out time must have to mention")
    else:
        r1 = v1.get()
        r2 = v2.get()
        r3 = v3.get()
        r4 = v4.get()
        r5 = v5.get()
        r6 = v6.get()
        #r7 = v7.get()

        query="INSERT INTO `entry`(`Full Name`, `Purpose`, `Gender`, `Mob_no`, `In_Time`, `Out_Time`) VALUES ('%s','%s','%s','%s','%s','%s')"%(r1,r2,r3,r4,r5,r6)
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
        #v7.set("")
        cur.close()
        con.close()


def Backf():
    my_window.destroy()
    messagebox.showinfo("Thank you for visiting us")
    import Login_page



L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)
L6=Label(my_window,text="Entry Section",bg="pink", fg="red", font=("arial black",15), width=20)
L6.place(x=450,y=70)

L2=Label(my_window,text="Full Name",bg="lightgreen", fg="white", font=("arial black",14), width=15)
L2.place(x=250,y=130)
E1 = Entry(my_window, width=40,font="40",bd=5,textvariable=v1)
E1.place(x=450,y=130)
L2=Label(my_window, text="Purpose",bg="lightgreen", fg="white", font=("arial black",14), width=15)
L2.place(x=250,y=200)
E2 = Entry(my_window, width=40,font="40",bd=5,textvariable=v2)
E2.place(x=450,y=200)
L3=Label(my_window, text="*Gender",bg="lightgreen", fg="white", font=("arial black",14), width=15)
L3.place(x=250,y=270)
R1=Radiobutton(my_window, text="Male",bg="lavender",bd=3, fg="black",font=("cambria",13),value="male", width=5,variable=v3)
R1.place(x=500,y=270)
R2=Radiobutton(my_window, text="Female",bg="lavender",bd=3, fg="black",font=("cambria",13),value="female", width=5,variable=v3)
R2.place(x=740,y=270)
v3.set(None)


L7=Label(my_window, text="Mobile_no.",bg="lightgreen", fg="white",font=("arial black",14), width=15)
L7.place(x=250,y=350)
E6 = Entry(my_window, width=40,font="40",bd=5,textvariable=v4)
E6.place(x=450,y=350)
L3=Label(my_window, text="In Time",bg="lightgreen", fg="white", font=("arial black",14), width=15)
L3.place(x=250,y=410)
E3 = Entry(my_window, width=40,font="40",bd=5,textvariable=v5)
E3.place(x=450,y=410)
L7=Label(my_window, text="Out Time",bg="lightgreen", fg="white", font=("arial black",14), width=15)
L7.place(x=250,y=490)
E4=Entry(my_window, width=40,font="40",bd=5,textvariable=v6)
E4.place(x=450,y=490)
#L8=Label(my_window, text="sign.",bg="lightgreen", fg="white", font=("arial black",14), width=15)
#L8.place(x=250,y=550)
#E4=Entry(my_window, width=40,font="40",bd=5,textvariable=v7)
#E4.place(x=450,y=550)
B1=Button(my_window,text="Submit",font=("Arial black",15),bd=5,bg="lightgreen",fg="black",command=insertdata,activebackground="grey",activeforeground="blue")
B1.place(x=800,y=590)
B2=Button(my_window,text="Back",font=("Arial black",15),bd=5,bg="orange",fg="white",command=Backf,activebackground="grey",activeforeground="blue")
B2.place(x=1000,y=590)
L10=Label(my_window,bg="pink",height=200,width=350,image=img2,bd=3)
L10.place(x=900,y=140)
F1=Frame(my_window,height=50,width=1366,bg="#ffff00")
F1.place(x=0,y=650)
L8=Label(F1,text="Designed & Developed by  : ",fg="red",bg="#ffff00",font=("Algerian",18),width="35")
L8.place(x=550,y=8)
L9=Label(F1,text="Pushpa Kumari",bg="#ffff00",fg="black",font=("arial black",13),width="20")
L9.place(x=1000,y=10)
my_window.mainloop()