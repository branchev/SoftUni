def fibonacci():
    fib = [0, 1]

    while True:
        next_num = fib[0] + fib[1]
        fib.append(next_num)
        yield fib.pop(0)

#
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
