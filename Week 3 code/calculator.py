number1 = int(input("insert number 1:")); number2 = int(input("insert number 2:"))
operation = input("Operation [+, -, /, *, %, //, **]:")
if operation == "+": combination = number1 + number2
if operation == "-": combination = number1 - number2
if operation == "/": combination = number1 / number2
if operation == "*": combination = number1 * number2
if operation == "%": combination = number1 % number2
if operation == "//": combination = number1 // number2
if operation == "**": combination = number1 ** number2
print("answer is:", combination)