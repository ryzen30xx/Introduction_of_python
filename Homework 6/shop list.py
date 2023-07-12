list = []
count  = 0
val = True
def add_item(item):
    list.append(item)

def process(condition):
    if condition == "all":
        return(f"Your Shopping List: {list}")
    elif int(condition) > len(list):
        return("wtf input")
    elif condition.isdigit():
        return(f"Your item: {list[int(condition) - 1]}")

while val:
    item = input("Enter the items you want to buy (press Enter to finish):")
    if item == "":
        val = False
    else:
        add_item(item)
for i in list:
    count += 1
    print(f"Item {count}: {i}")
choose_item = input("Which item? (all/[index]): ")
print(process(choose_item))