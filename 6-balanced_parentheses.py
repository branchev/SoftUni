line = [ord(x) for x in input()]

opening = line[0:(len(line)//2)]
closing = list(reversed(line[(len(line)//2):]))

balanced = True
if len(opening) == len(closing):
    for index in range(len(opening)):
        if opening[index] == 40 and closing[index] == 41:
            continue
        elif opening[index] == closing[index] -2:
            continue
        else:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")