guest_list = []
guest_num  = int(input("How many guests will be attending the party? "))

for i in range(1, guest_num + 1): guest_list.append(input(f"Enter the name of guest {i}:"))

print(f"The added guest list is: {guest_list}")

remove_question = input("Do you want to remove any guests from the list? (yes/no): ")

if remove_question.lower == "yes":
    guest_remove = input("Enter the name of the guest to remove: ")
    if guest_remove not in guest_list:
        print("wtf guest ?") 
    else: 
        #list.remove to remove element from guest list
        guest_list.remove(guest_remove)
        print(f"Guest {guest_remove} has been removed from the list.")
        print(f"The updated guest list is: {guest_list}")
else: print(f"Last guest list: {guest_list}")