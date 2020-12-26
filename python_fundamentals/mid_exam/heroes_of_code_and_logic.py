n = int(input())
heroes = []
for line in range(n):
    current_hero = input().split()
    for index in range(len(current_hero)):
        if index == 0:
            continue
        current_hero[index] = int(current_hero[index])
    heroes.append(current_hero)


def hero_popper(heroes, current_hero):
    for index in range(len(heroes)):
        if current_hero in heroes[index]:
            current_hero = heroes.pop(index)
            return heroes, current_hero


killed = []

# {hero name} {HP} {MP}
while True:
    line = input()
    if line == "End":
        break
    tokens = line.split(" - ")
    command = tokens[0]
    heroes, current_hero = hero_popper(heroes, tokens[1])
    if command == "CastSpell":
        MP_needed = int(tokens[2])
        spell_name = tokens[3]
        if current_hero[2] - MP_needed >= 0:
            current_hero[2] -= MP_needed
            print(f"{current_hero[0]} has successfully cast {spell_name} and now has {current_hero[2]} MP!")
        else:
            print(f"{current_hero[0]} does not have enough MP to cast {spell_name}!")
    # TakeDamage – {hero name} – {damage} – {attacker}
    elif command == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        if current_hero[1] - damage > 0:
            current_hero[1] -= damage
            print(f"{current_hero[0]} was hit for {damage} HP by {attacker} and now has {current_hero[1]} HP left!")
        else:
            killed.append(current_hero[0])
            print(f"{current_hero[0]} has been killed by {attacker}!")
    # Recharge – {hero name} – {amount}
    elif command == "Recharge":
        amount = int(tokens[2])
        if current_hero[2] + amount <= 200:
            current_hero[2] += amount
            print(f"{current_hero[0]} recharged for {amount} MP!")
        else:
            print(f"{current_hero[0]} recharged for {200 - current_hero[2]} MP!")
            current_hero[2] = 200
    # Heal – {hero name} – {amount}
    elif command == "Heal":
        amount = int(tokens[2])
        if current_hero[1] + amount <= 100:
            current_hero[1] += amount
            print(f"{current_hero[0]} healed for {amount} HP!")
        else:
            print(f"{current_hero[0]} healed for {100 - current_hero[1]} HP!")
            current_hero[1] = 100

    if current_hero[0] not in killed:
        heroes.append(current_hero)


def sort_by_health(element):
    return element[1]

heroes.sort(key=sort_by_health, reverse=True)

for hero in heroes:
    print(f"{hero[0]}\n  HP: {hero[1]}\n  MP: {hero[2]}")
