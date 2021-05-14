from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as db

my_window = Tk()

my_window.title("our final project/login/Enquiry record")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
my_window.resizable(1, 1)
L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)

def backf() :
    my_window.destroy()
    import Enquiry_page
def search() :
    swindow=Toplevel()
    swindow.geometry("800x600+30+30")
    TableMargin = Frame(swindow, height="768", width="500")
    TableMargin.place(x=60, y=60)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("slno", "a", "b", "c", "d", "e", "f"), height=23,
                        yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('slno', text="sl_no", anchor=W)
    tree.heading('a', text="Full_name", anchor=W)
    tree.heading('b', text="email", anchor=W)
    tree.heading('c', text="qualification", anchor=W)
    tree.heading('d', text="course_name", anchor=W)
    tree.heading('e', text="Fee", anchor=W)
    tree.heading('f', text="Duration", anchor=W)

    tree.column('#0', minwidth=10, width=10)
    tree.column('#1', minwidth=20, width=30)
    tree.column('#2', minwidth=80, width=100)
    tree.column('#3', minwidth=10, width=20)
    tree.column('#4', minwidth=15, width=20)
    tree.column('#5', minwidth=30, width=100)
    tree.column('#6', minwidth=20, width=80)

    tree.pack()
    # table code end
    if v7.get()=="name":
        query = "select * from enquiry where `Full Name`='%s'"%(v10.get())
    if v7.get() == "email":
        query = "select * from enquiry where email ='%s'" % (v10.get())
    if v7.get() == "qualification":
        query = "select * from enquiry where qualification ='%s'" % (v10.get())
    if v7.get() == "course":
        query = "select * from enquiry where course_name='%s'" % (v10.get())


    con = db.connect("localhost", "root", "", "enquiry")
    cur = con.cursor()
    cur.execute(query)
    row = cur.fetchone()
    while row is not None:
        tree.insert('', 'end', values=(row))
        row = cur.fetchone()

    cur.close()
    con.close()


L1=Label(my_window,text="Enquiry Record",bg="light pink",fg="blue",font=("arial black",20),width="18")
L1.place(x=450,y=75)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v10 = StringVar()
v13 = StringVar()

def insertdata():
    r1 = v1.get()
    r2 = v2.get()
    r3 = v3.get()
    r4 = v4.get()
    r5 = v5.get()
    r6 = v6.get()



    query = "INSERT INTO `enquiry`(`Full Name`, `email`, `qualification`, `course_name`, `fee`, `duration`) VALUES ('%s','%s','%s','%s','%s','%s')" % (
    r1, r2,r3,r4,r5,r6)
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

    messagebox.showinfo("info", " Enquiry Record insertion successfull")
    cur.close()
    con.close()


# table code

TableMargin = Frame(my_window, height="768", width="1000")
TableMargin.place(x=300,y=125)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("slno","a", "b", "c", "d","e","f"), height=23, yscrollcommand=scrollbary.set,
                    xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('slno', text="sl_no", anchor=W)
tree.heading('a', text="Full_name", anchor=W)
tree.heading('b', text="email", anchor=W)
tree.heading('c', text="qualification", anchor=W)
tree.heading('d', text="course_name", anchor=W)
tree.heading('e', text="fee.", anchor=W)
tree.heading('f', text="duration", anchor=W)

tree.column('#0', minwidth=10, width=10)
tree.column('#1', minwidth=20, width=30)
tree.column('#2', minwidth=80, width=100)
tree.column('#3', minwidth=10, width=20)
tree.column('#4', minwidth=15, width=20)
tree.column('#5', minwidth=30, width=100)
tree.column('#6', minwidth=20, width=80)

tree.pack()
# table code end

query = "select * from enquiry"

con = db.connect("localhost", "root", "", "enquiry")
cur = con.cursor()
cur.execute(query)
row = cur.fetchone()
while row is not None:
    tree.insert('', 'end', values=(row))
    row = cur.fetchone()

cur.close()
con.close()

def updatefinal():

    tree.delete(*tree.get_children())
    conn = db.connect("localhost", "root", "", "enquiry")
    cursor = conn.cursor()
    query1 = "UPDATE `enquiry` SET `Full Name`='%s',`email`='%s',`qualification`='%s',`course_name`='%s',`fee`='%s',`duration`='%s' WHERE `slno`=%d" % (
    v1.get(), v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),( slno))
    cursor.execute(query1)
    conn.commit()

    cursor.execute("select * from enquiry")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def updatedata():


    global UpdateWindow,slno,name,email,qualification,course_name,fee,duration

    if not tree.selection():
       result = messagebox.showwarning('update', 'Please Select Something First!')
    else:

        UpdateWindow = Toplevel()
        UpdateWindow.title("Enquiry Update Panel")

        UpdateWindow.geometry("1000x668")

        F2 = Frame(UpdateWindow, height=600, width=800, bg="grey")
        F2.place(x=40, y=40)

        L01 = Label(F2, text="Update Enquiry Record", bg="pink", fg="red", font=("arial black", 15), width=20)
        L01.place(x=250, y=40)

        L2 = Label(F2, text="*Full Name", bg="light green", fg="white", font=("arial black", 14), width=18)
        L2.place(x=100, y=100)
        E1 = Entry(F2, width=40, font="40", bd=5, textvariable=v1)
        E1.place(x=340, y=100)
        L6 = Label(F2, text="*Email", bg="light green", fg="white", font=("arial black", 14), width=18)
        L6.place(x=100, y=150)
        E5 = Entry(F2, width=40, font="40", bd=5, textvariable=v2)
        E5.place(x=340, y=150)
        L2 = Label(F2, text=" Required Qualification", bg="light green", fg="white", font=("arial black", 14),
                   width=18)
        L2.place(x=100, y=200)
        CB = ttk.Combobox(F2, value=("Diploma", "B.tech", "Graduation", "ITI", "BCA"), width="52",
                          textvariable=v3)
        CB.place(x=370, y=200)
        L3 = Label(F2, text="course Interested", bg="light green", fg="white", font=("arial black", 14),
                   width=18)
        L3.place(x=100, y=250)
        CB1 = ttk.Combobox(F2, value=("Python", "Java", "C++", "O level", "PHP"), width="52", textvariable=v4)
        CB1.place(x=370, y=250)
        L7 = Label(F2, text="course Fee", bg="light green", fg="white", font=("arial black", 14), width=18)
        L7.place(x=100, y=300)
        E1 = Entry(F2, width=40, font="40", bd=5, textvariable=v5)
        E1.place(x=340, y=300)
        L8 = Label(F2, text="course Duration", bg="light green", fg="white", font=("arial black", 14), width=18)
        L8.place(x=100, y=350)
        E8 = Entry(F2, width=40, font="40", bd=5, textvariable=v6)
        E8.place(x=340, y=350)



        B3 = Button(F2, text="Back", font=("Arial black", 15), bg="orange", fg="black", command=backf)
        B3.place(x=450, y=400)
        b3 = Button(F2, text="Final update", font=("Arial black", 15), bg="pink", fg="black", bd=5,
                    activebackground="grey", command=updatefinal)
        b3.place(x=600, y=400)

        # get the data from database to New window form

        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']

        conn = db.connect("localhost", "root", "", "enquiry")
        cursor = conn.cursor()
        slno = selecteditem[0]
        cursor.execute("select * from enquiry where slno=%d" %(selecteditem[0]))
        row = cursor.fetchone()
        v1.set(row[1])
        v2.set(row[2])
        v3.set(row[3])
        v4.set(row[4])
        v5.set(row[5])
        v6.set(row[6])

# get the data from database to New window form

def del1():
    if not tree.selection():
       result = messagebox.showwarning('delete', 'Please Select Something First!')
    else:
        result = messagebox.askquestion('delete', 'Are you sure you want to delete this record?')
        if result == 'yes':
         curItem = tree.focus()
         contents =(tree.item(curItem))
         selecteditem = contents['values']
         tree.delete(curItem)
         conn = db.connect("localhost","root","","enquiry")
         cursor = conn.cursor()
         cursor.execute("DELETE FROM enquiry WHERE slno = %d" % selecteditem[0])
         conn.commit()
         cursor.close()
         conn.close()

B2=Button(my_window,text="Delete",bd=5,font=("Arial black",15),bg="light grey",fg="black",width=8,command=del1,activebackground="grey",activeforeground="blue")
B2.place(x=10,y=170)
B1=Button(my_window,text="Update",bd=5,command=updatedata,font=("Arial black",15),bg="light grey",fg="black",width=8,activebackground="grey",activeforeground="blue")
B1.place(x=10,y=250)
B1=Button(my_window,text="Search by :",bd=5,font=("Arial black",15),bg="light grey",fg="black",width=10,activebackground="grey",activeforeground="blue")
B1.place(x=10,y=330)
CB9 = ttk.Combobox(my_window, value=("name", "email","qualification","course"), width="21",textvariable=v7)
CB9.place(x=10, y=390)
B3=Button(my_window,text="Go",bd=5,command=search,font=("Arial black",15),bg="light grey",fg="black",width=5,activebackground="grey",activeforeground="blue")
B3.place(x=10,y=470)
E7 = Entry(my_window, width=20, font="12", textvariable=v10, bd=5)
E7.place(x=10, y=430)




F1=Frame(my_window,height=50,width=1366,bg="#ffff00")
F1.place(x=0,y=650)
L7=Label(F1,text="Designed & Developed by  : ",fg="red",bg="#ffff00",font=("Algerian",18),width="35")
L7.place(x=550,y=8)
L8=Label(F1,text="Pushpa Kumari",bg="#ffff00",fg="black",font=("arial black",13),width="20")
L8.place(x=1000,y=10)
my_window.mainloop()