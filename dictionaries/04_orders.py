from collections import defaultdict

products = defaultdict(int)
prices = defaultdict(float)

while True:
    command = input()
    if command == "buy":
        break
    tokens = command.split()
    name = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])
    products[name] += quantity
    prices[name] = price

for product, price in prices.items():
    print(f"{product} -> {(price * products[product]):.2f}")
