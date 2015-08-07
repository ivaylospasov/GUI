#!/usr/bin/env python3

from tkinter import *

root = Tk()

photo = PhotoImage(file="us.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()