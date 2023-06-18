row = int(input("Enter number of rows:")); collumns = int(input("Enter number of collumns:"))
#collumns calculation
for i in range(collumns): 
    for j in range(row): print("*", end="") 
    for k in range(row): print("=", end="")
    print()