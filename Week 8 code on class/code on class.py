name = "kien"
name2= "khanh hoang"
number = 18
n_float = 3.14678
print(f'|{name:>8}|') #right align
print(f'|{name:<8}|') #left align
print(f'|{name:^8}|') #center align(delicate 8 to 4 each side)


print("\n\n\ntest difference between string and iteger\n")
print(f'|{name:8}|') #string will be right aligned
print(f'|{number:8}|') #iteger will be left aligned

print("\n\n\n test e func \n")
print(f"{n_float:8.2f}")
print(f"{n_float:8.2e}")
print(f"{n_float:8.2%}") #n_float / 100%


print("\n\n\ntest use up case, low case, title case and swap case")
print(name.lower())
print(name.upper())
print(name.title())
print(name.swapcase())

print("\n\n")
print(len(name))
print(max(name, name2))
print(min(name, name2))
print("\n\n\n")

if name > name2:
	print(f"{name} is greater than {name2}")
else:
	print(f"{name} is less than {name2}")

print("\n\n\n split string\n")

print(name*4)

print(name + " " + name2)
print("\ntest slicing")
between = len(name2) / 2 
print(f"{name2[:int(between)]}")

if "kien" in name.lower():
	print(f"{name} found is lower case!")
else: print("not found")

def test_string():
	msg = input("Enter a sub string")
	i = name.find(msg)
	if i == -1: print(msg, "not found!")
	else: print(f"{msg} in position {i}")

def start_with():
	if name.startswith("k"): print(f"{name} start with k")
	if name.endswith("n"): print(f"{name} end with n")

def remove_space():
	s = "	name	"
	print(s.strip())

def create_list():
	s = "Dinh trung Kien "
	print(f"There are have {len(s.split())} in {s}")
create_list()

