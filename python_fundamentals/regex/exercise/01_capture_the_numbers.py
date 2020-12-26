import re

data = input()

pattern = r"\d+"
result = []

while data:
    number = re.findall(pattern, data)
    result.extend(number)
    data = input()

print(*result)
