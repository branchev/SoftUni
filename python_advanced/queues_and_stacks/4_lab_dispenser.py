from collections import deque

water_amount = int(input())

people = deque()
while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

while True:
    line = input()
    if line == "End":
        break
    if line.startswith("refill"):
        water_amount += int(line.split()[1])
    else:
        asked_liters = int(line)
        if asked_liters <= water_amount:
            water_amount -= asked_liters
            print(f"{people.popleft()} got water")
            continue
        print(f"{people.popleft()} must wait")

print(f"{water_amount} liters left")