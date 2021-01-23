def printing(parked_cars):
    if parked_cars:
        for car in parked_cars:
            print(car)
    else:
        print("Parking Lot is Empty")


def parking_lot(n):
    parked_cars = set()
    for _ in range(n):
        direction, number = input().split(', ')
        if direction == "IN":
            parked_cars.add(number)
        else:
            parked_cars.remove(number)
    printing(parked_cars)


n = int(input())
parking_lot(n)