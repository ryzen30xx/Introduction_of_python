users = int(input("Please insert your age: "))
if users < 0 or users > 100: 
    print("wrong age!")
    exit()
elif users == 20: 
    print("You are eligible to apply for a driver's license.")
    print("You need to be at least 21 years old to rent a car.")
elif 18<= users <= 19: 
    print("You are eligible to apply for a driver's license.")
elif users < 18: 
    print("You are not eligible to apply for a driver's license.")
else: 
    print("You are eligible to apply for a driver's license.")
    print("You are also eligible to rent a car.")