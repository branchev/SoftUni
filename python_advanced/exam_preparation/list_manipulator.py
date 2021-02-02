from collections import deque


def add_to_list(given_list, side, args):
    given_list = deque(given_list)
    if side == "beginning":
        for i in range(-1, -len(args)-1, -1):
            given_list.appendleft(args[i])
    elif side == "end":
        for item in args:
            given_list.append(item)
    return list(given_list)


def remove_from_list(given_list, side, args=None):
    given_list = deque(given_list)
    if side == "beginning":
        if not args:
            given_list.popleft()
        else:
            for _ in range(int(args)):
                given_list.popleft()
    elif side == "end":
        if not args:
            given_list.pop()
        else:
            for _ in range(int(args)):
                given_list.pop()
    return list(given_list)


def list_manipulator(given_list, command, side, *args):
    if command == "add":
        given_list = add_to_list(given_list, side, args)
    elif command == "remove":
        given_list = remove_from_list(given_list, side, *args)
    return given_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
