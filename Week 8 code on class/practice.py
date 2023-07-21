product_name = input("enter name of product: ")
price = float(input("enter price: "))
VAT = 2
print(f"Your invoice:\n {'product':<10}: {product_name:>10}\n {'Price':<10}: {price:>10}\n {'VAT':<10}: {float(VAT):>10}\n {'Total':<10}: {float(price + VAT):>10}")
