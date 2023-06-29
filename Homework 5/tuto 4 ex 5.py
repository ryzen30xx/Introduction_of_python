from random import randint
def random(minimum, maximum):
    if minimum == "" and maximum != "":
        minimum = 1
        if int(maximum) > int(minimum): 
            for i in range(4): return(randint(int(minimum), int(maximum)))
        else: return(f"Maximum less than minimum !")
    if minimum != "" and maximum != "":
        if minimum < maximum: return(randint(int(minimum), int(maximum)))
        else: return(f"Maximum less than minimum !")
    elif minimum == "" and maximum == "":
        minimum = 1; maximum = 100
        for i in range(4): return(randint(minimum, maximum))
    else:
        if int(maximum) > int(minimum): 
            for i in range(4): return(randint(int(minimum), int(maximum)))
        else: return(f"Maximum less than minimum! Pls check your insert")
print(random(input("Enter the minimum number:"), input("Enter the maximum number:")))