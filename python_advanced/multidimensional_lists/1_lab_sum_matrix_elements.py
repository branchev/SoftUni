def matrix_building(rows):
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix


def get_sum_of_matrix(matrix):
    the_sum = 0
    for row in matrix:
        the_sum += sum(row)
    return the_sum


rows, cols = [int(x) for x in input().split(', ')]

matrix = matrix_building(rows)
print(get_sum_of_matrix(matrix))
print(matrix)