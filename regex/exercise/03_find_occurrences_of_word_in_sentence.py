import re

data = input()
searched = input()

pattern = fr"\b{searched}\b"

print(len([oc for oc in re.finditer(pattern, data, re.IGNORECASE)]))
