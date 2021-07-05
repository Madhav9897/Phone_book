from tkinter import*
import datetime
from my_people import My_people
from AddPeople import addpeople
today = datetime.date.today()
class Application(object):
    def __init__(self,master):

        #upper portion
        self.master = master
        self.top_container = Frame(master,height =150, bg = 'white')
        self.top_container.pack(fill= X)
        self.phon_img = PhotoImage(file = "images/phone.png")

        self.label = Label(self.top_container,image = self.phon_img,bg="white")
        self.label.place(x = 40,y = 30)

        self.desc = Label(self.top_container, text = "Phone book directory",fg = "powder blue",font = "arial 20 bold",bg = "white")
        self.desc.place(x = 170,y = 50)

        self.date = Label(self.top_container, text = "Date ({})".format(today), font = "arial 10 ",bg = "white")
        self.date.place(x = 500, y = 120)

        #lower portion
        self.bottom_container = Frame(master,height = 500, bg = "powder blue")
        self.bottom_container.pack(fill= X)
        self.view = Button(self.bottom_container,font = "arial 20 bold", text = "       view       ", fg = "#e6f3ff",bg = "grey",command = self.people_func)
        self.view.place(x = 230,y = 50)

        self.add = Button(self.bottom_container,font = "arial 20 bold", text = " add contact ", fg = "#e6f3ff",bg = "grey",command = self.add_people)
        self.add.place(x = 230,y = 150)

        
    def people_func(self):
        people = My_people()

    def add_people(self):
        add = addpeople()
def main():
    root = Tk()
    App = Application(root)
    root.title('Phone book')
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()
