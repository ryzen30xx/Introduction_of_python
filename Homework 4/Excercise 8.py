from random import randint
min_number = int(input("enter min number: ")); max_number = int(input("enter max number: ")); condition = int(input("Do you want many random numbers: "))
for i in range(condition):
    randomnumber =  randint(min_number, max_number)
    if randomnumber == 0: print("Bad luck, no random values for you"); exit()
    elif randomnumber == 7: continue
    print(randomnumber)