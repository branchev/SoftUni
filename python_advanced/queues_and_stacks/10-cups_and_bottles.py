from collections import deque

cups = deque([int(x) for x in input().split(' ')])
bottles = [int(b) for b in input().split()]

wasted_water = 0

while True:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    elif current_bottle < current_cup:
        current_cup -= current_bottle
        while current_cup and bottles:
            current_bottle = bottles.pop()
            if current_bottle > current_cup:
                wasted_water += current_bottle - current_cup
                current_cup = None
            else:
                current_cup -= current_bottle
    if not cups or not bottles:
        break

if cups:
    print(f"Cups: {' '.join([str(c) for c in cups])}")
elif bottles:
    print(f"Bottles: {' '.join([str(b) for b in bottles])}")
print(f"Wasted litters of water: {wasted_water}")