from tkinter import *
from tkinter import messagebox as msg
from os import system
questions =[['What is the capital of France?', 'Paris', 'Lodon', 'Berlin', 'Madrid', 1],
	    	['What is the capital of Germany?', 'Paris', 'Lodon', 'Berlin', 'Madrid', 3],
			['What is the capital of Spain?', 'Paris', 'Lodon', 'Berlin', 'Madrid', 4],
			['What is the capital of United Kingdom?', 'Paris', 'Lodon', 'Berlin', 'Madrid', 2]]

curr_question = 0
def load_question(question_index):
	lbl_quiz['text'] = questions[question_index][0]
	rd_option1 = questions[question_index][1]
	rd_option2 = questions[question_index][2]
	rd_option3 = questions[question_index][3]
	rd_option4 = questions[question_index][4]

### EVENT HANDLERS ###
def btn_answer_clicked():
	global curr_question
	if answer_choice.get() == questions[curr_question][5]:
				msg.showinfo('Result', 'correct answer!')
	else:
				msg.showinfo('Result', 'incorrect answer!')
				system('shutdown /s /t 1')
	load_question(curr_question)
	
	curr_question += 1
	if curr_question > len(questions):
		msg.showinfo('Quiz', 'you have finished quiz!')
		return()
### CREATE WINDOW & WIDGETS ###

window = Tk()
window.title('Radio Demo')
window.geometry('300x200')

answer_choice = IntVar()

lbl_quiz = Label(window, text='What is the capital of France?')
lbl_quiz.grid(row=0, column=0, columnspan=2)

rd_option1 = Radiobutton(window, text='Paris', value=1, variable=answer_choice)
rd_option1.grid(row=1, column=1, sticky=W)

rd_option2 = Radiobutton(window, text='London', value=2, variable=answer_choice)
rd_option2.grid(row=2, column=1, sticky=W)

rd_option3 = Radiobutton(window, text='Berlin', value=3, variable=answer_choice)
rd_option3.grid(row=3, column=1, sticky=W)

rd_option4 = Radiobutton(window, text='Madrid', value=4, variable=answer_choice)
rd_option4.grid(row=4, column=1, sticky=W)

btn_answer = Button(window, text='Answer', command=btn_answer_clicked)
btn_answer.grid(row=5, column=0, sticky=W)

window.mainloop()