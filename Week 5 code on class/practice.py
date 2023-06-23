def print_slogan(slogan, symbol):
    n = len(slogan) + 2
    print(symbol * n)
    print(f"{symbol}{slogan}{symbol}")
    print(symbol * n)
print_slogan(input("Enter your name: "), "+")