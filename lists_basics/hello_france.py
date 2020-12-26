# Type	            Maximum Price
# Clothes	        50.00
# Shoes	            35.00
# Accessories	    20.50

def validator(product_type, price):
    if product_type == "Clothes" and price <= 50:
        return True
    if product_type == "Shoes" and price <= 35:
        return True
    if product_type == "Accessories" and price <= 20.5:
        return True
    return False


shopping_list = input().split("|")
starting_budget = float(input())
budget = starting_budget

my_price_list = []

for product in shopping_list:
    tokens = product.split("->")
    product_type = tokens[0]
    price = float(tokens[1])
    if validator(product_type, price) and budget - price >= 0:
        my_price_list.append(price)
        budget -= price
    else:
        continue

profit = sum([round(price*0.4, 2) for price in my_price_list])
my_price_list = [round(pr*1.4, 2) for pr in my_price_list]

print(" ". join([str(pr) for pr in my_price_list]))
print(f"Profit: {profit:.2f}")

if profit + starting_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
