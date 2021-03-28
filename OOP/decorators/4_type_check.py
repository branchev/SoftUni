def type_check(type_given):
    def decorator(fn):
        def wrapper(argument):
            if type_given == type(argument):
                return fn(argument)
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
