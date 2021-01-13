filters = {"Positive": lambda x: x >= 0,
           "Negative": lambda x:  x < 0,
           "Even": lambda x:  x % 2 == 0,
           "Odd": lambda x: x % 2 != 0,
           }

line = list(map(int, input().split(', ')))

for f in filters:
    filtered = list(filter(filters[f], line))
    print(f"{f}: {', '. join([str(x) for x in filtered])}")