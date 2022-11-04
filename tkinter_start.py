from tkinter import *
from tkinter import messagebox

top = Tk()
# Code to add widgets will go here...
top.geometry("500x600")


def hello_call_back():
    msg = messagebox.showinfo("Info", f"Twoje imię to: {e1.get()}")


def insert_name_to_label():
    l2.configure(text=e1.get())


b = Button(top, text = "Podaj imię", command = hello_call_back)
b.place(x = 50,y = 50)

b2 = Button(top, text="Zmień label", command= insert_name_to_label )
b2.place(x = 250,y = 250)

l1 = Label(top, text="Podaj imię: ")
l1.pack(side=LEFT)

l2 = Label(top, text="To jest label2")
l2.pack()

e1 = Entry(top, bd=5)
e1.pack(side=RIGHT)


top.mainloop()
