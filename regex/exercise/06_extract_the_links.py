import re

pattern = r"(^|(?<=\s))w{3}\.[-\w]+(\.[a-z]+)+"

while True:
    line = input()
    if line == "":
        break
    match = re.finditer(pattern, line)
    if match:
        for m in match:
            print(m.group())
