import re


# def emo_coolness(emos, total):
#     for emo in emos:
#         emo = emo.group()
#         stoper = len(emo) - 2
#         calculation = 0
#         for i in range(2, stoper):
#             calculation += ord(emo[i])
#         if calculation > total:
#             print(emo)


data = input()
pattern = r"(:{2}|\*{2})[A-Z][a-z]{2,}\1"

icons = re.finditer(pattern, data)

regex = r"\d"
digits = re.findall(regex, data)

total = 1
for d in digits:
    total *= int(d)

number_of_emos = 0
valid_icons = []
for e in icons:
    number_of_emos += 1
    validator = e.group()
    emo_result = 0
    for c in validator:
        emo_result += ord(c)
    if emo_result > total:
        valid_icons.append(validator)
    emo_result = 0
print(f"Cool threshold: {total}")
print(f"{number_of_emos} emojis found in the text. The cool ones are:")
if valid_icons:
    for ic in valid_icons:
        print(ic)
