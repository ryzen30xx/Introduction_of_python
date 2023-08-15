from tkinter import *
from tkinter import messagebox as msg

window = Tk()

window.title("Arithmetic Operators")

window.geometry('1366x768')

a= Label(window, text='a = ')
a.grid(row=0, column=0)

a_in = Entry(window, width=10)
a_in.grid(row=0, column=1)

b = Label(window, text='b = ')
b.grid(row=1, column=0)

b_in = Entry(window, width=10)
b_in.grid(row=1, column=1)

window.mainloop()

