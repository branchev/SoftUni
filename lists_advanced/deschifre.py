line = input().split()
deschifred = []

for item in line:
    digits = ""
    letters = ""
    for ch in item:
        if ch.isdigit():
            digits += ch
        else:
            letters += ch
    digits = chr(int(digits))
    first = letters[-1]
    middle = letters[1:-1]
    last = letters[0]
    if len(letters) == 1:
        result = digits + letters
        deschifred.append(result)
        continue
    result = digits + first + middle + last
    deschifred.append(result)

print(" ".join(deschifred))
