from os import system
students = []
gpas = []
class bcolors: HEADER = '\033[95m'; OKBLUE = '\033[94m'; OKCYAN = '\033[96m'; green = '\033[92m'; warning = '\033[93m'; red = '\033[91m'; end = '\033[0m'; BOLD = '\033[1m'; UNDERLINE = '\033[4m'
condition = True
def function_list():
	print("List of function \n 1. Add student \n 2. Delete student\n 3. Edit student\n 4. Search student\n 5. Print all student in system\n 6. exit program")

def add_student(names, gpa):
	for n_name in names:
		if n_name == "": #error check case with empty input
			print("Something went wrong with input string")
			input("press enter to back")
			return
		else:
			if len(names) != len(gpa):
				print(f"WTF Request ?Count of student name is: {len(names)} and count of score is: {len(gpa)}")
			else:
				if n_name in students:
					print(f"{bcolors.red}student {n_name} has already exist!{bcolors.end}")
				else:
					students.append(n_name)
					print(f"{bcolors.green}Student {bcolors.warning}{n_name}{bcolors.green} added successful!{bcolors.end}")
				for i in gpa:
					if i:
						gpas.append(float(i))
					else:
						gpas.append(0.0)
	input(bcolors.warning+"press enter to back"+bcolors.end)

def delete_student(names, gpa): #need to fix
	for i in names:
		for j in range(len(students)):
			if i == students[j]: students.pop[j]; gpas.pop[j]

def edit_student(name, gpa):
	if students.find(name) == -1: print("Invalid Student !")
	else: gpas.replace(students.find(name), gpa)
	input()

def print_all_student():
	print("All students in system")
	for i in range(len(students)):
		print(f"student: {bcolors.green}{students[i]}{bcolors.end} with GPA: {bcolors.green}{gpas[i]}{bcolors.end}")
	input()

while condition:
	system("clear")
	print(bcolors.HEADER+"Student Management System"+bcolors.end)
	function_list()
	choose = int(input("enter function you want to execute: "))
	if choose == 1: add_student(input("Enter student name you want to add\n(add ',' after each student name if you want add more than 1 student): ").split(","), input("Enter GPA of this student\nif you skip this step, normal score will be set to zero\n(add , symbol if you want add more than one score): ").split(","))
	elif choose == 2: delete_student(input("Enter name of student you want to delete: "))
	elif choose == 3: edit_student(input("Enter name of student you want to edit: "), float(input("Enter GPA you want to change: ")))
	elif choose == 4: search_student(input("Enter name of student to search score: "))
	elif choose == 5: print_all_student()
	elif choose == 6: print(bcolors.red+"Appication exiting..."); condition = False
	else: print(warning+"Invalid input!")