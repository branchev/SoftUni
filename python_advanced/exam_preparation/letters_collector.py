# 1. Build the matrix
def build_the_matrix(n):
    return [list(input()) for i in range(n)]


# 2. Find the initial position of the player
def initial_pos_of_p(matx):
    for i in range(len(matx)):
        if "P" in matx[i]:
            return i, matx[i].index("P")


# 4. Validate of the next step
def step_validator(*args):
    limit, r, c = args
    limit -= 1
    if r > limit or r < 0:
        return False
    if c > limit or c < 0:
        return False
    return True


# 3. Move to position after receiving a command
def move(*args):
    commands_mapper = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    matx, command, r, c, collected_word = args
    new_row = r + commands_mapper[command][0]
    new_col = c + commands_mapper[command][1]
    if step_validator(len(matx), new_row, new_col):
        matx[r][c] = "-"
        r += commands_mapper[command][0]
        c += commands_mapper[command][1]
        if matx[r][c] != "-":
            collected_word += matx[r][c]
            matx[r][c] = "P"
    else:
        collected_word = collected_word[:-1]
    return matx, r, c, collected_word


# 5. Print the output
def print_the_output(m, word):
    print(word)
    for i in m:
        print(''.join(i))


def run_the_game():
    initial_string = input()
    matrix_square_size = int(input())

    # 1. Build the matrix
    matrix = build_the_matrix(matrix_square_size)

    # 2. Find the position of the player
    row, col = initial_pos_of_p(matrix)

    commands_amount = int(input())
    for _ in range(commands_amount):
        comand = input()
        matrix, row, col, initial_string = move(matrix, comand, row, col, initial_string)

    # 5. Print the output
    print_the_output(matrix, initial_string)


run_the_game()