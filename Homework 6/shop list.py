list = ["apple", "break", "milk", "eggs"]; count = 0; wtf_conditional = "WTF_input"
print("Enter the items you want to buy (press Enter to finish):")
for i in list: count += 1; print(f"{count}: {i}")
choose_item = input("Which item? (all/index): ")
if choose_item.replace(" ", "").isalpha() or choose_item.replace(" ", "").isdigit():
    if choose_item.replace(" ", "").isalpha():
        if choose_item.lower() != "all":print(wtf_conditional)
        else: print(f"Your Shopping List: {list}")
    else: 
        print(wtf_conditional) if int(choose_item) > len(list) else print(f"Your item: {list[int(choose_item) - 1]}")
else: print(wtf_conditional)