from tkinter import *
from tkinter import messagebox as msg

window = Tk()
window.title("Event Registration")
window.geometry('600x400')


try:
	# Show Lable
	##Show title
	n_title = Label(window, text='Event Registration Form')
	n_title.grid(row=0, column=0, columnspan= 3, sticky=W)
	
	#

	window.mainloop()
except KeyboardInterrupt:
	msg.showinfo('Notification', 'Do you want force exit')