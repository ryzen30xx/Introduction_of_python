def triangle(symbol, n):
    symbol += " "
    for i in range(1, n+1):
        print(f"{symbol * i}")
triangle(input("Enter your symbol you want to print: "), int(input("Do you want to print how many times: ")))