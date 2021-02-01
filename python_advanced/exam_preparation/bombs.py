from collections import deque
from collections import defaultdict


def try_to_create_a_bomb(effect, casing):
    bombs_mapper = {
        "datura_bomb": 40,
        "cherry_bomb": 60,
        "smoke_decoy_bomb": 120
        }
    for bomb, power in bombs_mapper.items():
        if effect + casing == power:
            return bomb


def pouch_checker(bombs_created):
    if len(bombs_created) < 3:
        return True
    for _, amount in bombs_created.items():
        if amount < 3:
            return True
    return False


def bombs_pouch_printing(created_bombs):
    if len(created_bombs) < 3:
        print("You don't have enough materials to fill the bomb pouch.")
        return
    else:
        for _, amount in created_bombs.items():
            if amount < 3:
                print("You don't have enough materials to fill the bomb pouch.")
                return
    print("Bene! You have successfully filled the bomb pouch!")


def bomb_effects_printing(bomb_effects):
    if not bomb_effects:
        print("Bomb Effects: empty")
    else:
        print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")


def bomb_cassings_printing(bombs_casing):
    if not bombs_casing:
        print("Bomb Casings: empty")
    else:
        print(f"Bomb Casings: {', '.join([str(x) for x in bombs_casing])}")


def pouch_printing(bombs_created):
    mapper = {"cherry_bomb": "Cherry Bombs",
              "datura_bomb": "Datura Bombs",
              "smoke_decoy_bomb": "Smoke Decoy Bombs",
              }
    for bomb, description in mapper.items():
        if bomb in bombs_created:
            print(f"{description}: {bombs_created[bomb]}")
        else:
            print(f"{description}: 0")


bombs_created = defaultdict(int)

bomb_effects = deque([int(n) for n in input().split(", ")])
bombs_casing = [int(n) for n in input().split(", ")]

while bomb_effects or bombs_casing:
    if not pouch_checker(bombs_created):
        break
    current_effect = bomb_effects.popleft()
    current_bomb_case = bombs_casing.pop()
    if try_to_create_a_bomb(current_effect, current_bomb_case):
        bombs_created[try_to_create_a_bomb(current_effect, current_bomb_case)] += 1
    else:
        bomb_effects.appendleft(current_effect)
        current_bomb_case -= 5
        bombs_casing.append(current_bomb_case)

bombs_pouch_printing(bombs_created)
bomb_effects_printing(bomb_effects)
bomb_cassings_printing(bombs_casing)
pouch_printing(bombs_created)