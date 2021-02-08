def read_the_chess_board():
    board = [input().split(' ') for _ in range(8)]
    return board


def read_the_king_position(board):
    for i in range(8):
        if "K" in board[i]:
            return i, board[i].index("K")


def hor_check(row_k, row, index):
    queens = []
    for i in range(index, 8):
        if row[i] == "Q":
            queens.append([row_k, i])
            break
    for i in range(index, -1, -1):
        if row[i] == "Q":
            queens.append([row_k, i])
            break
    return queens


def ver_check(row_k, board, col):
    queens = []
    for i in range(row_k, 8):
        if board[i][col] == "Q":
            queens.append([i, col])
            break
    for i in range(row_k, -1, -1):
        if board[i][col] == "Q":
            queens.append([i, col])
            break
    return queens


def pr_diagonal_check(row_k, board, col_k):
    queens = []
    row = row_k
    col = col_k

    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            queens.append([row, col])
            break
        row -= 1
        col -= 1

    row = row_k
    col = col_k
    while row < 8 and col < 8:
        if board[row][col] == "Q":
            queens.append([row, col])
            break
        row += 1
        col += 1
    return queens


def sec_diagonal_check(row_k, board, col_k):
    queens = []
    row = row_k
    col = col_k

    while row >= 0 and col < 8:
        if board[row][col] == "Q":
            queens.append([row, col])
            break
        row -= 1
        col += 1

    row = row_k
    col = col_k
    while row < 8 and col >= 0:
        if board[row][col] == "Q":
            queens.append([row, col])
            break
        row += 1
        col -= 1

    return queens


def run_the_game():
    available_queens = []
    chess_board = read_the_chess_board()
    k_row, k_col = read_the_king_position(chess_board)
    queens_hor = hor_check(k_row, chess_board[k_row], k_col)
    if queens_hor:
        available_queens += queens_hor
    queens_ver = ver_check(k_row, chess_board, k_col)
    if queens_ver:
        available_queens += queens_ver
    queens_pr_diagonal = pr_diagonal_check(k_row, chess_board, k_col)
    if queens_pr_diagonal:
        available_queens += queens_pr_diagonal
    queens_sec_diagonal = sec_diagonal_check(k_row, chess_board, k_col)
    if queens_sec_diagonal:
        available_queens += queens_sec_diagonal
    return available_queens


def printing_positions_of_available_queens(queens):
    for q in queens:
        print(q)


available_queens = run_the_game()
if available_queens:
    printing_positions_of_available_queens(available_queens)
else:
    print("The king is safe!")