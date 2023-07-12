list = []; count = 0; wtf_conditional = "WTF input"; accept = True
print("Welcome to the Grocery Store! \nEnter the items you want to buy (press Enter to finish):")
while accept: 
    count += 1
    insert_item = input(f"Item {count}:")
    if insert_item != "": list.append(insert_item)
    else: accept = False
count = 0
for i in list: count += 1; print(f"{count}: {i}")
choose_item = input("Which item? (all/index): ")
if choose_item.replace(" ", "").isalpha() or choose_item.replace(" ", "").isdigit():
    if choose_item.replace(" ", "").isalpha(): print(wtf_conditional) if choose_item.lower() != "all" else print(f"Your Shopping List: {list}")
    else: print(wtf_conditional) if int(choose_item) > len(list) else print(f"Your item: {list[int(choose_item) - 1]}")
else: print(wtf_conditional)