from tkinter import *
my_window=Tk()
my_window.title("Logout page")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
def entryf():
    my_window.destroy()
    import Registration_page
def out():
    my_window.destroy()
    import our_final_project
L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)
L2=Label(my_window, text="Do you want to log out? :", bg="grey", fg="white", font=("cambria",20),width=40)
L2.place(x=200,y=200)
B1=Button(my_window,text="Yes",font=("Arial black",15),bg="lightgreen",fg="black",command=out)
B1.place(x=400,y=400)
B2=Button(my_window,text="No",font=("Arial black",15),bg="#f00000",fg="white")
B2.place(x=700,y=400)
F1 = Frame(my_window, height=60, width=1366, bg="#ffff00")
F1.place(x=0, y=620)
L7 = Label(F1, text="Designed & Developed by  : ", fg="red", bg="#ffff00", font=("cambria", 20), width="30")
L7.place(x=600, y=20)
L8 = Label(F1, text="Pushpa Kumari", bg="#ffff00", fg="black", font=("arial black", 13), width="20")
L8.place(x=1000, y=30)

my_window.mainloop()