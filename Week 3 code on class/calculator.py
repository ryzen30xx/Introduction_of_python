number1 = int(input("insert number 1:")); number2 = int(input("insert number 2:"))
operation = input("Operation [+, -, /, *, %, //, **]:")
if operation not in ["+", "-", "/", "*", "%", "//", "**"]: exit()
elif operation == "+": combination = number1 + number2
elif operation == "-": combination = number1 - number2
elif operation == "/": combination = number1 / number2
elif operation == "*": combination = number1 * number2
elif operation == "%": combination = number1 % number2 #chia lay so du
elif operation == "//": combination = number1 // number2 #chia lay so nguyen
elif operation == "**": combination = number1 ** number2 #boi so
print("answer is:", combination)