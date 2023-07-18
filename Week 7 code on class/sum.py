from random import sample as sp
groceries = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
price = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stock = [1, 2, 3, 4, 5, 6, 7, 8, 9]
students = ["John", "Peter", "Mary", "Jane", "Tom", "Jerry", "Alice", "Bob"]
Department = ["IT", "GD", "IT", "Biz", "Biz", "GD", "IT", "GD"]
GPAs = [3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
numbers = sp(range(10, 100), 10)#generate a random number from 10 to 100 and step 10
print(numbers)
s = 0
#find sumarize number
for i in numbers:
    s += i # plus number of digits
print(s)
#find max number of digits
m = numbers[0]
print(m)
for n in numbers:
    if n < m: m = n
print (m)
def find_max_price():
    i_max = 0
    price_max = price[0]
    for i in range(len(price)):
        if price[i] < price_max: price_max = price[i]; i_max = i
        print(i_max)
    return(f"The fruit that has the highest price is {groceries[i_max]} with price {price_max}")
def find_even_number():
    count = 0
    for i in price:
        if i % 2 == 0: count += 1
    return count
def find_price_product():
    i_product = groceries[0]
    i = 4
    count = 0
    i_price = price[0]
    i_stock =  stock[0]
    for f in stock:
        if f > i: i = f; count += 1
    return(f"product{groceries[count]} price{price[count]} stock{stock[count]}")
def search():
    product = input("Enter Product: ")
    found_pos = 0
    count = 0
    for i in groceries:
        if product == i:
            found_pos = count
            break
        count += 1
    if found_pos == None:
        return(f"Product {product} not found")
    else: return(f"Price: {price[found_pos]} Prod: {groceries[found_pos]} Stock: {stock[found_pos]},")
def track_product():
    #find products have values >= 4
    j = 0
    k = 0
    list_product = []
    mark = price[0]
    for i in price:
        total = price[k] * stock[k]
        if total >= 12:
            print(total)
            list_product.append(groceries[k])
        k += 1
    return(f"product:{list_product}")
def student(condition):#search
    def student_search():
        k = 0
        name = input("Enter name of student: ")
        for i in students:
            if i == name:
                break
            k += 1
        return(f"Student name: {students[k]} Department: {Department[k]} GPA: {GPAs[k]}")
    
    def department_search():
        k = 0
        department_name = input("Enter department to search: ")
        for i in Department:
            if i == department_name:
                return_value = k
                print(f"Student name: {students[k]} Department: {Department[k]} GPA: {GPAs[k]}")
            k += 1
    def best_student():
        k = 0
        max_gpas = GPAs[0]
        for i in GPAs:
            if i > max_gpas:
                max_gpas = i
            k += 1
    if condition == 1:
        print(student_search())
    elif condition == 2:
        print(department_search())

student(2)
