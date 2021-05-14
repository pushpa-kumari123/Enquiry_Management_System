from tkinter import *
my_window=Tk()
my_window.title("our final project/about us")
my_window.geometry("1366x768")
my_window.configure(bg="light grey")
img2=PhotoImage(file="down.gif")
L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)

L8 = Label(my_window, text="ABOUT US", fg="red", bg="light grey", font=("cambria", 25), width="15")
L8.place(x=550, y=100)

L8 = Label(my_window, text="NIELIT", fg="red", bg="light grey", font=("cambria", 25), width="15")
L8.place(x=200, y=160)

L8 = Label(my_window, text="NIELIT Centre, Patna was established in the year 2008 \n and is operational from 11th floor, Biscomaun Tower,\n Gandhi Maidan, Patna,with an objective  to co-ordinate\n the activities of the various NIELIT Centers in the \n Eastern  Region and to undertake pro-active role \nfor promotion of NIELIT activities in the \nregion thereby extending the access of NIELIT\n to promote knowledge and skill development \nin Information, Electronics and Communications \n Technology (IECT) at various levels which will\n meet the requirement of the industry,\n thereby making the overall development of the \nregion specially in Bihar State.\n",
fg="black", bg="light grey", font=("cambria", 15), width="50")
L8.place(x=50, y=200)

L8 = Label(my_window, text="But now NIELIT is in Bihta", fg="indianred1", bg="light grey", font=("cambria", 15), width="50")
L8.place(x=600, y=180)

L10=Label(my_window,bg="white",height=200,width=350,image=img2)
L10.place(x=700,y=210)






F1 = Frame(my_window, height=60, width=1366, bg="#ffff00")
F1.place(x=0, y=620)
L7 = Label(F1, text="Designed & Developed by  : ", fg="red", bg="#ffff00", font=("cambria", 20), width="30")
L7.place(x=600, y=20)
L8 = Label(F1, text="Pushpa Kushwaha", bg="#ffff00", fg="black", font=("arial black", 13), width="20")
L8.place(x=1000, y=30)
my_window.mainloop()