#Window like notepad
from tkinter import *
a = Tk()
a.title("Untitled - Notepad")
a.geometry("500x500+0+0")
m1 = Menu()
l1 = Menu()
l1.add_command(label="New")
l1.add_command(label="New Window")
l1.add_command(label="Open...")
l1.add_command(label="Save")
l1.add_command(label="Save As...")
l1.add_command(label="Page Setup...")
l1.add_command(label="Print")
l1.add_command(label="Exit")

l2 = Menu()
l2.add_command(label="Undo")
l2.add_command(label="Cut")
l2.add_command(label="Copy")
l2.add_command(label="Paste")
l2.add_command(label="Delete")
l2.add_command(label="Search with Bing...")
l2.add_command(label="Find")
l2.add_command(label="Find Next")
l2.add_command(label="Find Previous")
l2.add_command(label="Replace...")
l2.add_command(label="Go To...")
l2.add_command(label="Select All")
l2.add_command(label="Time/Date")

l3 = Menu()
l3.add_command(label="Word Wrap")
l3.add_command(label="Font")

l4 = Menu()
l4.add_command(label="Zoom")
l4.add_command(label="Status Bar")

l5 = Menu()
l5.add_command(label="View Help")
l5.add_command(label="Send Feedback")
l5.add_command(label="About Notepad")

m1.add_cascade(label="File", menu=l1)
m1.add_cascade(label="Edit", menu=l2)
m1.add_cascade(label="Format", menu=l3)
m1.add_cascade(label="View", menu=l4)
m1.add_cascade(label="Help", menu=l5)
a.config(menu=m1)

a.mainloop()