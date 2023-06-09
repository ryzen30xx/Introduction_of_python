from tabulate import tabulate

product_name = input("enter name of product: ")
price_of_product = float(input("Price of product:"))
stock = input("Stock: ")
value = int(stock) * int(price_of_product)
# print("-" * 57)
# print (f"|{'name of product':<20}|{'Price':>7}|{'Stock':>10}|{'Value':>20}|")
# print("-" * 57)
# print (f"|{product_name:<20}|{price_of_product:>7}|{stock:>10}|{value:>20}|")
# print("-" * 57)
# print("+" + "-" * 20 + "-" * 20 + "+" + "-" * 20 + "+" + "-" * 20 + "+" + "-" * 20)
value = float(value)
price_of_product = str(price_of_product) + "VND"
value = str(value) + "VND"
data = [[product_name, price_of_product, stock, value]]
head = ["Name of product", "Price of product", "stock", "value"]
print(tabulate(data, headers=head, tablefmt="grid"))