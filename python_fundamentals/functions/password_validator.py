def is_perfect(number):
    devidors = []
    half = number // 2
    for n in range(1, half+1):
        if number // n == 0:
            devidors.append(n)
    if sum(devidors) == number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())

print(is_perfect(number))
