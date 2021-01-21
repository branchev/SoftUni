equation = list(input())

indices_stack = []
for i in range(len(equation)):
    if equation[i] == "(":
        indices_stack.append(i)
    elif equation[i] == ")":
        start_i = indices_stack.pop()
        print(''.join(equation[start_i:i+1]))