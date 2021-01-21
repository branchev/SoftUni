from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

supermarket_queue = deque()
while True:
    name = input()
    if name == END_COMMAND:
        break
    elif name == PAID_COMMAND:
        while supermarket_queue:
            print(supermarket_queue.popleft())
    else:
        supermarket_queue.append(name)

print(f"{len(supermarket_queue)} people remaining.")