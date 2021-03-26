def get_primes(nums):
    for x in nums:
        is_prime = True

        if x in (0, 1):
            continue

        for n in range(2, x):
            if x % n == 0:
                is_prime = False
                break

        if is_prime:
            yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
