list = ["apple", "bread", "milk", "eggs"]; count = 0; wtf_conditional = "WTF_input"
print("Enter the items you want to buy (press Enter to finish):")
#to show an items in list
for i in list: 
    count += 1 
    print(f"{count}: {i}")

choose_item = input("Which item? (all/index): ")
if choose_item.replace(" ", "").isalpha() or choose_item.replace(" ", "").isdigit(): #this line will check conditions if input condition is not alpha or not digits, application will be exit
    if choose_item.replace(" ", "").isalpha():
        if choose_item.lower() != "all":print(wtf_conditional)
        else: print(f"Your Shopping List: {list}")
    else: 
        if int(choose_item) > len(list):
            print(wtf_conditional) 
        else: print(f"Your item: {list[int(choose_item) - 1]}")
else: print(wtf_conditional)