list = ["apple", "bread", "milk", "eggs"]; count = 0; wtf_conditional = "WTF_input"
print("Enter the item you want to buy (press Enter to finish):")
#to show an items in list
for i in list: 
    count += 1 
    print(f"{count}: {i}")

def alpha_case(choose_item):
    if choose_item.lower() != "all":return(wtf_conditional)
    else: return(f"Your Shopping List: {list}")

def digit_case(choose_item):
    if int(choose_item) > len(list):return(wtf_conditional)
    else: return(f"Your item: {list[int(choose_item) - 1]}")

choose_item = input("Which item? (all/index): ")    
if choose_item.replace(" ", "").isalpha() or choose_item.replace(" ", "").isdigit(): #this line will check conditions if input condition is not alpha or not digits, application will be exit
    print(alpha_case(choose_item)) if choose_item.replace(" ", "").isalpha() else print(digit_case((choose_item)))
else: 
    print(wtf_conditional)