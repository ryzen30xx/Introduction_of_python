guest_list = []
print ("Welcome to the Party!")
guest_party = int(input("How many guests will be attending the party? "))
def remove_guest(guest_remove):
    guest_list.remove(guest_remove)
for i in range(1, guest_party + 1):
    guest_name = input(f"Enter the name of guest {i}: ")
    guest_list.append(guest_name)
print(f"The final guest list is: {guest_list}")

condition = input("Do you want to remove any guests from the list? (yes/no): ")
if condition.lower() == "yes":
    name_guest = input("Enter the name of the guest to remove:")
    remove_guest(name_guest)
    print(f"Guest {name_guest}' has been removed from the list.")
    print(f"The updated guest list is: {guest_list}")