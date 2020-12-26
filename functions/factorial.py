def factorial(n):
    multiplicators = [n for n in range(n, 0, -1)]
    result = 1
    for x in multiplicators:
        result = result * x
    return result


def result_of_factorial_devision(n_1, n_2):
    first_factorial = factorial(n_1)
    seccond_factorial = factorial(n_2)
    result = (first_factorial / seccond_factorial)
    return f"{result:.2f}"


n_1 = int(input())
n_2 = int(input())

print(result_of_factorial_devision(n_1, n_2))
