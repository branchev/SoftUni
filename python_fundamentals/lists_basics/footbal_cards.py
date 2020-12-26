team_a = ["X" for n in range(1, 11+1)]
team_b = ["X" for n in range(1, 11+1)]

cards = input().split()

a_removed = 0
b_removed = 0
terminated = False

for element in cards:
    if element == "":
        break
    decision = element.split("-")
    team = decision[0]
    player = int(decision[1]) - 1
    if team == "A":
        if team_a[player] == "_":
            continue
        else:
            team_a[player] = "_"
            a_removed += 1
            if a_removed > 4:
                terminated = True
                break
    else:
        if team == "B":
            if team_b[player] == "_":
                continue
            else:
                team_b[player] = "_"
                b_removed += 1
                if b_removed > 4:
                    terminated = True
                    break

team_a = len(team_a) - a_removed
team_b = len(team_b) - b_removed

print(f"Team A - {team_a}; Team B - {team_b}")
if terminated:
    print("Game was terminated")

