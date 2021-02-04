import re


def counter(line, pattern):
    return len(re.findall(pattern, line))


def line_printing(line, n):
    n += 1
    if line[-1] == "\n":
        line = line[:-1]

    letters_pattern = r"[a-zA-Z]"
    punct_pattern = r"['-\.\?\!,]"
    return f"Line {n}: {line} ({counter(line, letters_pattern)})({counter(line, punct_pattern)})"


with open("text.txt", "r") as file:
    lines = file.readlines()
    for line_n in range(len(lines)):
        print(line_printing(lines[line_n], line_n))