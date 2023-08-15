sell_list = {'hackintosh' : 20.0, 'Phuong' : 20}
from time import sleep
def total_sales():
	print(f"Sold list")
	for name, price in sell_list.items():
		print(f"- Book {name} sold with price {price}")
	sleep(2)
total_sales()