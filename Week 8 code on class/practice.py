def shopping():
	product_name = input("enter name of product: ")
	price = float(input("enter price: "))
	VAT = 2
	print(f"Your invoice:\n {'product':<10}: {product_name:>10}\n {'Price':<10}: {price:>10}\n {'VAT':<10}: {float(VAT):>10}\n {'Total':<10}: {float(price + VAT):>10}")
def practice():
	fruit = input("Enter fruit name: ").split(",")
	print(f"There are have {len(fruit)} fruits")
	fave_fruit = input("enter your favourite fruit")
	if fave_fruit not in fruit: print(f"{fave_fruit} not found in list")
	else: print(f"{fave_fruit} found in list")
	
practice()
