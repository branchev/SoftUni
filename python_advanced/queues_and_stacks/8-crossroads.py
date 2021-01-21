from collections import deque

GREEN_LIGHT = int(input())
green_timer = GREEN_LIGHT

FREE_WINDOW = int(input())
free_timer = FREE_WINDOW

safe = True

cars_passed = []
waiting_cars = deque()
car_inside = deque()

while safe:
    model = input()
    if model == "END":
        break
    elif model == "green":
        current_car = waiting_cars.popleft()
        for ch in current_car:
            car_inside.append(ch)
        for _ in range(green_timer):
            if car_inside:
                car_inside.popleft()
            else:
                cars_passed.append(current_car)
                if waiting_cars:
                    current_car = waiting_cars.popleft()
                    for ch in current_car:
                        car_inside.append(ch)
                else:
                    break
            green_timer -= 1
        green_timer = GREEN_LIGHT
        if car_inside:
            for _ in range(free_timer):
                free_timer -= 1
                if car_inside:
                    car_inside.popleft()
                else:
                    cars_passed.append(current_car)
                    break
            if car_inside:
                safe = False
                print("A crash happened!")
                print(f"{current_car} was hit at {car_inside.popleft()}.")
                break
            else:
                free_timer = FREE_WINDOW
    else:
        waiting_cars.append(model)

if safe:
    print("Everyone is safe.")
    print(f"{len(cars_passed)} total cars passed the crossroads.")

