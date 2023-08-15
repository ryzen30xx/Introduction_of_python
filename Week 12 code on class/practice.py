from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msgbox
from loadlist import load_books, load_name

#event handlers
window = Tk()
window.geometry('500x300')
window.title("Book Store")
deliver_op = ['fast', 'ultra fast', 'ultra light']

#optional
def btn_entered():
    if cover_val == 1:
        total =+ 2000

# create widgets
lbl_title = Label(window, text="Book")
lbl_title.grid(row=0, column=0, sticky=W, padx=10)

#listbox label
lst_book = Listbox(window, height=5,selectmode=SINGLE)
lst_book.grid(row=1, column=0, columnspan=2, sticky=W, padx=10)

#name label
lbl_name = Label(window, text="Name :")
lbl_name.grid(row=1, column=3, sticky=W, padx=5)

txt_name = Entry(window, width=10)
txt_name.grid(row=1, column=4, sticky=W, padx=5)

#author label
lbl_author = Label(window, text="Author :")
lbl_author.grid(row=2, column=3, sticky=W, padx=5)

txt_author = Entry(window, width=10)
txt_author.grid(row=2, column=4, sticky=W, padx=5)

#price label
lbl_price = Label(window, text="Price :")
lbl_price.grid(row=3, column=3, sticky=W, padx=5)

txt_price = Entry(window, width=10)
txt_price.grid(row=3, column=4, sticky=W, padx=5)

#quantity label
lbl_quantity = Label(window, text="Quantity :", width=10)
lbl_quantity.grid(row=5, column=0, sticky=W, padx=5)

txt_quantity = Entry(window, width=20)
txt_quantity.grid(row=5, column=1, sticky=W, padx=5)

#Cover label
cover_val = IntVar()
lbl_cover = Label(window, text="Cover ")
lbl_cover.grid(row=6, column=2, sticky=W, padx=5)

txt_cover = Radiobutton(window, text="yes", value=2, variable=cover_val)
txt_cover.grid(row=6, column=3, sticky=W, padx=5)

txt_cover = Radiobutton(window, text="no", value=1, variable=cover_val)
txt_cover.grid(row=6, column=4, sticky=W, padx=5)

#Deliver options
lbl_deliver = Label(window, text="Delivery ", width=10)
lbl_deliver.grid(row=7, column=0, sticky=W)

cbb_deliver = Combobox(window, values=deliver_op)
cbb_deliver.grid(row=7, column=1, sticky=W, padx=5)

#button setting
btn_ok = Button(window, text="OK", width=5)
btn_ok.grid(row=8, column=3, sticky=W, padx=5, command=btn_entered)

btn_ok = Button(window, text="Cancel", width=5)
btn_ok.grid(row=8, column=4, sticky=W, padx=5)

window.mainloop()