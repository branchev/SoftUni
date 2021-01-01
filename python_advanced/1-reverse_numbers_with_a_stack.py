line = input().split()

result = []
while line:
    item = line.pop()
    result.append(item)

print(' '.join(result))