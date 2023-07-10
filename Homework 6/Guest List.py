guest_list = []
guest_num  = int(input("How many guests will be attending the party? "))

for i in range(1, guest_num + 1): guest_list.append(input(f"Enter the name of guest {i}:"))
print(f"The final guest list is: {guest_list}")
remove_question = input("Do you want to remove any guests from the list? (yes/no): ")
guest_remove = input("Enter the name of the guest to remove: "); print("wtf guest ?") if guest_remove not in guest_list else guest_list.remove(guest_remove);print(f"Guest {guest_remove} has been removed from the list.");print(f"The updated guest list is: {guest_list}") if remove_question.lower == "yes" else print(f"Last guest list: {guest_list}")