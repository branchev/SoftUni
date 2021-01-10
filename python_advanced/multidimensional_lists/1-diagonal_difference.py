n = int(input())

matrix = [[int(x) for x in input().split(' ')] for i in range(n)]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

secondary_diagonal_index = len(matrix[0]) - 1
for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][secondary_diagonal_index]
    secondary_diagonal_index -= 1

print(abs(primary_diagonal_sum - secondary_diagonal_sum))

