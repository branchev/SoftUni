def matrix_building(rows):
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix


def get_submatrix_sum(best_submatrix):
    the_sum = 0
    for i in best_submatrix:
        the_sum += sum(i)
    return the_sum


def get_best_square(matrix):
    best_submatrix = []
    best_submatrix_sum = None
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if not best_submatrix:
                best_submatrix.append(matrix[i][j: j+2])
                best_submatrix.append(matrix[i+1][j: j+2])
                best_submatrix_sum = get_submatrix_sum(best_submatrix)
                continue
            if get_submatrix_sum([matrix[i][j: j+2], matrix[i+1][j: j+2]]) > best_submatrix_sum:
                best_submatrix_sum = get_submatrix_sum([matrix[i][j: j+2], matrix[i+1][j: j+2]])
                best_submatrix = [[matrix[i][j: j+2], matrix[i+1][j: j+2]]]
    return best_submatrix, best_submatrix_sum


def printing(submatrix, sub_sum):
    for i in submatrix:
        for j in i:
            print(' '.join([str(x) for x in j]))
    print(sub_sum)


rows, cols = [int(x) for x in input().split(', ')]

matrix = matrix_building(rows)
sub_matrix, sub_sum = (get_best_square(matrix))
printing(sub_matrix, sub_sum)

