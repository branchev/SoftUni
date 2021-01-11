def is_valid_move(field, start_row, start_col, commands_path):
    LIMIT = len(field[0]) -1
    next_row, next_col = commands_path
    if start_row + next_row > LIMIT or start_row + next_row < 0:
        return False
    if start_col + next_col > LIMIT or start_col + next_col < 0:
        return False
    return True


def start_the_game(matrix, commands, start):
    commands_path = {'up': (-1, 0), 'right': (0, 1), 'left': (0, -1), 'down': (1, 0)}
    coals = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "c":
                coals += 1

    start_row, start_col = start
    for command in commands:
        valid_move = is_valid_move(matrix, start_row, start_col, commands_path[command])
        if valid_move:
            start_row += commands_path[command][0]
            start_col += commands_path[command][1]
        next_step = matrix[start_row][start_col]
        if next_step == "e":
            return f"Game over! ({start_row}, {start_col})"
        elif next_step == "*":
            continue
        elif next_step == "c":
            coals -= 1
            matrix[start_row][start_col] = "*"
            if coals == 0:
                return f"You collected all coals! ({start_row}, {start_col})"

    return f"{coals} coals left. ({start_row}, {start_col})"


n = int(input())

commands = input().split()

matrix = [input().split() for i in range(n)]

start = None
for i in range(n):
    if "s" in matrix[i]:
        start = (i, matrix[i].index("s"))

print(start_the_game(matrix, commands, start))
