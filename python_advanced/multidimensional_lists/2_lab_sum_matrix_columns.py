def matrix_building(rows):
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split(' ')])
    return matrix


def get_columns_sum(matrix):
    columns_sums = []
    for j in range(len(matrix[0])):
        column_values = []
        for i in range(len(matrix)):
            column_values.append(matrix[i][j])
            if i == len(matrix) -1:
                columns_sums.append(sum(column_values))
                column_values = []
    return columns_sums


rows, cols = [int(x) for x in input().split(', ')]

matrix = matrix_building(rows)
column_sums = get_columns_sum(matrix)

for x in column_sums:
    print(x)