from tkinter import*
import sqlite3
from tkinter import messagebox
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("create table if not exists phone_book1 (p_id integer  primary key, email text, p_name text, p_sname text,p_phone integer,p_add text)" )
class addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.resizable(False,False)
        self.title("Add People")

        #upper

        upper = Frame(self,height = 150,bg = 'white')
        upper.pack(fill = X)
        self.ico = PhotoImage(file = "images/add.png")
        ico_label = Label(upper, image = self.ico,bg = "white")
        ico_label.place(x = 20, y = 30)
        desc = Label(upper,text = "Add people", font = "arial 20 bold",fg = "grey", bg = "white")
        desc.place(x = 130, y= 50)
        #lower

        lower = Frame(self,height = 500, bg = "#b3ffc2")
        lower.pack(fill = X)
        self.name = Entry(lower,width = 30,bd = 4)
        self.n_label = Label(lower,text = "Name",font="sans 15",bg = "#b3ffc2")
        self.n_label.place(x = 80,y =80 )
        self.name.place(x = 190,y = 80)
        self.name.insert(0,"enter name")

        self.s_name = Entry(lower,width = 30,bd = 4)
        self.s_label = Label(lower,text = "Surname" ,font="sans 15",bg = "#b3ffc2")
        self.s_label.place(x =80 ,y = 120)
        self.s_name.place(x =190 ,y = 120)
        self.s_name.insert(0,"enter surname")

        self.e_label = Label(lower,text = "E-mail",font="sans 15",bg = "#b3ffc2")
        self.e_label.place(x =80 ,y = 160)
        self.email = Entry(lower,width = 30,bd = 4)
        self.email.place(x = 190,y = 160)
        self.email.insert(0,"enter email")

        self.p_label = Label(lower,text = "Phone",font="sans 15",bg = "#b3ffc2")
        self.p_label.place(x =80 ,y =200 )
        self.phone = Entry(lower,width = 30,bd = 4)
        self.phone.place(x = 190,y = 200)
        self.phone.insert(0,"enter phone number")

        self.a_label = Label(lower,text = "Address",font="sans 15",bg = "#b3ffc2")
        self.a_label.place(x =80 ,y = 240)
        self.address = Text(lower,width = 30,height = 12)
        self.address.place(x =190 ,y =240 )


        SUBMIT  = Button(lower,text = "Add person",font = "sans 15",command = self.add)
        SUBMIT.place(x = 130,y = 300)
    def add(self):
        name = self.name.get()
        email = self.email.get()
        address = self.address.get("1.0",END)
        phone = self.phone.get()
        s_name = self.s_name.get()
        if(name and email!="" and address and phone and s_name!=""):
            try:
                query = "insert into phone_book1(email, p_name, p_sname,p_phone,p_add)values(?,?,?,?,?)"
                cur.execute(query,(email,name,s_name,phone,address))
                messagebox.showinfo("success")
                conn.commit()
                self.destroy()
            except Exception as e:
                messagebox.showerror("error",str(e))
        else:
            messagebox.showerror("fill all the entries")
