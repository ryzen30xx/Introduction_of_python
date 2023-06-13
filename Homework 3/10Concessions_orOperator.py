name = input("What is your name? ")
message = f"Hello {name}"
if name == "Chris": message += " - congratulations, you are entitled to a 30% discount"
else: message += " - sorry, you must pay the regular price"
print(message)