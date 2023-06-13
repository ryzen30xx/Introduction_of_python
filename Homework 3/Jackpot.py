from random import randint
luckynumber = randint(1, 10)
if luckynumber == 3 or luckynumber == 9: messange = f"your lucky number is {luckynumber}and you have won a prize"
elif luckynumber == 7: messange = f"your lucky number is {luckynumber} and you have hit the jackpot"
print ("Hello", input("Enter your name: "), messange)