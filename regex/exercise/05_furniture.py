import re


pattern = r"(^>>)(?P<product>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<amount>\d+)($|\s)"
products = []
total = 0

while True:
    line = input()
    if line == "Purchase":
        break
    matches = re.finditer(pattern, line)
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        products.append(obj["product"])
        total += float(obj["price"]) * int(obj["amount"])

print("Bought furniture:")

for p in products:
    print(p)

print(f"Total money spend: {total:.2f}")
