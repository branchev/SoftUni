import re


def contact_validator(data):
    pattern = r"^\d+(?:\s+|$)"
    result = re.findall(pattern, data)
    return result


contacts = {}
iter_count = 0
while True:
    line = input()
    if line[0].isdigit():
        number = contact_validator(line)
        iter_count = int(number[0])
        break
    name, phone_number = line.split("-", 1)
    contacts[name] = phone_number

for _ in range(iter_count):
    contact_name = input()
    if contact_name not in contacts:
        print(f"Contact {contact_name} does not exist.")
    else:
        print(f"{contact_name} -> {contacts[contact_name]}")