def matrix_building(rows):
    matrix = []
    for i in range(rows):
        matrix.append(list(input()))
    return matrix


def searching_symbol(matrix, symbol):
    for i in range(len(matrix)):
        if symbol in matrix[i]:
            return i, matrix[i].index(symbol)


def printing_the_coordinates(coordinates, symbol):
    if coordinates:
        print(coordinates)
    else:
        print(f"{symbol} does not occur in the matrix")


n = int(input())
matrix = matrix_building(n)

searched_symbol = input()
symbol_coordinates = searching_symbol(matrix, searched_symbol)
printing_the_coordinates(symbol_coordinates, searched_symbol)