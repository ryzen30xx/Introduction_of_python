def input_int(prompt):
    string = input(prompt)
    number = int(string)
    return number


def output(parameter1, parameter2):
    print(f"{parameter1} {parameter2}")


number1 = input_int(" First number: ")

number2 = input_int("Second number: ")

operation = input("Operation [+, -]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2

output("Answer:", combination)

print()
input("Press return to continue ...")
