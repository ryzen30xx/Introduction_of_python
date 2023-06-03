from random import randint

name = input("type your name: ")
birthdayyear = int(input("your birthday year: "))
yearrandom = randint(int(birthdayyear), birthdayyear + 70)

print("hello "+ name+ "Your lucky year is: "+ str(yearrandom))