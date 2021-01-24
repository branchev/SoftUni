def matrix_building(rows):
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split(' ')])
    return matrix


def get_pr_diagonal_sum(matrix):
    the_sum = 0
    for i in range(len(matrix)):
        the_sum += matrix[i][i]
    return the_sum


n = int(input())

matrix = matrix_building(n)
print(get_pr_diagonal_sum(matrix))