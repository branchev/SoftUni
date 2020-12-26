n = int(input())

cars = {}
for _ in range(n):
    info = input()
    car, mileage, fuel_range = info.split("|")
    cars[car] = {}
    cars[car]['mileage'] = int(mileage)
    cars[car]['fuel'] = int(fuel_range)

while True:
    line = input()
    if line == "Stop":
        break
    tokens = line.split(" : ")
    command = tokens[0]
    if command == "Drive":
        car, distance, fuel = tokens[1:]
        distance = int(distance)
        fuel = int(fuel)
        if car not in cars:
            continue
        if cars[car]['fuel'] - fuel < 0:
            print(f"Not enough fuel to make that ride")
            continue
        else:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]['mileage'] >= 100_000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif command == "Refuel":
        car, fuel = tokens[1:]
        fuel = int(fuel)
        if cars[car]['fuel'] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        car, kms = tokens[1:]
        kms = int(kms)
        if cars[car]['mileage'] - kms < 10_000:
            cars[car]['mileage'] = 10_000
            continue
        cars[car]['mileage'] -= kms
        print(f"{car} mileage decreased by {kms} kilometers")

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for car in sorted_cars:
    print(f"{car[0]} -> Mileage: {car[1]['mileage']} kms, Fuel in the tank: {car[1]['fuel']} lt.")
