n = int(input("Enter n:"))
s = 1
for i in range(n+1):
    for j in range(i+1):
        print(j, end=" ")
    print()