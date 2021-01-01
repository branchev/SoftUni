clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
used_space_of_rack = 0

needed_racks_amount = 1

while clothes_stack:
    current_cloth = clothes_stack[-1]
    if used_space_of_rack + current_cloth <= rack_capacity:
        clothes_stack.pop()
        used_space_of_rack += current_cloth
    else:
        used_space_of_rack = 0
        needed_racks_amount += 1

print(needed_racks_amount)