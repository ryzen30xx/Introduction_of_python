books = []; authors = []; genres = []; pub_years = []

def add_item(n_book, n_auth, n_genre, p_year):
	if n_book == "" or n_auth == "" or n_genre == "" or p_year == "": return("Wrong input")
	else:	books.append(n_book); genres.append(n_genre); authors.append(n_auth); pub_years.append(p_year); print(f"Book {n_book} added!")
	

def remove_item(n_book):
	if len(books) == 0:
		print("There do not have any book!")
	else:
		for i in range(len(books)):
			if n_book == books[i]:
				books.pop(i); authors.pop(i); genres.pop(i); pub_years.pop(i); 

def edit_item(n_book, n_auth, n_genre, p_year):
	