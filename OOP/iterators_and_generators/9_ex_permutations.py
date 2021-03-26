from itertools import permutations


def possible_permutations(nums):
    # return map(list, permutations(nums))
    for el in permutations(nums):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
