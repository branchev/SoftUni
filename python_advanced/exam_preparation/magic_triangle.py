def clean_zeros(matrix):
    for x in matrix:
        while 0 in x:
            x.remove(0)
    return matrix


def get_magic_triangle(n):
    matrix = [[0 for j in range(n)]for i in range(n)]

    for x in range(len(matrix)):
        if x - 1 < 0:
            matrix[x][0] = 1
            continue
        for y in range(x+1):
            if y - 1 < 0:
                matrix[x][y] = 1
                continue
            matrix[x][y] = matrix[x-1][y] + matrix[x-1][y-1]
    matrix = clean_zeros(matrix)
    return matrix


