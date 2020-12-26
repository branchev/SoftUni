line = input()
result = line[0:line.find(">")+1]
line = line[line.find(">")+1:]
bombs = 0
for ch in line:
    if ch.isdigit() and result[-1] == ">":
        bombs += int(ch) - 1
        continue
    if ch == ">":
        result += ch
        continue
    if bombs:
        bombs -= 1
        continue
    result += ch

print(result)
