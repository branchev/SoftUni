from collections import deque

prepared_food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if prepared_food >= current_order:
        prepared_food -= current_order
    else:
        orders.appendleft(current_order)
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(o) for o in orders])}")