books = []; authors = []; genres = []; pub_years = []

def add_item(n_book, n_auth, n_genre, p_year):
	if n_book == "" or n_auth == "" or n_genre == "" or p_year == "": print("pls check your enter!s")
	else:	books.append(n_book); genres.append(n_genre); authors.append(n_auth); pub_years.append(p_year); print(f"Book {n_book} added!")
	

def remove_item(n_book):
	if not books:
		print("There do not have any book!")
	else:
		for i in range(len(books)):
			if n_book == books[i]:
				books.pop(i); authors.pop(i); genres.pop(i); pub_years.pop(i); print(f"The books {n_book} has been deleted !")

def edit_item(n_book, n_auth, n_genre, p_year):
	if not books:
		print("Book list in database is empty !")
	elif n_book not in books: print(f"the book {n_book} not in database to modify !")
	else:
		for i in range(len(books)):
			if n_book == books[i]:
				authors[i] = n_auth; genres[i] = n_genre; pub_years[i] = p_year; print(f"update book's title {n_book} successfully")

def search_items(n_genre):
	if not books: print("database is empty !")
	elif n_genre not in genres: print("Your search condition is invalid !")
	else:
		for i in range(len(genres)):
			if n_genre == genres[i]:
				print(f"the genre {n_genre} has found: Book: {books[i]} Author: {Author[i]} with public year: {pub_years[i]}")