def make_bold(fn):
    def wrapper(*args, **kwargs):
        return f"<b>{fn(*args, **kwargs)}</b>"
    return wrapper


def make_italic(fn):
    def wrapper(*args, **kwargs):
        return f"<i>{fn(*args, **kwargs)}</i>"
    return wrapper


def make_underline(fn):
    def wrapper(*args, **kwargs):
        return f"<u>{fn(*args, **kwargs)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
