def growing(n):
    for row in range(1, n + 1):
        current_row = ' ' * (n - row)
        current_row += '* ' * row
        print(current_row)


def shrinking(n):
    for row in range(n-1, 0, -1):
        current_row = ' ' * (n - row)
        current_row += '* ' * row
        print(current_row)


def rhombus(n):
    growing(n)
    shrinking(n)


rhombus(int(input()))