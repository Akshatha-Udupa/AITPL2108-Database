#login window using tkinter
from tkinter import *
import tkinter.messagebox
a = Tk()
a.geometry("500x500+0+0")
a.title("Login Window")
b = tkinter.messagebox
l1 = Label(a, text="Username", font=16)
txt1 = Entry(a, width=20, font=16)
l2 = Label(text="Password", font=16)
txt2 = Entry(a, width=20, font=16, show='*')
def login():
    user = txt1.get()
    pwd = txt2.get()
    if user == 'Admin' and pwd == 'adminadmin':
        b.showinfo("Login successful")
    elif user == '' or pwd == '':
        b.askokcancel("Enter username & password")
    else:
        b.askokcancel("Invalid username and password")
b1 = Button(text="Login", height=2, width=10, font=16, command=login)
l1.grid(row=0, column=0)
txt1.grid(row=0, column=1)
l2.grid(row=1, column=0)
txt2.grid(row=1, column=1)
b1.grid(row=2, column=1)
a.mainloop()


