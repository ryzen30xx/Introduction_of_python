from tkinter import *
from tkinter import messagebox as msg

window = Tk()
def btn_OK_clicked():
	msg.showinfo('noti', 'OK button clicked!')

window.title('test windows')
window.geometry('1920x1080')

lbl_message = Label(window, text='Hello world')
lbl_message.grid(row=0, column=0)

btn_OK = Button(window, text='OK', command=btn_OK_clicked)
btn_OK.grid(row=1, column=1)

window.mainloop()