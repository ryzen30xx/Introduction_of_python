students = []
gpas = []
def function_list():
	print("List of function \n 1. Add student \n 2. Delete student\n 3. Edit student\n 4. Search student\n 5. Print all student in system\n 6. exit program")

def add_student(names, gpa):
	if gpas == "" or names == "":
		print("invalid input")
	else:
		students.append(names)
		gpas.append(float(gpa))
		print(f"Add Student{names} finished!")

def edit_student(name, gpa):
	if students.find(name):
condition = True
while condition:
	function_list()
	if choose == 1: add_student(input("Enter student name you want to add\n(add ',' after each student name if you want add more than 1 student): "), input("Enter GPA of this student"))
	elif choose == 2: delete_student(input("Enter name of student you want to delete: "))
	elif choose == 3: edit_student(input("Enter name of student you want to edit: "))
	elif choose == 4: search_student(input("Enter name of student to search score: "))
	elif choose == 5: print_all_student()
	elif choose == 6: print("Appication exiting..."); condition = False
	else: print("Invalid input!")
