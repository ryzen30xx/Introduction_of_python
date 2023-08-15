languages = open('languages.txt', 'r')
authors = open('authors.txt', 'r')
agencies = open('agencies.txt', 'r')
new_file = open('new file.txt', 'a')
import os

def read_language():
	languages =  language.read().split('\n')
	print(len(languages))
	for i in language:
		print(i)
	languages.close()

def read_all_language():
	languages.close()
	
	for i in language.readlines():
		print(f'{i.strip()}')

def find_character():
	

	for i, line in enumerate(agencies.readlines()):
		if 'Authority' in line:
			print(i+1, line)

def enter_file():
	file_name = input('enter file link: ')
	condition = True
	while condition:
		try:
			read_file = open(file_name, 'r')
			condition = False
		except FileNotFoundError:
			print("File not found, please try again !")

	for i, line in enumerate(read_file.readlines()):
		if 'Authority' in line:
			print(i+1, line)

def read_folder(path):
	if os.path.isdir(path):
		list_path = os.listdir(path)
		for i in list_path:
			read_folder(path + '/' + i)
			print(path)

def example(path):
	if os.path.isdir(path):
		print('+', path.split('/')[-1])
	else:
		print('-', path.split('/')[-1])
	if os.path.isdir(path):
		list_path = os.listdir(path)
		for i in list_path:
			read_folder(path + '/' + i)


def modify_and_write():
	
	for i in authors.readlines():
		n_filter = i.split('<', -1)
		for i in range(len(n_filter)):
			if i == 0:
				name = n_filter[0]
				print('', name.strip(), end="")
				new_file.write(name.strip() + ':')
			if i == 1:
				email = n_filter[i]
				print(': ', email.strip().strip('>'))
				if 'gmail' in email:
					new_file.write(' '+email.strip().strip('>')+'\n')
	new_file.close()

#example('/mnt/c/Users/RYZEN30xx')
modify_and_write()