from collections import deque

pumps = int(input())

tokens = deque()
for _ in range(pumps):
    line = [int(x) for x in input().split()]
    tokens.append(line)

not_passed = True

fuel_in_tank = 0
pump_to_start_the_tour = 0
while not_passed:
    for pump in tokens:
        if pump == tokens[-1]:
            not_passed = False
            break
        added_fuel, needed_fuel = pump[:]
        if fuel_in_tank + added_fuel >= needed_fuel:
            fuel_in_tank += added_fuel
            fuel_in_tank -= needed_fuel
        else:
            pump_to_start_the_tour += 1
            fuel_in_tank = 0
            tokens.rotate(-1)
            break

print(pump_to_start_the_tour)
