def matrix_swapper(matrix, row_1, col_1, row_2, col_2):
    element = matrix[row_1][col_1]
    matrix[row_1][col_1] = matrix[row_2][col_2]
    matrix[row_2][col_2] = element
    return matrix


def command_validator(matrix, command, row_1, col_1, row_2, col_2):
    if command != "swap":
        return False
    length_of_rows = len(matrix) - 1
    length_of_cols = len(matrix[0]) - 1
    if row_1 > length_of_rows or row_2 > length_of_rows:
        return False
    if col_1 > length_of_cols or col_2 > length_of_cols:
        return False
    return True


rows, cols = [int(x) for x in input().split(' ')]

matrix = [input().split(' ') for i in range(rows)]

while True:
    tokens = input().split(' ', maxsplit=1)
    command = tokens[0]
    if command == 'END':
        break
    positions = [int(x) for x in tokens[1].split()]
    if len(positions) == 4:
        row_1, col_1, row_2, col_2 = positions[0], positions[1], positions[2], positions[3]
    else:
        print("Invalid input!")
        continue
    if command_validator(matrix, command, row_1, col_1, row_2, col_2):
        matrix = matrix_swapper(matrix, row_1, col_1, row_2, col_2)
        for i in matrix:
            print(' '.join([str(x) for x in i]))
    else:
        print("Invalid input!")
