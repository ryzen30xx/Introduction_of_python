name = str(input("Enter your name: "))
#name.isalpha to compare name string is alpha case or not
#.replace(condition, new_condition) to replace if string have value like first condition
while name.replace(" ","").isalpha():
    student_operation = input("Are you student[y/n]: ").lower()
    if student_operation == "y":
        print(f"Hello {name}, congratulations, you are entitled to a 10% discount")
    else: 
        print(f"Hello {name}, sorry you must pay the regular price")
    name = str(input("Please enter your name[or enter blank to exit]: "))
    if name == "" or name == " " or not name.replace(" ","").isalpha(): 
        break
print("Good Bye!")
# not name.isalpha() to check name variable is alpha or not to advoid loops(for if else or something like that)