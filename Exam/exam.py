from random import randint
from tkinter import *
from tkinter import messagebox as msg

cau = []
budget = '10000.00'

window = Tk()
window.title("Sunwin")
window.geometry("300x500")
msg.showinfo('Welcome', 'Welcome to Sunwin')

def Tai_op():
	cau = []
	for i in range(1, 4): 
		cau.append(randint(1,6))
	if cau[0] + cau[1] + cau[2] > 10:msg.showinfo('Cau Tai', f'Ket qua: Thang\nCau 1: {cau[0]}\nCau 2: {cau[1]}\nCau 3: {cau[2]} \nCau: {cau[0] + cau[1] + cau[2]} ')
	else: msg.showinfo('Cau Tai', f'Ket qua: Thua\nCau 1: {cau[0]}\nCau 2: {cau[1]}\nCau 3: {cau[2]} \nCau: {cau[0] + cau[1] + cau[2]} ')

def Xiu_op():
	cau = []
	for i in range(1, 4): 
		cau.append(randint(1,6))
	if cau[0] + cau[1] + cau[2] > 10: msg.showinfo('Cau Xiu', f'Ket qua: Thua\nCau 1: {cau[0]}\nCau 2: {cau[1]}\nCau 3: {cau[2]} \nCau: {cau[0] + cau[1] + cau[2]} ')
	else: msg.showinfo('Cau Xiu', f'Ket qua: Thang\nCau 1: {cau[0]}\nCau 2: {cau[1]}\nCau 3: {cau[2]} \nCau: {cau[0] + cau[1] + cau[2]} ')


lbl_result = Label(window, text=f"Số tiền: {float(budget)}")
lbl_result.grid(row=0, column=0, sticky=W)
txt_budget = Entry(window, )
btn_all_in = Button(window, text="All in", width=20)
btn_all_in.grid(row=4, column=0)
btn_Tai = Button(window, text="Tai", width=20, command=Tai_op)
btn_Tai.grid(row=5, column=0)

btn_Xiu = Button(window, text="Xiu", width=20, command=Xiu_op)
btn_Xiu.grid(row=6, column=0, columnspan=2, sticky=W)
window.mainloop()