def to_print(matrix):
    for i in matrix:
        print(''.join(i))


def is_dead_checker(matrix):
    for i in matrix:
        if "P" in i:
            return False
    return True


def step_validator(matrix, position, movement):
    row_index, col_index = position
    next_row = row_index + movement[0]
    next_col = col_index + movement[1]
    limit_rows = len(matrix)
    limit_cols = len(matrix[0])
    if next_row > limit_rows or next_row < 0:
        return False
    if next_col > limit_cols or next_col < 0:
        return False
    return True


def bunny_breeding(matrix):
    command_ways = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "B":
                for command in command_ways:
                    matrix[i+command[0]][j+command[1]] = "B"


def player_movement(matrix, start, movement):
    start_row, start_col = start
    matrix[start_row][start_col] = "."
    next_row = start_row + movement[0]
    next_col = start_col + movement[1]
    matrix[next_row][next_col] = "P"
    return matrix


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for i in range(rows)]

start = None
for i in range(rows):
    if "P" in matrix[i]:
        start = (i, matrix[i].index("P"))

commands_for_move_of_player = [x for x in input()]
directions_for_player = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for command_for_p in commands_for_move_of_player:
    movement = directions_for_player[command_for_p]
    if not step_validator(matrix, start, movement):
        print(to_print(matrix))
        print(f"won: {start[0]} {start[1]}")
        break
    matrix = player_movement(matrix, start, movement)
    is_dead = is_dead_checker(matrix)
    if is_dead:
        print(to_print(matrix))
        print(f"dead: {start[0]} {start[1]}")
        break
    current_row, current_col = start
    next_row = current_row + movement[0]
    next_col = current_col + movement[1]
    start = (next_row, next_col)
