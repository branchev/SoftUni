rows, cols = [int(x) for x in input().split(' ')]

matrix = [' '.join([''.join([chr(97+i) if k != 1 else chr(97+i+j) for k in range(3)]) for j in range(cols)]) for i in range(rows)]

print('\n'.join(matrix))