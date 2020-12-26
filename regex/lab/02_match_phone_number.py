import re

data = input()

pattern = r"(^|(?<=\s))\+359([ \-])2\2\d{3}\2\d{4}($|(?=[\s,]))"
matches = re.finditer(pattern, data)

result = []
for match in matches:
    number = match.group()
    result.append(number)

print(", ".join(result))
