from collections import defaultdict
materials = {
    "fragments": 0,
    "shards": 0,
    "motes": 0
}

junks = defaultdict(int)

material_obtained = False

while not material_obtained:

    line = input().split()
    for index in range(0, len(line), 2):
        material = line[index + 1].lower()
        quantity = int(line[index])
        if material in materials:
            materials[material] += quantity
        if material not in materials:
            junks[material] += quantity
        if materials["fragments"] >= 250 or materials["shards"] >= 250 or materials["motes"] >= 250:
            if materials["fragments"] >= 250:
                print(f"Valanyr obtained!")
                materials["fragments"] -= 250
            elif materials["shards"] >= 250:
                print(f"Shadowmourne obtained!")
                materials["shards"] -= 250
            else:
                print(f"Dragonwrath obtained!")
                materials["motes"] -= 250
            material_obtained = True
            break




materials = dict(sorted(materials.items(), key = lambda t: (-t[1], t[0])))
for key, value in materials.items():
    print(f"{key}: {value}")

junks = dict(sorted(junks.items(), key= lambda t: t[0]))
for key, value in junks.items():
    print(f"{key}: {value}")
