from random import randint 
name = input("type your name: ") 
birthdayyear = int(input("your birthday year: ")) 
print("hello ", name, "Your lucky year is: ", randint(int(birthdayyear), birthdayyear + 70))