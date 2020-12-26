import re

data = input()

pattern = r"(?P<name>\b[A-Z][a-z]+) (?P<surname>[A-Z][a-z]+\b)"
names = re.finditer(pattern, data)

for person in names:
    p = person.groupdict()
    print(f"{p['name']} {p['surname']}", end=" ")
