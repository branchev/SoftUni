def age_assignment(*args, **kwargs):
    return {ar: kwargs[ar[0]] for ar in args}
    # for ar in args:
    #     result[ar] = kwargs[ar[0]]
    # return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
