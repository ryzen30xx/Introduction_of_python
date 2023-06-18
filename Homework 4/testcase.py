dict = ['Nguyen Van A', 'nguyen van a', 'nguyenvana', '123456', '1 2 3 4 5 6', '. . . . . . . . . . . . . . . . . .']
def testcase(name, student_operation):
        while name.replace(" ","").isalpha():
            student_operation = input("Are you student[y/n]: ").lower()
            print(f"Hello {name}, congratulations, you are entitled to a 10% discount") if student_operation == "y" else print(f"Hello {name}, sorry you must pay the regular price")
            name = str(input("Please enter your name[or enter blank to exit]: "))
            if name == "" or name == " " or not name.replace(" ","").isalpha(): break
        print("Good Bye!")

for i in dict:
      testcase(i.strip(), 'y')