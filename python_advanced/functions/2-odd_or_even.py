def filter_of_nums(command, x):
    if command == "Odd":
        return x % 2 != 0
    if command == "Even":
        return x % 2 == 0


searched = input()
initial_line = [int(x) for x in input().split(' ')]
searched_sum = sum([x for x in initial_line if filter_of_nums(searched, int(x))]) * len(initial_line)
print(searched_sum)