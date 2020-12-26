energie = 100
coins = 100

working_day_events = input().split("|")

bankrupt = False

for e_or_i in working_day_events:
    tokens = e_or_i.split("-")
    event_or_item = tokens[0]
    value = int(tokens[1])
    if event_or_item == "rest":
        if energie == 100:
            print("You gained 0 energy.")
            print("Current energy: 100.")
        elif energie + value >= 100:
            print(f"You gained {-(value-100)} energy.")
            energie = 100
            print("Current energy: 100.")
        else:
            energie += value
            print(f"You gained {value} energy.")
            print(f"Current energy: {energie}.")
    elif event_or_item == "order":
        if energie - 30 <= 0:
            energie += 50
            if energie > 100:
                energie = 100
            print("You had to rest!")
            continue
        else:
            energie -= 30
            coins += value
            print(f"You earned {value} coins.")
    else:
        if coins - value > 0:
            coins -= value
            print(f"You bought {event_or_item}.")
        elif coins - value <= 0:
            print(f"Closed! Cannot afford {event_or_item}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energie}")