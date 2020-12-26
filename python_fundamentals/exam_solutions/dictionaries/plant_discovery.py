n = int(input())

plants = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant] = {}
    plants[plant]['rarity'] = rarity
    plants[plant]['ratings'] = []

while True:
    line = input()
    if line == "Exhibition":
        break
    tokens = line.split(": ")
    command = tokens[0]
    try:
        if command == "Rate":
            plant, rating = tokens[1].split(" - ")
            rating = int(rating)
            plants[plant]['ratings'].append(rating)
        elif command == "Update":
            plant, rarity = tokens[1].split(" - ")
            rarity = int(rarity)
            plants[plant]['rarity'] = rarity
        elif command == "Reset":
            plant = tokens[1]
            plants[plant]['ratings'].clear()
    except:
        print("error")


for pl in plants:
    if plants[pl]['ratings']:
        rate = sum(plants[pl]['ratings']) / len(plants[pl]['ratings'])
        rate = round(rate, 2)
        plants[pl]['ratings'] = rate
    else:
        plants[pl]['ratings'] = round(0, 2)


sorted_plants = sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['ratings']))

print("Plants for the exhibition:")
for p in sorted_plants:
    print(f"- {p[0]}; Rarity: {p[1]['rarity']}; Rating: {p[1]['ratings']:.2f}")
