from os import system
from time import sleep

book_list = {}
sell_list ={}

def print_menu():
	print("1: Add book")
	print("2: Edit a book's price")
	print("3: Search book (by name)")
	print("4: Sell a book")
	print("5: Show total sales")
	print("6: Print all books")
	print("7: Quit")

def book_management():
	
	while True:
		system('clear')
		print_menu()

		try:
			condition = int(input("Enter your choose: "))
			if condition >= 8 or condition <= 0: 
				print("Wrong input! wait 2 seconds to re-enter")
				sleep(2)
				system('clear')
			elif condition == 1: add_book()
			elif condition == 2: edit_book()
			elif condition == 3: Search_book()
			elif condition == 4: sell_book()
			elif condition == 5: total_sales()
			elif condition == 6: print_all()

		except ValueError:
			print("Wrong input! your enter must be integer number")
			sleep(1)

#functions
def add_book():
	system('clear')

	n_book = input("Enter book's name to add: ")
	if n_book in book_list:
		return("book already exist in system !")
	else:
		try:
			n_price = float(input("enter price of book: "))
			book_list[n_book] = n_price
			print(f"Inport book '{n_book}' successfully !")
			input("Press enter for back to menu")
		except ValueError:
			print("Price enter must be integer number !"); sleep(2)

def edit_book():
	system('clear')
	n_book = input("Enter book's name you want to edit price: ")
	if n_book not in book_list:
		print(f'Book name {n_book} not in system so you can not edit !')
	else:
		try:
			n_price = float(input("Enter new price: "))
			book_list[n_book] = n_price
			print(f"Book {n_book} has been update price to {n_price} successfully !")
			input("Press enter for back to menu")
		except ValueError:
			print("your enter must be integer number !")
			sleep(2)

def Search_book():
	system('clear')
	s_book = input("enter book name you want to search: ")
	if s_book not in book_list:
		print("Your book want to search don not exist in system !")
		sleep(1)
	else:
		print(f"Book {s_book} with price: {book_list[s_book]}")
		input("Press enter for back to menu")

def sell_book():
	system('clear')
	s_book = input("Enter book's name you want to sell: ")
	if s_book not in book_list:
		print("book you want to sell must be exist in system !")
		sleep(1)
	else:
		sell_list[s_book] = book_list[s_book]
		book_list.pop(s_book)
		print(f"Book {s_book} sold successfully !")
		input("Press enter for back to menu")

def total_sales():
	system('clear')
	n_price = 0
	if not sell_list:
		print("You haven't sold any books yet !")
	else:
		print(f"Sold list")
		for name, price in sell_list.items():
			n_price += price
			print('_' * (len(name + str(price)) + 23))
			print(f"|Book {name} Sold with price {price}|")
			print('-' * (len(name + str(price)) + 23))

		print(f"\n|You earned {n_price} with a job selling books !|")

	input("Press enter for back to menu")

def print_all():
	system('clear')
	if not book_list:
		print("Empty database !")
	else:
		for name, price in book_list.items():
			print('_' * (len(name + str(price)) + 9))
			print(f"|{name:^10}:{price:^10}|")
			print('-' * (len(name + str(price)) + 9))
	input("Press enter for back to menu")



# in this code, I using (__name__ == '__main__') to separate the running code and the function declaration
if __name__ == '__main__': 
	book_management()