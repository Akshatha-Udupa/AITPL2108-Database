#calculator using tkinter
from tkinter import *

a = Tk()
exp = " "

def press(num):
    global exp
    exp = exp+str(num)
    equation.set(exp)

def equalpress(equation):
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = " "
    except:
        equation.set('error')
        exp = " "

def clear ():
    global exp
    exp = " "
    equation.set(" ")


equation = StringVar()
a.title("Calculator")
a.geometry("375x275+0+0")


t1 = Entry(a, font=16, bd=4,textvariable=equation)
t1.grid(columnspan=4, ipadx=67)

b1 = Button(text='1', height=1, width=7,font=14, command=lambda : press(1))
b1.grid(row=1, column=0)
b2 = Button(text='2', height=1, width=7,font=14, command=lambda : press(2))
b2.grid(row=1, column=1)
b3 = Button(text='3', height=1, width=7,font=14, command = lambda : press(3))
b3.grid(row=1, column=2)
b4 = Button(text='4', height=1, width=7,font=14, command = lambda : press(4))
b4.grid(row=2, column=0)
b5 = Button(text='5', height=1, width=7,font=14, command = lambda : press(5))
b5.grid(row=2, column=1)
b6 = Button(text='6', height=1, width=7,font=14, command = lambda : press(6))
b6.grid(row=2, column=2)
b7 = Button(text='7', height=1, width=7,font=14, command = lambda : press(7))
b7.grid(row=3, column=0)
b8 = Button(text='8', height=1, width=7,font=14, command = lambda : press(8))
b8.grid(row=3, column=1)
b9 = Button(text='9', height=1, width=7,font=14, command = lambda : press(9))
b9.grid(row=3, column=2)
b0 = Button(text='0', height=1, width=7,font=14, command = lambda : press(0))
b0.grid(row=4, column=0)
plus = Button(text='+', height=1, width=7, font=14,command = lambda : press('+'))
plus.grid(row=1, column=3)
pmin = Button(text='-', height=1, width=7, font=14, command = lambda : press('-'))
pmin.grid(row=2, column=3)
mul = Button(text='*', height=1, width=7, font=14, command = lambda : press('*'))
mul.grid(row=3, column=3)
div = Button(text='/', height=1, width=7, font=14, command = lambda : press('/'))
div.grid(row=4, column=3)
eql = Button(text='=', height=1, width=7, font=14, command=lambda: equalpress(equation))
eql.grid(row=4, column=2)
Decimal = Button(text='.', height=1, width=7, font=12,command=lambda: press('.'))
Decimal.grid(row=4, column=1)
clr = Button(text='Clear', height=1, width=7, font=12,command=lambda : clear())
clr.grid(row=5, ipadx=135, columnspan=14)



a.mainloop()