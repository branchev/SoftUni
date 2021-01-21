from collections import deque

pairs = {
    "{": "}",
    "(": ")",
    "[": "]",
}

line = list(input())
opening_parentheses = deque(line[0:(len(line)//2)])
closing_parentheses = deque(line[(len(line)//2):])

balanced = True
while opening_parentheses and closing_parentheses:
    if pairs[opening_parentheses.popleft()] == closing_parentheses.pop():
        continue
    balanced = False
    break

if balanced:
    print("YES")
else:
    print("NO")




