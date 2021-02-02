def build_a_territory(n):
    return [list(input()) for i in range(n)]


def take_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                return i, j


def next_step_validator(row, col, matrix, command_map, command):
    row += command_map[command][0]
    col += command_map[command][1]
    if row < 0 or row >= len(matrix[0]):
        return False
    if col < 0 or col >= len(matrix):
        return False
    return True


def play(matrix, row, col):
    matrix[row][col] = "."
    return matrix


def next_base_check(matrix, row, col):
    return matrix[row][col]


def barrow_skipping(matrix, row, col):
    matrix[row][col] = "."
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "B":
                matrix[i][j] = "S"
                return i, j


def matrix_printing(matrix):
    for i in matrix:
        print(''.join(i))


command_map = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

n = int(input())
matrix = build_a_territory(n)
row, col = take_position(matrix)

won = False
eaten = 0
while True:
    command = input()
    matrix = play(matrix, row, col)
    is_valid = next_step_validator(row, col, matrix, command_map, command)
    if is_valid:
        row += command_map[command][0]
        col += command_map[command][1]
        next_base = next_base_check(matrix, row, col)
        if next_base == "B":
            row, col = barrow_skipping(matrix, row, col)
            matrix[row][col] = "S"
        elif next_base == "*":
            eaten += 1
            if eaten == 10:
                matrix[row][col] = "S"
                won = True
                break
        elif next_base == "-":
            matrix[row][col] = "S"
    else:
        break

if won:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {eaten}")
matrix_printing(matrix)