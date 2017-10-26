from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("500x300")

L1 = Label(top, text = "Enter")
L1.pack( side = LEFT)
E1 = Entry(top)
E1.pack(side = RIGHT)

top.mainloop()