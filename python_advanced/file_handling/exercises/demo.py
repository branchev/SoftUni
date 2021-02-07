from pyfiglet import figlet_format

with open("demo.txt", "a") as file:
    while True:
        line = input()
        if line == "END":
            break
        text = figlet_format(line, font="digital")
        file.writelines(text)

