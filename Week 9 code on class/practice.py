from os import system
from time import sleep
prod = {}

def add_product(n_product, price):
	if n_product == "" or price == "":return("input value must be not empty!")
	else:
		if n_product in prod: print(f"{n_product} already exist in system !")
		else: prod[n_product] = price

def edit_product(n_product, price):
	if len(prod) == 0: return(f"your database of product is empty, pls add product before edit!")
	else:
		if n_product == "" or price == "": return("input value must be not empty!")
		else:
			if n_product not in prod: print(f'{n_product} not in system for editable!')
			else: prod[n_product] = price
	sleep(2)

def delete_product(n_product):
	if n_product == "": return("input value must be not empty!")
	else:
		if n_product not in prod: return(f"{n_product} not in system to delete!")
		else: prod.pop(n_product); print(f'{n_product} has been deleted !')
	sleep(2)

def filter_product(price):
	for p_name, f_price in prod.items():
		if f_price >= price:
			print(f'{p_name} - {f_price}')
	sleep(2)

def print_all():
	count = 0
	for prod_name, prod_price in prod.items():
		count += 1
		print(f"{count}: {prod_name} - {float(prod_price)}")
		print("wait 4 seconds for back to menu")
		sleep(4)

while True:
		system('clear')
		print(f"1: Add product \n2: edit product \n3: delete product \n4: filter product \n5: print all product \n0: Exit program")
		choose = input("Enter your choose: ")
		if choose == "0": print("exit program!"); exit()
		elif choose == "1": add_product(input("Enter product name you want add to system: "), input("Enter price: "))
		elif choose == "2": edit_product(input("enter name product you want to edit price: "), input("enter new price: "))
		elif choose == "3": delete_product(input("Enter name product you want to delete:"))
		elif choose == "4": filter_product(input("Enter minimum price to print product equal or better than: "))
		elif choose == "5": print_all()
		else: print("wrong input!")
