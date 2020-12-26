import re

data = input()

pattern = r"(^|(?<=[\b\s]))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z]+((\.[a-z]+)+)(?=\.)?"
matches = re.finditer(pattern,data, re.IGNORECASE)

for match in matches:
    print(match).group(0)
