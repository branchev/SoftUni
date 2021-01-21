from collections import deque

people = deque(input().split())
rotates = int(input())

while len(people) > 1:
    for _ in range(rotates-1):
        people.rotate(-1)
    print(f"Removed {people.popleft()}")

print(f"Last is {people.popleft()}")
