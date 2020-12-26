import re

data = input()

pattern = r"(?P<dd>(^|(?<=\s))\d{2})(?P<sep>[\./-])(?P<mm>[A-Z][a-z]{2})(?P=sep)(?P<yy>\d{4})"
matches = re.finditer(pattern, data)

for match in matches:
    date = match.groupdict()
    print(f"Day: {date['dd']}, Month: {date['mm']}, Year: {date['yy']}")
