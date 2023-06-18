from random import randint
random_request = int(input("How many times do you want to random:")) 
lowest = int(input("Enter min number: "))
highest = int(input("Enter max number: "))
dict = []
for i in range(random_request):
    random_number = randint(lowest, highest)
    if random_number == 0: 
        print("Bad luck, no random values for you")
        exit()
    elif random_number == 7: 
        continue
    #record to store(dictionary) append have a function is record values to the dictionary
    dict.append(random_number)
print("Random: "+", ".join(str(random_number)for random_number in dict))