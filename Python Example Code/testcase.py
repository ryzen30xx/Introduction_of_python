import random

random_values = []
for _ in range(10):
    value = random.randint(0, 10)
    if value == 0:
        print("Bad luck, no random values for you")
        break
    elif value == 7:
        continue
    random_values.append(value)

output_string = "Random values: " + ", ".join(str(value) for value in random_values)
print(output_string)