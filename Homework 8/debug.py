books = ['abc']; authors = ['abc']; genres = ['abc']; pub_years = ['abc']

def search_items(n_genre):
	check = False
	if not books: print("database is empty !")
	elif n_genre not in genres: print("Your search condition is invalid !")
	else:
		for i in range(len(genres)):
			if n_genre == genres[i]:
				print(f"the genre {n_genre} has found: Book: {books[i]} Author: {authors[i]} with public year: {pub_years[i]}")
				check = True
			elif not check:
				print("????")

search_items('a')