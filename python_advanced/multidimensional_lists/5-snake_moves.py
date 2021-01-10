from collections import deque

rows, cols = [int(x) for x in input().split(' ')]

matrix = [["" for j in range(cols)] for i in range(rows)]

line = deque(input())

for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            current_char = line.popleft()
            matrix[i][j] = current_char
            line.append(current_char)
    else:
        for j in range(cols-1, -1, -1):
            current_char = line.popleft()
            matrix[i][j] = current_char
            line.append(current_char)

for i in matrix:
    print(''.join(i))
