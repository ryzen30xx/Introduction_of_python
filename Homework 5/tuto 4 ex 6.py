def get_message(name, age, condition):
    if condition in ['y', 'yes'] and (age <= 18 or age >= 65): return (f"Hello {name} - congratulations, you are entitled to a 20% discount")
    elif condition in ['y', 'yes'] or (age <= 18 or age >= 65): return (f"Hello {name} - - congratulations, you are entitled to a 10% discount")
    else: return (f"Hello {name} - sorry, you must pay the regular price")
print(get_message(input("Please enter your name: "), int(input("Enter your age: ")), input("You are student (y/n)").lower()))