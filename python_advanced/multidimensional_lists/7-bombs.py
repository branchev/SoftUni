def get_alive_cells_and_their_sum(matrix):
    number_of_alive_cells = 0
    sum_of_alive_cells = 0
    for i in matrix:
        for j in i:
            if j > 0:
                a = 5
                number_of_alive_cells += 1
                sum_of_alive_cells += j
    return f"Alive cells: {number_of_alive_cells}\nSum: {sum_of_alive_cells}"


def bombing(matrix, row, col):
    LIMIT = len(matrix[0]) -1
    targets = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    bomb = matrix[row][col]
    if bomb > 0:
        for target in targets:
            target_row, target_col = target
            target_row += row
            target_col += col
            if target_row > LIMIT or target_row < 0 or target_col > LIMIT or target_col < 0 or matrix[target_row][target_col] <= 0:
                continue
            matrix[target_row][target_col] -= bomb
        matrix[row][col] = 0
    return matrix


n = int(input())

matrix = [[int(x) for x in input().split(' ')] for i in range(n)]

coordinates = [[int(y) for y in x.split(',')] for x in input().split()]

for row, col in coordinates:
    matrix = bombing(matrix, row, col)

print(get_alive_cells_and_their_sum(matrix))

for i in matrix:
    print(' '.join([str(x) for x in i]))
