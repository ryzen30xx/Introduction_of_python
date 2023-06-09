def input_and_convert(prompt, conversion_fn):
    string = input(prompt)
    number = conversion_fn(string)
    return number


def calculate(fish, cornflake, teatray):
    if teatray == "+":
        flipflop = fish + cornflake
    elif teatray == "-":
        flipflop = fish - cornflake
    return flipflop


def output(parameter1, parameter2):
    print(f"{parameter1} {parameter2}")


number1 = input_and_convert(" First number: ", int)

number2 = input_and_convert("Second number: ", int)

operation = input_and_convert("Operation [+, -]: ", str)

combination = calculate(number1, number2, operation)

output("Answer:", combination)

print()
input("Press return to continue ...")
