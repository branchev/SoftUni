n = int(input())

parked_cars = {}

for _ in range(n):
    line = input().split()
    command = line[0]
    name = line[1]
    if command == "register":
        number = line[2]
        if name in parked_cars:
            print(f"ERROR: already registered with plate number {parked_cars[name]}")
            continue
        parked_cars[name] = number
        print(f"{name} registered {number} successfully")
    else:
        if name not in parked_cars:
            print(f"ERROR: user {name} not found")
            continue
        print(f"{name} unregistered successfully")
        del(parked_cars[name])

for key, value in parked_cars.items():
    print(f"{key} => {value}")
