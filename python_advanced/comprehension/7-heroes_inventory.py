heroes = input().split(", ")

heroes_inventory = {}
for hero in heroes:
    heroes_inventory[hero] = {}


while True:
    line = input()
    if line == "End":
        break
    tokens = line.split("-")
    name, item, price = tokens
    price = int(price)
    if item not in heroes_inventory[name]:
        heroes_inventory[name][item] = price

for hero in heroes_inventory:
    cost = 0
    for item in heroes_inventory[hero]:
        cost += heroes_inventory[hero][item]
    print(f"{hero} -> Items: {len(heroes_inventory[hero])}, Cost: {cost}" )

