from tkinter import*
import sqlite3
from tkinter import messagebox
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("create table if not exists phone_book1 (p_id integer  primary key, email text, p_name text, p_sname text,p_phone integer,p_add text)" )
class Display(Toplevel):
    def __init__(self,index):
        global index1
        index1 = index
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.resizable(False,False)
        self.title("Display")

        #upper

        upper = Frame(self,height = 150,bg = 'white')
        upper.pack(fill = X)
        self.ico = PhotoImage(file = "images/person.png")
        ico_label = Label(upper, image = self.ico,bg = "white")
        ico_label.place(x = 20, y = 30)
        desc = Label(upper,text = "Display contact", font = "arial 20 bold",fg = "grey", bg = "white")
        desc.place(x = 130, y= 50)
        #lower

        lower = Frame(self,height = 500, bg = "#778ed9")
        lower.pack(fill = X)

        query = "select * from phone_book1 where p_id='{}'".format(index1[0])
        result = cur.execute(query).fetchone()
        mail = result[1]
        name = result[2]
        s_name = result[3]
        phone = result[4]
        address = result[5]


        self.name = Entry(lower,width = 30,bd = 4)
        self.n_label = Label(lower,text = "Name",font="sans 15",bg = "#b3ffc2")
        self.n_label.place(x = 80,y =80 )
        self.name.place(x = 190,y = 80)

        self.name.insert(0,name)
        self.name.config(state = "disabled")

        self.s_name = Entry(lower,width = 30,bd = 4)
        self.s_label = Label(lower,text = "Surname" ,font="sans 15",bg = "#b3ffc2")
        self.s_label.place(x =80 ,y = 120)
        self.s_name.place(x =190 ,y = 120)
        self.s_name.insert(0,s_name)
        self.s_name.config(state = "disabled")

        self.e_label = Label(lower,text = "E-mail",font="sans 15",bg = "#b3ffc2")
        self.e_label.place(x =80 ,y = 160)
        self.email = Entry(lower,width = 30,bd = 4)
        self.email.place(x = 190,y = 160)
        self.email.insert(0,mail)
        self.email.config(state = "disabled")

        self.p_label = Label(lower,text = "Phone",font="sans 15",bg = "#b3ffc2")
        self.p_label.place(x =80 ,y =200 )
        self.phone = Entry(lower,width = 30,bd = 4)
        self.phone.place(x = 190,y = 200)
        self.phone.insert(0,phone)
        self.phone.config(state = "disabled")

        self.a_label = Label(lower,text = "Address",font="sans 15",bg = "#b3ffc2")
        self.a_label.place(x =80 ,y = 240)
        self.address = Text(lower,width = 30,height = 12)
        self.address.insert(1.0,address)
        self.address.place(x =190 ,y =240 )
        self.address.config(state = "disabled")
