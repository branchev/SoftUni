m =[
    [1, 2, 3, 4],
    [3, 2, 4, 5],
]

r, c = len(m), len(m[0])
total = 0

for j in range(c):
    for i in range(r):
        current = m[i][j]
        total += current
    print(total)
    total = 0
