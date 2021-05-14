from tkinter import *
from tkinter import ttk
from tkinter import messagebox

my_window = Tk()
my_window.title("our final project/help")
my_window.geometry("1366x768")
my_window.resizable(1, 1)
my_window.configure(bg="grey")
L1 = Label(my_window, text="ENQUIRY MANAGEMENT SYSTEM", bg="lavender", fg="blue", font=("Algerian", 40), bd=4)
L1.pack(fill=X)

L2=Label(my_window, text="How can i help you? :", bg="grey", fg="white", font=("cambria",20),width=40)
L2.place(x=200,y=200)
E2=Entry(my_window,width=50,font="20",show="*",bd=3)
E2.place(x=230,y=250)

F1 = Frame(my_window, height=60, width=1366, bg="#ffff00")
F1.place(x=0, y=620)
L7 = Label(F1, text="Designed & Developed by  : ", fg="red", bg="#ffff00", font=("cambria", 20), width="30")
L7.place(x=600, y=20)
L8 = Label(F1, text="Pushpa Kumari", bg="#ffff00", fg="black", font=("arial black", 13), width="20")
L8.place(x=1000, y=30)
my_window.mainloop()