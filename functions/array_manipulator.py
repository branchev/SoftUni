def exchange(data, n):
    n += 1
    first = data[n:]
    sec = data[:n]
    exchanged = first + sec
    return exchanged


def max(data, statement):
    import sys
    winner = - sys.maxsize - 1
    index_winner = None
    new_data = list(enumerate([int(n) for n in data]))
    if statement == "even":
        for index, number in new_data:
            if number % 2 != 0:
                continue
            if number > winner:
                winner = number
                index_winner = index
    elif statement == "odd":
        for index, number in new_data:
            if number % 2 == 0:
                continue
            if number > winner:
                winner = number
                index_winner = index
    if index_winner == None:
        return f"No matches"
    return index_winner


def min(data,statement):
    import sys
    winner = sys.maxsize
    index_winner = None
    new_data = list(enumerate([int(n) for n in data]))
    if statement == "even":
        for index, number in new_data:
            if number % 2 != 0:
                continue
            if number < winner:
                winner = number
                index_winner = index
    elif statement == "odd":
        for index, number in new_data:
            if number % 2 == 0:
                continue
            if number < winner:
                winner = number
                index_winner = index
    if index_winner == None:
        return f"No matches"
    return index_winner


def first(data, number, statement):
    data = list(map(int, data))
    searched = []
    if statement == "even":
        for num in data:
            if number == 0:
                break
            if num % 2 != 0:
                continue
            searched.append(num)
            number -= 1
    elif statement == "odd":
        for num in data:
            if number == 0:
                break
            if num % 2 == 0:
                continue
            searched.append(num)
            number -= 1
    if searched == []:
        return []
    searched = list(map(str, searched))
    return " ".join(searched)


def last(data, number, statement):
    data = list(map(int, data))
    searched = []
    if statement == "even":
        for index in range((len(data)-1), -1, -1):
            if number == 0:
                break
            n = data[index]
            if n % 2 != 0:
                continue
            searched.append(n)
            number -= 1
    elif statement == "odd":
        for index in range((len(data)-1), -1, -1):
            if number == 0:
                break
            n = data[index]
            if n % 2 == 0:
                continue
            searched.append(n)
            number -= 1
    searched = reversed(list(map(str, searched)))
    return " ".join(searched)



data = input().split()

while True:
    command = input()
    if command == "end":
        break
    tokens = command.split()
    command = tokens[0]
    statement = tokens[1]
    if command == "exchange":
        if int(statement) < len(data):
            data = exchange(data, int(statement))
        else:
            print("Invalid index")
    elif command == "max":
        winner = max(data, statement)
        print(winner)
    elif command == "min":
        winner = min(data, statement)
        print(winner)
    elif command == "first":
        number = int(statement)
        type_of_search = tokens[2]
        if len(data) >= number:
            searched = first(data, number, type_of_search)
            print(searched)
        else:
            print("Invalid count")
    elif command == "last":
        number = int(statement)
        type_of_search = tokens[2]
        if len(data) >= number:
            searched = last(data, number, type_of_search)
            print(searched)
        else:
            print("Invalid count")
