# 1. Build the matrix wit all 0 cells:
def build_the_field(n):
    return [[0 for j in range(n)]for i in range(n)]


# 2. Place the bombs:
def place_the_bombs(n_of_bombs, field):
    for _ in range(n_of_bombs):
        line = [int(x) for x in input()[1:-1].split(', ')]
        row, col = line
        field[row][col] = "*"
    return field


# Helping func - current cell neighbour validator:
def is_valid(r, c, limit):
    if r >= limit or r < 0:
        return False
    if c >= limit or c < 0:
        return False
    return True


# 4. Calculate the cell:
def calculate_the_cell(matrix, row, col):
    MAPPER = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    neighbour_bombs = 0
    for step_forwarder in MAPPER:
        neighbour_r = row + step_forwarder[0]
        neighbour_c = col + step_forwarder[1]
        if is_valid(neighbour_r, neighbour_c, len(matrix)):
            if matrix[neighbour_r][neighbour_c] == "*":
                neighbour_bombs += 1
    return neighbour_bombs


# 3. Roaming the cells without bombs:
def roaming_the_cells(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "*":
                continue
            matrix[row][col] = calculate_the_cell(matrix, row, col)
    return matrix


# 4. Print the output:
def output_print(matrix):
    for i in matrix:
        print(' '.join([str(x) for x in i]))


def run_the_game():
    matrix = build_the_field(int(input()))
    matrix = place_the_bombs(int(input()), matrix)
    matrix = roaming_the_cells(matrix)
    output_print(matrix)


run_the_game()