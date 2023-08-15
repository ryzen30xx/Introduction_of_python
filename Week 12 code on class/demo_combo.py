from tkinter import *
from tkinter.ttk import Combobox
import time
#Event Handlers#
time = time.time()
#create window
window = Tk()
window.title("hackintosh Demo combobox")
window.geometry('400x300')

#crate widgets
lbl_table = Label(window, text="Enter your favorite film: ")
lbl_table.grid(row=0, column=0, columnspan=2, sticky=EW)

movie_list = ['The Matrix', 'Roll Royce & Prado Sport', 'Civic with he best friend', \
            'Interstellar']
movies_dict = {'The Matrix': ['Lana Wachowski, Lilly Wachowski', 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss'], \
                'The Lord of the Rings': ['Peter Jackson', 'Elijah Wood, Ian McKellen, Orlando Bloom'], \
                'The Dark Knight': ['Christopher Nolan', 'Christian Bale, Heath Ledger, Aaron Eckhart'], \
                'Inception': ['Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'], \
                'Interstellar': ['Christopher Nolan', 'Matthew McConaughey, Anne Hathaway, Jessica Chastain']}

def check_film(event):
    movie = cbb_movie.get()
    director = movies_dict[movie][0]
    actor = movies_dict[movie][1]
    lbl_director['text'] = director
    lbl_actor['text'] = actor

cbb_movie = Combobox(window, values=movie_list)
cbb_movie.grid(row=1, column=0, sticky=W)
cbb_movie.bind('<<ComboboxSelected>>', check_film)

lbl_info = Label(window, text="Movie Information: ")
lbl_info.grid(row=2, column=0, sticky=W)

lbl_director = Label(window, text="Director: ")
lbl_director.grid(row=3, column=0, columnspan=2, sticky=W)

lbl_actor = Label(window, text="Actor: ")
lbl_actor.grid(row=4, column=0, columnspan=2, sticky=W)


window.mainloop()