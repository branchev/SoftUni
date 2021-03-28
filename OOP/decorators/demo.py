def uppercase(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return res.upper()
    return wrapper


@uppercase
def say_hi(name):
    return f"Hi from {name}"


print(say_hi("Boris"))


# Decorator which receives argument


def adder(n):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs)
            return res + n
        return wrapper
    return decorator


@adder(3)
def calculate(x):
    return x * 2




