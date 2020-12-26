list_of_nms = list(map(int, input().split(", ")))

groups_count = (max(list_of_nms) // 10) + 1
if max(list_of_nms) % 10 == 0:
    groups_count -= 1

groups_of_tens = [[] for _ in range(groups_count)]

for number in list_of_nms:
    index = number // 10
    if number % 10 == 0:
        index -= 1
    groups_of_tens[index].append(number)

group_number = 10
for group in groups_of_tens:
    print(f"Group of {group_number}'s: {group}")
    group_number += 10
