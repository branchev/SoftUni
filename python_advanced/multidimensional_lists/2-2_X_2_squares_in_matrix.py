def submatrix_validator(submatrix):
    symbol = ''
    for i in submatrix:
        for k in i:
            if symbol == '':
                symbol = k
            if k != symbol:
                return False
    return True


rows, cols = [int(x) for x in input().split(' ')]

matrix = [input().split(' ') for i in range(rows)]

SUB_COLUMNS = 2

SUB_RANGE_ROWS = rows - 1
SUB_RANGE_COLS = cols - 1

matches = 0
for row in range(SUB_RANGE_ROWS):
    sub_matrix = []
    for col in range(SUB_RANGE_COLS):
        sub_matrix.append(matrix[row][col:col+SUB_COLUMNS])
        sub_matrix.append(matrix[row+1][col:col + SUB_COLUMNS])
        is_matched = submatrix_validator(sub_matrix)
        if is_matched:
            matches += 1
        sub_matrix = []

print(matches)