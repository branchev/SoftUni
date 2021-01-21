from collections import deque


def add_second(hours, mins, secs):
    secs += 1
    if secs == 60:
        secs = 0
        mins += 1
    if mins == 60:
        mins = 0
        hours += 1
    if hours == 24:
        hours = 0
    return hours, mins, secs


robots = input().split(";")
available_robots = deque()
working_robots = deque()
robots_info_time = {}
materials = deque()
timer = []
start = input().split(":")
for x in start:
    timer.append(int(x))

for r in robots:
    name, time = r.split("-")[0:]
    time = int(time)
    available_robots.append([name, time])
    robots_info_time[name] = int(time)

while True:
    current_material = input()
    if current_material == "End":
        break
    materials.append(current_material)

while materials:
    for rob_NA in working_robots:
        rob_NA[1] -= 1
        if rob_NA[1] == 0:
            working_time_of_robot = robots_info_time[rob_NA[0]]
            available_robots.append([rob_NA[0], working_time_of_robot])
    working_robots = [r for r in working_robots if r[1] > 0]
    timer = add_second(timer[0], timer[1], timer[2])
    h, m, s = timer[0], timer[1], timer[2]

    material = materials.popleft()
    if not available_robots:
        materials.append(material)
        continue

    if available_robots:
        current_robot = available_robots.popleft()
        working_robots.append(current_robot)
        print(f"{current_robot[0]} - {material} [{h:02d}:{m:02d}:{s:02d}]")


