from random import randint

name = input("type your name: ")
birthdayyear = int(input("your birthday year: "))
year70 = birthdayyear + 70
yearrandom = randint(int(birthdayyear), int(year70))

print("hello "+ name+ "Your lucky year is: "+ str(yearrandom))