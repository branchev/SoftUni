n = int(input())

stack_of_nums = []
for _ in range(n):
    line = [int(x) for x in input().split()]
    command = line[0]
    if command == 1:
        element = line[1]
        stack_of_nums.append(element)
    elif command == 2:
        if stack_of_nums:
            stack_of_nums.pop()
    elif command == 3 and stack_of_nums:
        print(max(stack_of_nums))
    elif command == 4 and stack_of_nums:
        print(min(stack_of_nums))

print(', '.join(reversed([str(x)for x in stack_of_nums])))