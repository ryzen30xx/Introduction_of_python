n = int(input("Enter n:"))

for i in range(n + 1):
    for j in range(i):
        print(f"{i} ", end ="")
    print()