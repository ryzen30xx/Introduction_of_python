list = []; count = 0; wtf_conditional = "WTF_input"; condition = True

def add_item(enter_item):
    list.append(enter_item)
    
def alpha_case(choose_item):
    if choose_item.lower() != "all":return(wtf_conditional)
    else: return(f"Your Shopping List: {list}")

def digit_case(choose_item):
    if int(choose_item) > len(list):return(wtf_conditional)
    else: return(f"Your item: {list[int(choose_item) - 1]}")

while condition:
    count += 1
    enter_item = input(f"Enter the item you want to buy (press Enter to finish)[{count}]:")
    if enter_item.replace(" ", "") =="": condition = False
    else: add_item(enter_item)
#to show an items in list
count = 0
for i in list: 
    count += 1 
    print(f"{count}: {i}")


choose_item = input("Which item? (all/index): ")    
if choose_item.replace(" ", "").isalpha() or choose_item.replace(" ", "").isdigit(): #this line will check conditions if input condition is not alpha or not digits, application will be exit
    print(alpha_case(choose_item)) if choose_item.replace(" ", "").isalpha() else print(digit_case((choose_item)))
else: 
    print(wtf_conditional)