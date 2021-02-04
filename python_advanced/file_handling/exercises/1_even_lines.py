import re


def symbol_replace(line):
    pattern = r"[-\.\?\!,]"
    return re.sub(pattern, "@", line)


def result_format(line):
    line = line.split(" ")
    return " ".join(line[::-1])


with open("text.txt", "r") as file:
    lines = file.readlines()
    for line_n in range(len(lines)):
        if line_n % 2 == 0:
            result_line = result_format(symbol_replace(lines[line_n][:-1]))
            print(result_line)
