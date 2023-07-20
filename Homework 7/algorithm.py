students = ['John', 'Peter', 'Mary', 'Jane', 'Tom', 'Jerry', 'Alice', 'Bob']
departments = ['IT', 'GD', 'IT', 'Biz', 'Biz', 'GD', 'IT', 'GD']
GPAs = [3.5, 3.0, 3.2, 3.6, 3.8, 3.9, 3.7, 3.4]
def find_student(): #find GPAs and departments with student name
	i = 0
	s_name = input("Enter student name: ")
	if len(s_name) == 0:
		return("invalid input")
	else:
		for k in students:
			if k == s_name:
				print(f'finished search! \n Student name: {s_name}, GPAs Score: {GPAs[i]}, Department: {Departments[i]}')
			i += 1

def find_department(): #query GPAs, name student with Department name
	i = 0
	s_department = input("Enter department name: ")
	if len(s_department) == 0:
		print("invalid input")
	else:
		print(f'Find student and GPAs with department {s_department}')
		for k in departments:
			if s_department == k:
				print(f"Student Name: {students[i]}, GPAs: {GPAs[i]}")
				i += 1

def best_student(): #find best student with condition is highest GPA score 
	i = GPAs[0]
	j = 0
	for k in GPAs:
		if k > i: i = k; n_find = j
		j += 1
	print(f"Best student is: {students[n_find]} with GPAs: {GPAs[n_find]} in department: {departments[n_find]}")

def find_gpa(): #find GPA in database is same or better than
	i = 0
	gpa_enter = float(input("Enter GPA to find same or more than: "))
	for k in GPAs:
		if k >= gpa_enter: print(f"Student {students[i]} with GPAs: {GPAs[i]} in department: {departments[i]}")
		i += 1

def average_gpa(): #calculate average score on all department
	total = 0
	for i in GPAs:
		total += i
	print(f"Average score in all apartment is: {str((total / len(GPAs)))[0:4]}")

def average_gpa_depart(): #calculate average score of some department
	i = 0
	total_score = 0
	enter_depart = input("Enter department you want calculate average score: ")
	if enter_depart not in departments:
		print("invalid input")
	else:
		for j in departments:
			if enter_depart == j:
				total_score += GPAs[i]
				i += 1
		print(f"Average score of {enter_depart} is: {str(total_score / i)[0:5]}")