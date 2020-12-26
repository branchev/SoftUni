def manipulator(cod):
    total = 0
    letters = {chr(97+n): n+1 for n in range(26)}
    first_letter = cod[0]
    last_letter = cod[-1]
    num = int(cod[1:-1])
    if first_letter.isupper():
        total = num / letters[first_letter.lower()]
    else:
        total = num * letters[first_letter]

    if last_letter.isupper():
        total -= letters[last_letter.lower()]
    else:
        total += letters[last_letter]
    return total


line = input().split()

result = 0

for code in line:
    result += manipulator(code)

print(f"{result:.2f}")
