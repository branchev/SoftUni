def attack_validator(current_row, current_col, matrix, n):
    positions_to_attack = [(-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1)]
    n = n - 1
    counter = 0
    for row_col in positions_to_attack:
        row, col = row_col
        attacked_row = current_row + row
        attacked_col = current_col + col
        if attacked_row > n or attacked_row < 0 or attacked_col > n or attacked_col < 0:
            continue
        if matrix[attacked_row][attacked_col] == "K":
           counter += 1
    return counter


n = int(input())

chess_desk = [[x for x in input()] for i in range(n)]

total_removed_knights = 0
while True:
    best_position_row_and_col = None
    best_possibilities_to_attack = 0
    for i in range(n):
        for j in range(n):
            if chess_desk[i][j] == 'K':
                current_knight_possibilities_to_attack = attack_validator(i, j, chess_desk, n)
                if current_knight_possibilities_to_attack > best_possibilities_to_attack:
                    best_possibilities_to_attack = current_knight_possibilities_to_attack
                    best_position_row_and_col = (i, j)
    if not best_possibilities_to_attack:
        break
    row, col = best_position_row_and_col
    chess_desk[row][col] = "0"
    total_removed_knights += 1
    best_position_row_and_col = None
    best_possibilities_to_attack = 0

print(total_removed_knights)




