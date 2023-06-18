from random import randint; min_str = input("Min: "); max_str = input("Max: "); minimum = int(min_str); maximum = int(max_str)
for i in range(5): print(randint(int(minimum), int(maximum)))