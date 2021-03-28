def logged(fn):
    def wrapper(*args, **kwargs):
        name = fn.__name__
        output = f"you called {name}{args}\nit returned {fn(*args, **kwargs)}"
        return output
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

