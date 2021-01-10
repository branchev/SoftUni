import itertools
import sys


rows, columns = [int(x) for x in input().split(' ')]

SUBCOLUMNS = 3
SUBROWS = 3
LIMIT_RANGE_FOR_COLUMNS = columns - 2
LIMIT_RANGE_FOR_ROWS = rows-2

matrix = [[int(x) for x in input().split(' ')] for i in range(rows)]
max_submatrix_sum = -sys.maxsize
max_submatrix_content = []

current_sub_matrix = []
for row in range(LIMIT_RANGE_FOR_ROWS):
    for col in range(LIMIT_RANGE_FOR_COLUMNS):
        current_sub_matrix.append(matrix[row][col:col + SUBCOLUMNS])
        current_sub_matrix.append(matrix[row+1][col:col + SUBCOLUMNS])
        current_sub_matrix.append(matrix[row+2][col:col + SUBCOLUMNS])
        current_sub_matrix_sum = sum(itertools.chain(*current_sub_matrix))
        if current_sub_matrix_sum > max_submatrix_sum:
            max_submatrix_sum = current_sub_matrix_sum
            max_submatrix_content = current_sub_matrix
        current_sub_matrix = []


print(f"Sum = {max_submatrix_sum}")

for i in max_submatrix_content:
    print(f"{' '.join([str(x) for x in i])}")