from collections import deque
import sys


def calculation_of_pureness(nums):
    result = 0
    for i in range(len(nums)):
        result += i * nums[i]
    return result


def best_list_pureness(*args):
    best_pureness = -sys.maxsize - 1
    best_rotation = 1
    list_of_nums, rotations = args

    list_of_nums = deque(list_of_nums)
    for rotation in range(rotations):
        result = calculation_of_pureness(list_of_nums)
        if result > best_pureness:
            best_pureness = result
            best_rotation = rotation
        list_of_nums.rotate()
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
