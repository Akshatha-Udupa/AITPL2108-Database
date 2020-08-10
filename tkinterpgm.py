from tkinter import *
a = Tk()
def hello():
    Label(text="Welcome", fg='blue',bg='white',font=20).pack()

a.geometry("1920x1080+0+0")
a.title("My Window")
l = Label(text="Label1", fg='blue',bg='white',font=20).pack()
btn = Button(text="Click Here", fg='red', bg='white', command=hello, font=20).pack()
a.mainloop()