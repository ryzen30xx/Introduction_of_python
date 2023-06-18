row = int(input("Enter number of rows:")); collumns = int(input("Enter number of collumns:"))
#collumns calculation
for i in range(collumns +1): 
    for j in range(row + 1): print("*", end="") 
    for k in range(row + 1): print("=", end="")
    print()