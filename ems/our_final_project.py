from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as db
my_window=Tk()
my_window.title("OUR FINAL PROJECT")
my_window.geometry("1366x768")
my_window.resizable(1, 1)
my_window.configure(bg="grey")
img2=PhotoImage(file="nielitlogo.gif")
L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40),bd=4)
L1.pack(fill=X)
L7=Label(my_window,text="Admin Panel",bg="indianred1",fg="white",font=("cambria",20),width="20")
L7.place(x=200,y=80)
u1=StringVar()
p1=StringVar()
def forg():
    my_window.destroy()
    import Forget_password_page
def subm():
        if u1.get() == "" or p1.get() == "":
            messagebox.showinfo("error", "username and password can not be left blank")
        else:
            conn = db.connect("localhost", "root", "", "enquiry")
            cursor = conn.cursor()
            query = "SELECT * from forget where user_id='%s' and pass='%s'" % (u1.get(), p1.get())
            cursor.execute(query)
            if cursor.rowcount == 1:
                import Login_page
            else:
                messagebox.showinfo("error", "either username or password is wrong")
            cursor.close()
            conn.close()
def abt():
    my_window.destroy()
    import About_us

def out():
    my_window.destroy()
    import Logout
def help():
    my_window.destroy()
    import Help_page


L2= Label(my_window,text="User Id", bg="light green", fg="black", font=("bold",15), width=15)
L2.place(x=100,y=200)
E1=Entry(my_window,width=30,font="20",textvariable=u1,bd=3)
E1.place(x=300,y=200)
L3=Label(my_window,text="Password",bg="light green",fg="black",font=("bold",15),width=15)
L3.place(x=100,y=280)
E2=Entry(my_window,width=30,font="20",show="*",textvariable=p1,bd=3)
E2.place(x=300,y=280)
B1=Button(my_window,text="Login",font=("Arial black",15),bg="pink",fg="black",command=subm,bd=3,activebackground="grey",activeforeground="blue")
B1.place(x=400,y=400)
B2=Button(my_window,text="Exit",font=("Arial black",15),bg="pink",fg="black",command=my_window.quit,bd=3,activebackground="grey",activeforeground="blue")
B2.place(x=600,y=400)
B3=Button(my_window,text="Forget password",font=("Arial black",15),bg="pink",fg="black",command=forg,bd=3,activebackground="grey",activeforeground="blue")
B3.place(x=100,y=400)
F1 = Frame(my_window, height=30, width=1366, bg="#ffff00")
F1.place(x=0, y=650)
L7 = Label(F1, text="Designed & Developed by  : ", fg="red", bg="#ffff00", font=("Algerian", 20), width="30")
L7.place(x=550,y=0)
L8 = Label(F1, text="Pushpa Kumari", bg="#ffff00", fg="black", font=("arial black", 14), width="20")
L8.place(x=1000, y=0)
L10=Label(my_window,bg="white",height=200,width=350,image=img2)
L10.place(x=900,y=150)



B5=Button(my_window,text="About us",font=("Arial black",10),bg="lavender",fg="Red",command=abt,width=17,bd=7,activebackground="grey",activeforeground="blue")
B5.place(x=800,y=600)

B8=Button(my_window,text="Log out",font=("Arial black",10),bg="lavender",fg="Red",command=out,width=17,bd=7,activebackground="grey",activeforeground="blue")
B8.place(x=1000,y=600)
B9=Button(my_window,text="Help",font=("Arial black",10),bg="lavender",fg="Red",command=help,height=1,width=17,bd=7,activebackground="grey",activeforeground="blue")
B9.place(x=1200,y=600)
my_window.mainloop()