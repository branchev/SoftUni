n = int(input())

elements = set()

for _ in range(n):
    line = input().split()
    for element in line:
        elements.add(element)

for el in elements:
    print(el)