def bank(balance, month):
    if month > 12:
        return "invalid month"
    elif month < 6:
        interest = balance * 5 / 100
        return balance + interest
    else:
        interest = balance * 8 / 100
        return balance + interest
print(bank(int(input("enter your balance: ")), int(input("enter month: "))))