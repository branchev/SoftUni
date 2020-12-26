def plunder(target_dict, city, people, gold):
    population = target_dict[city]['people']
    wealthy = target_dict[city]['gold']
    if population - people <= 0:
        if wealthy - gold <= 0:
            del target_dict[city]
            print(f"{city} plundered! {wealthy} gold stolen, {population} citizens killed.")
            print(f"{city} has been wiped off the map!")
            return target_dict
        del target_dict[city]
        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        print(f"{city} has been wiped off the map!")
        return target_dict
    if wealthy - gold <= 0:
        del target_dict[city]
        print(f"{city} plundered! {wealthy} gold stolen, {people} citizens killed.")
        print(f"{city} has been wiped off the map!")
        return target_dict
    target_dict[city]['people'] -= people
    target_dict[city]['gold'] -= gold
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    return target_dict


target_towns = {}

while True:
    line = input()
    if line == "Sail":
        break
    city, people, gold = line.split("||")
    people = int(people)
    gold = int(gold)
    if city not in target_towns:
        target_towns[city] = {}
        target_towns[city]['people'] = 0
        target_towns[city]['gold'] = 0
    target_towns[city]['people'] += people
    target_towns[city]['gold'] += gold

while True:
    data = input()
    if data == "End":
        break
    tokens = data.split("=>")
    command = tokens[0]
    if command == "Plunder":
        city, people, gold = tokens[1:]
        people = int(people)
        gold = int(gold)
        target_towns = plunder(target_towns, city, people, gold)

    elif command == "Prosper":
        city, gold = data.split("=>")[1:]
        gold = int(gold)
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        target_towns[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {target_towns[city]['gold']} gold.")

if target_towns:
    print(f"Ahoy, Captain! There are {len(target_towns)} wealthy settlements to go to:")
    sorted_targets = sorted(target_towns.items(), key=lambda x: (-x[1]['gold'], x[0]))
    # print(sorted_targets)
    for town in sorted_targets:
        print(f"{town[0]} -> Population: {town[1]['people']} citizens, Gold: {town[1]['gold']} kg")
