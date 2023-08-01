dict = {
	'4jghufus342jkh' : 'ishar',
	'abcxyz' : 'ryzen30xx',
}

def find_val():
	found = input("Enter your key to query val in dictionary: ")
	if found not in dict: print("wtf input!")
	else: print(dict[found])

def add_val():
	n_key = input("Enter new key: ")
	n_val = input("Enter new valriable: ")
	if n_key in dict:print(f"{n_key} already exist in dictionary!")
	else: dict[n_key] = n_val

def modify_val():
	n_key = input("enter key you want modify: ")
	if n_key not in dict: print(f"{n_key} not in dictionary to modify! ")
	else: n_val = input("Enter new variable: "); dict[n_key] = n_val; print(dict)

def delete_val():
	d_key = input("enter key you want to delete: ")
	if d_key not in dict: print(f"{d_key} not in dictionary!")
	else: del dict[d_key]

def except_practice():
	#while True:
		try:
			a = int(input("enter integer number: "))
		except ValueError as e:
			print("Value Error", e) #to print error with value