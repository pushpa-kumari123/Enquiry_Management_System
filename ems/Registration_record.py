from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as db

my_window = Tk()

my_window.title("our final project/login/record")
my_window.geometry("1366x768")
my_window.configure(bg="grey")
my_window.resizable(1, 1)
L1=Label(my_window,text="ENQUIRY MANAGEMENT SYSTEM",bg="lavender",fg="blue",font=("Algerian",40))
L1.pack(fill=X)

def backf() :
    my_window.destroy()
    import Registration_page
def search() :
    swindow=Toplevel()
    swindow.geometry("1000x600+30+30")
    TableMargin = Frame(swindow, height="300", width="800")
    TableMargin.place(x=100, y=125)
    L00 = Label(swindow, text=" Registration Search Record", bg="pink", fg="blue", font=("arial black", 20))
    L00.place(x=270, y=30)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("slno", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"), height=15,
                        yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('slno', text="sl_no", anchor=W)
    tree.heading('a', text="Full_name", anchor=W)
    tree.heading('b', text="email", anchor=W)
    tree.heading('c', text="dob", anchor=W)
    tree.heading('d', text="Gender", anchor=W)
    tree.heading('e', text="Mobile no.", anchor=W)
    tree.heading('f', text="Qualification", anchor=W)
    tree.heading('g', text="City", anchor=W)
    tree.heading('h', text="Course", anchor=W)
    tree.heading('i', text="Duration", anchor=W)
    tree.heading('j', text="Fee", anchor=W)
    tree.column('#0', minwidth=10, width=10)
    tree.column('#1', minwidth=20, width=30)
    tree.column('#2', minwidth=80, width=100)
    tree.column('#3', minwidth=10, width=20)
    tree.column('#4', minwidth=15, width=20)
    tree.column('#5', minwidth=30, width=100)
    tree.column('#6', minwidth=20, width=80)
    tree.column('#7', minwidth=15, width=70)
    tree.column('#8', minwidth=25, width=30)
    tree.column('#9', minwidth=15, width=40)
    tree.column('#10', minwidth=10, width=50)
    tree.pack()
    # table code end
    if v13.get()=="name":
        query = "select * from registration where `Full Name`='%s'"%(v10.get())
    if v13.get() == "email":
        query = "select * from registration where email='%s'" % (v10.get())
    if v13.get() == "mob_no":
        query = "select * from registration where Mob_no='%s'" % (v10.get())
    if v13.get() == "course":
        query = "select * from registration where Course='%s'" % (v10.get())
    if v13.get() == "city":
        query = "select * from registration where city='%s'" % (v10.get())

    con = db.connect("localhost", "root", "", "enquiry")
    cur = con.cursor()
    cur.execute(query)
    row = cur.fetchone()
    while row is not None:
        tree.insert('', 'end', values=(row))
        row = cur.fetchone()

    cur.close()
    con.close()


L1=Label(my_window,text="Registration Record",bg="light pink",fg="blue",font=("arial black",20),width="18")
L1.place(x=450,y=75)

v1 = StringVar()
v2 = StringVar()
dd = StringVar()
mm = StringVar()
yy = StringVar()
v11 = StringVar()
v3 = StringVar()
q = StringVar()
ci = StringVar()
co = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v10 = StringVar()
v13 = StringVar()


def insertdata():
    r1 = v1.get()
    r2 = v2.get()
    r3 = dd.get()
    r4 = mm.get()
    r5 = yy.get()
    dob1 = r5 + "-" + r4 + "-" + r3
    r6 = v11.get()
    r7 = v3.get()
    r8 = q.get()
    r9 = ci.get()
    r10 = co.get()
    r11 = v4.get()
    r12 = v5.get()

    query = "INSERT INTO `registration`(`Full Name`, `email`, `dob`, `Gender`, `Mob_no`, `qualification`, `city`, `Course`, `Duration`,`Fee`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (r1, r2, dob1, r6, r7, r8, r9, r10, r11, r12)
    con = db.connect("localhost", "root", "", "enquiry")
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    v1.set("")
    v2.set("")
    dd.set("")
    mm.set("")
    yy.set("")
    v11.set("")
    v3.set("")
    q.set("")
    ci.set("")
    co.set("")
    v4.set("")
    v5.set("")

    messagebox.showinfo("info", "Record insertion successfull")
    cur.close()
    con.close()


# table code

TableMargin = Frame(my_window, height="768", width="1500")
TableMargin.place(x=250,y=125)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("slno","a", "b", "c", "d","e","f","g","h","i","j"), height=23,yscrollcommand=scrollbary.set,
                    xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('slno', text="sl_no", anchor=W)
tree.heading('a', text="Full_name", anchor=W)
tree.heading('b', text="email", anchor=W)
tree.heading('c', text="dob", anchor=W)
tree.heading('d', text="Gender", anchor=W)
tree.heading('e', text="Mobile no.", anchor=W)
tree.heading('f', text="Qualification", anchor=W)
tree.heading('g', text="City", anchor=W)
tree.heading('h', text="Course", anchor=W)
tree.heading('i', text="Duration", anchor=W)
tree.heading('j', text="Fee", anchor=W)
tree.column('#0', minwidth=10, width=10)
tree.column('#1', minwidth=20, width=30)
tree.column('#2', minwidth=80, width=100)
tree.column('#3', minwidth=10, width=20)
tree.column('#4', minwidth=15, width=20)
tree.column('#5', minwidth=30, width=100)
tree.column('#6', minwidth=20, width=80)
tree.column('#7', minwidth=15, width=70)
tree.column('#8', minwidth=25, width=30)
tree.column('#9', minwidth=15, width=40)
tree.column('#10', minwidth=10, width=50)
tree.pack()
# table code end

query = "select * from registration"

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
        r3 = dd.get()
        r4 = mm.get()
        r5 = yy.get()
        dob1 = r5 + "-" + r4 + "-" + r3
        tree.delete(*tree.get_children())
        conn = db.connect("localhost", "root", "", "enquiry")
        cursor = conn.cursor()
        query1 = "UPDATE `registration` SET `Full Name`='%s',`email`='%s',`dob`='%s',`Gender`='%s',`Mob_no`='%s',`qualification`='%s',`city`='%s',`Course`='%s',`Duration`='%s',`Fee`='%s' WHERE `slno`=%d"%(v1.get(),v2.get(),dob1,v11.get(),v3.get(),q.get(),ci.get(),co.get(),v4.get(),v5.get(),slno)
        cursor.execute(query1)
        conn.commit()

        cursor.execute("select * from registration")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def updatedata():


    global UpdateWindow,slno,v1,v2,dob1,v11,v3,q,ci,co,v4,v5

    if not tree.selection():
       result = messagebox.showwarning('update', 'Please Select Something First!')
    else:

        UpdateWindow = Toplevel()
        UpdateWindow.title("Update Panel")

        UpdateWindow.geometry("1000x668")
        F2 = Frame(UpdateWindow, height=650, width=1000, bg="light green")
        F2.place(x=150, y=40)
        L00 = Label(F2, text=" Registration Update Form", bg="light green", fg="black", font=("arial black", 13))
        L00.place(x=270, y=3)

        L1 = Label(F2, text="*Type your name here :", bg="light green", fg="black", font=7, width=30)
        L1.place(x=10, y=25)
        L1 = Label(F2, text="Full Name", bg="grey", fg="white", font=("arial black", 12), width=15)
        L1.place(x=30, y=50)
        E1 = Entry(F2, width="30", font="12", textvariable=v1, bd=5)
        E1.place(x=200, y=50)

        L01 = Label(F2, text="*Fill your email id :", bg="light green", fg="black", font=7, width=30)
        L01.place(x=4, y=85)
        L2 = Label(F2, text="Email", bg="grey", fg="white", font=("arial black", 12), width=15)
        L2.place(x=30, y=110)
        E2 = Entry(F2, width="30", font="12", textvariable=v2, bd=5)
        E2.place(x=200, y=110)

        L02 = Label(F2, text="*your date of birth :", bg="light green", fg="black", font=7, width=30)
        L02.place(x=4, y=145)
        L3 = Label(F2, text="DOB", bg="grey", fg="white", font=("arial black", 12), width=15)
        L3.place(x=30, y=170)
        CB1 = ttk.Combobox(F2, textvariable=dd, value=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31), width="8")
        CB1.place(x=220, y=170)
        CB2 = ttk.Combobox(F2, textvariable=mm, value=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width="8")
        CB2.place(x=320, y=170)
        CB3 = ttk.Combobox(F2, textvariable=yy, value=(
        1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004),
                           width="8")
        CB3.place(x=410, y=170)

        L3 = Label(F2, text="*Gender", bg="grey", fg="white", font=("arial black", 12), width=15)
        L3.place(x=30, y=210)
        R1 = Radiobutton(F2, text="Male", bg="lavender", bd=3, fg="black", font=("cambria", 13), value="male", width=5,
                         variable=v11)
        R1.place(x=220, y=210)
        R2 = Radiobutton(F2, text="Female", bg="lavender", bd=3, fg="black", font=("cambria", 13), value="female",
                         width=5, variable=v11)
        R2.place(x=400, y=210)

        L4 = Label(F2, text="Mobile no.", bg="grey", fg="white", font=("arial black", 12), width=15)
        L4.place(x=30, y=250)
        E4 = Entry(F2, width="30", font="12", textvariable=v3, bd=5)
        E4.place(x=200, y=250)

        L03 = Label(F2, text="*Your higher Qualifaction :", bg="light green", fg="black", font=7, width=30)
        L03.place(x=4, y=280)
        L4 = Label(F2, text="Qualification", bg="grey", fg="white", font=("arial black", 12), width=15)
        L4.place(x=30, y=310)
        CB3 = ttk.Combobox(F2, value=("12th", "diploma", "BCA", "MCA", "B.tech", "M.tech", "Graduation"), width="39",
                           textvariable=q)
        CB3.place(x=220, y=310)

        L7 = Label(F2, width=15, height=8, bd=20, bg="lavender")
        L7.place(x=560, y=47)

        L5 = Label(F2, text="Select City", bg="grey", fg="white", font=("arial black", 12), width=15)
        L5.place(x=30, y=348)
        CB4 = ttk.Combobox(F2, textvariable=ci, value=("Patna", "Muzaffarpur", "Barauni", "chapra", "Purniya", "orangabaad", "Bihta", "Motihari", "Bhagalpur",
        "Sitamadhi"), width="39")
        CB4.place(x=220, y=348)

        L05 = Label(F2, text="*Please select your desired course :", bg="light green", fg="black", font=7, width=30)
        L05.place(x=20, y=375)
        L6 = Label(F2, text="course", bg="grey", fg="white", font=("arial black", 12), width=15)
        L6.place(x=30, y=400)
        CB5 = ttk.Combobox(F2, textvariable=co, value=("Python", "core Java", "O Level", "PHP", "C++", "C", "Computer Network ", "Html", "Hacking"), width="39")
        CB5.place(x=220, y=400)
        L7 = Label(F2, text="course Duration", bg="grey", fg="white", font=("arial black", 12), width=15)
        L7.place(x=30, y=435)
        E7 = Entry(F2, width=30, font="12", textvariable=v4, bd=5)
        E7.place(x=200, y=435)

        L8 = Label(F2, text="*course Fee", bg="grey", fg="white", font=("arial black", 12), width=15)
        L8.place(x=30, y=470)
        E8 = Entry(F2, width=30, font="12", textvariable=v5, bd=5)
        E8.place(x=200, y=470)


        B3 = Button(F2, text="Back", font=("Arial black", 15), bg="orange", fg="black", bd=5, command=backf,
                    activebackground="grey", activeforeground="blue")
        B3.place(x=400, y=510)
        b3 = Button(F2, text="Final update", font=("Arial black", 15), bg="pink", fg="black", bd=5,activebackground="grey",command=updatefinal)
        b3.place(x=600, y=510)

        # get the data from database to New window form

        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']

        conn = db.connect("localhost", "root", "", "enquiry")
        cursor = conn.cursor()
        slno = selecteditem[0]
        cursor.execute("select * from registration where slno=%d" %(selecteditem[0]))
        row = cursor.fetchone()
        v1.set(row[1])
        v2.set(row[2])
        dd.set(row[3].split('-')[2])
        mm.set(row[3].split('-')[1])
        yy.set(row[3].split('-')[0])

        v11.set(None)
        v11.set(row[4])
        v3.set(row[5])
        q.set(row[6])
        ci.set(row[7])
        co.set(row[8])
        v4.set(row[9])
        v5.set(row[10])

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
         cursor.execute("DELETE FROM registration WHERE slno = %d" % selecteditem[0])
         conn.commit()
         cursor.close()
         conn.close()

B2=Button(my_window,text="Delete",bd=5,font=("Arial black",15),bg="light grey",fg="black",width=8,command=del1,activebackground="grey",activeforeground="blue")
B2.place(x=10,y=170)
B1=Button(my_window,text="Update",bd=5,command=updatedata,font=("Arial black",15),bg="light grey",fg="black",width=8,activebackground="grey",activeforeground="blue")
B1.place(x=10,y=250)
L20=Label(my_window,text="Search by :",font=("Arial black",15),bg="light grey",fg="black",width=10,activebackground="grey",activeforeground="blue")
L20.place(x=10,y=330)
CB9 = ttk.Combobox(my_window, font=2,value=("name", "email", "mob_no","course", "city"), width="15",textvariable=v13)
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