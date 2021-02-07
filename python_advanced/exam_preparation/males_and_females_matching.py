from collections import deque


def is_match(m, f):
    if m == f:
        return True
    return False


def male_points_decrease(m):
    m -= 2
    if m > 0:
        return m


def special_case(g_value, g_list, g):
    if g_value % 25 == 0:
        for _ in range(2):
            if g == "m":
                g_list.pop()
            elif g == "f":
                g_list.popleft()
    return g_list


def special_check(g):
    if g % 25 == 0:
        return True
    return False


def run_the_tinder(males, females):
    matches = 0
    while males and females:
        current_m = males.pop()
        current_f = females.popleft()
        if current_m == 0:
            females.appendleft(current_f)
            continue
        elif current_f == 0:
            males.append(current_m)
            continue
        if special_check(current_m):
            males = special_case(current_m, males, "m")
            continue
        elif special_check(current_f):
            females = special_case(current_f, females, "f")
            continue
        if is_match(current_m, current_f):
            matches += 1
        else:
            if male_points_decrease(current_m):
                males.append(male_points_decrease(current_m))
    return matches, males, females


def output_printer(matches, males, females):
    print(f"Matches: {matches}")

    if males:
        print(f"Males left: {', '.join([str(m) for m in males])}")
    else:
        print("Males left: none")
    if females:
        print(f"Females left: {', '.join([str(f) for f in females])}")
    else:
        print("Females left: none")


males_deque = deque([int(x) for x in input().split()])
females_deque = deque([int(x) for x in input().split()])

matches, males, females = run_the_tinder(males_deque, females_deque)
output_printer(matches, males, females)


