import re

data = input()

pattern = r"(^|(?<!\w))_{1}(?P<expr>[A-Za-z0=9]+)(?!\w)"
matches = re.finditer(pattern, data)

result = []
for match in matches:
    result_dict = match.groupdict()
    result.append(result_dict['expr'])

print(*result, sep=',')
