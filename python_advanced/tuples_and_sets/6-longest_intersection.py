n = int(input())

max_length = 0
max_range = set()

range_1 = set()
range_2 = set()

for r in range(n):
    tokens = input().split("-")
    iterations = 1
    for rng in tokens:
        current_range = rng.split(",")
        start = int(current_range[0])
        stop = int(current_range[1]) + 1
        if iterations == 1:
            for number in range(start, stop):
                range_1.add(number)
            iterations += 1
        else:
            for number in range(start, stop):
                range_2.add(number)
            iterations = 1
    current_intersection = range_1 & range_2
    if len(current_intersection) > max_length:
        max_length = len(current_intersection)
        max_range = current_intersection
    range_1 = set()
    range_2 = set()

print(f"Longest intersection is {list(max_range)} with length {max_length}")
