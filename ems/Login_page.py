from tkinter import *
my_window=Tk()
my_window.title("our final/login")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
img2=PhotoImage(file="login.gif")
def Entryf():
    my_window.destroy()
    import Entry_page
def out():
    my_window.destroy()
    import Logout
def reg():
    my_window.destroy()
    import Registration_page
def Enq():
    my_window.destroy()
    import Enquiry_page
def regr():
    my_window.destroy()
    import Registration_Record
def enqr():
    my_window.destroy()
    import Enquiry_record
def entr():
    my_window.destroy()
    import Entry_Record
def Backf():
    my_window.destroy()
    import our_final_project
L1 = Label(my_window, text="ENQUIRY MANAGEMENT SYSTEM", bg="lavender", fg="blue", font=("Algerian", 40))
L1.pack(fill=X)
L1 = Label(my_window, text="Welcome to our enquiry & information zone",width=50, bg="grey", fg="white", font=("arial black", 25))
L1.place(x=170,y=100)

B5=Button(my_window,text="Registration",font=("Arial black",15),bd=5,bg="lavender",fg="black",width=20,command=reg,activebackground="grey",activeforeground="blue")
B5.place(x=400,y=160)
B6=Button(my_window,text="Enquiry",font=("Arial black",15),bd=5,bg="lavender",fg="black",width=20,command=Enq,activebackground="grey",activeforeground="blue")
B6.place(x=400,y=220)
B1=Button(my_window,text="Entry",font=("Arial black",15),bd=5,bg="lavender",fg="black",width=20,command=Entryf,activebackground="grey",activeforeground="blue")
B1.place(x=400,y=280)
L13=Label(my_window,text="Record",font=("Arial black",15),bg="lavender",fg="black",width=20,activebackground="grey",activeforeground="blue")
L13.place(x=400,y=340)

L11 = Label(my_window, text=":",width=2, bg="grey",bd=5, fg="white", font=("arial black", 40))
L11.place(x=720,y=325)

B1=Button(my_window,text="Registration record",bd=5,font=("Arial black",15),bg="pink",fg="black",width=20,command=regr,activebackground="grey",activeforeground="blue")
B1.place(x=820,y=340)
B2=Button(my_window,text="Enquiry record",bd=5,font=("Arial black",15),bg="pink",fg="black",width=20,command=enqr,activebackground="grey",activeforeground="blue")
B2.place(x=820,y=400)
B2=Button(my_window,text="Entry record",bd=5,font=("Arial black",15),bg="pink",fg="black",width=20,command=entr,activebackground="grey",activeforeground="blue")
B2.place(x=820,y=460)


B7=Button(my_window,text="Back",font=("Arial black",14),bg="indianred1",fg="white",width=10,command=Backf,activebackground="grey",activeforeground="blue")
B7.place(x=1200,y=530)
F1=Frame(my_window,height=50,width=1366,bg="#ffff00")
F1.place(x=0,y=600)

L10=Label(my_window,height=400,width=250,image=img2)
L10.place(x=2,y=100)


L7=Label(F1,text="Designed & Developed by  : ",fg="red",bg="#ffff00",font=("Algerian",18),width="35")
L7.place(x=550,y=8)
L8=Label(F1,text="Pushpa Kumari",bg="#ffff00",fg="black",font=("arial black",13),width="20")
L8.place(x=1000,y=10)

my_window.mainloop()