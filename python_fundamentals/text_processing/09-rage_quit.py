line = input()
line += " "

total = ""
current = ""
num = ""
index = 0

while index < len(line):
    if not line[index].isdigit():
        current += line[index]
    else:
        num += line[index]
        if not line[index+1].isdigit():
            total += current * int(num)
            current = ""
            num = ""
    index += 1

total = total.upper()
unique = len(set(total))
print(f"Unique symbols used: {unique}")
print(total)
