#enter credit scores and how many cash you want to loan
incomes = int(input("Enter your income: ")); credit_scores = int(input("Enter your credit score: "))
if incomes < 0 or credit_scores < 0: print("wrong variable! Please re-enter your income and credit scores")
elif incomes >= 100000 and credit_scores >= 700: print("You are eligible for a loan with the lowest interest rates.")
elif incomes >= 50000 and credit_scores >= 700: print("You are eligible for a loan with low interest rates.")
elif incomes >= 30000 and credit_scores >= 500: print("You are eligible for a loan with moderate interest rates.")
else: print("Sorry, you are not eligible for a loan at this time.")