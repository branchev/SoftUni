from collections import deque

# !!! UNKNOWN BUSINESS LOGIC - possible to replace 1 and 2.


# 1. special case check - if m or f divisible by 25 without reminder
def is_special_case(value):
    if value % 25 == 0:
        return True
    return False


# 2. validate the value before trying to match
def valid_value_check(value):
    if value > 0:
        return True
    return False


# 3. compare the values of both m and f
def is_match(m, f):
    if m == f:
        return True
    return False


# 4. print the output
def output_print(m, f, matches_n):
    print(f"Matches: {matches_n}")
    if m:
        m = ', '.join([str(x) for x in list(m)[::-1]])
    else:
        m = "none"
    if f:
        f = ', '.join([str(x) for x in list(f)])
    else:
        f = "none"
    print(f"Males left: {m}")
    print(f"Females left: {f}")


def run_the_app():
    mans = deque([int(x) for x in input().split(' ')])
    fems = deque([int(x) for x in input().split(' ')])

    matches = 0

    while True:
        if not mans or not fems:
            break
        m = mans.pop()
        f = fems.popleft()

        # 2. check for positive values
        if not valid_value_check(m):
            fems.appendleft(f)
            continue
        if not valid_value_check(f):
            mans.append(m)
            continue

        # 1. check for special case
        if is_special_case(m):
            mans.pop()
            continue
        if is_special_case(f):
            fems.popleft()
            continue

        # 3 check for match
        if is_match(m, f):
            matches += 1
            continue
        else:
            m -= 2
            mans.append(m)

    # 4. print the output
    output_print(mans, fems, matches)


run_the_app()


