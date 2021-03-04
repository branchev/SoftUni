class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        total = 1
        for x in args:
            total *= x
        return total

    @staticmethod
    def divide(*args):
        total = args[0]
        if len(args) > 1:
            for i in range(1, len(args)):
                total /= args[i]
            return total
        return total

    @staticmethod
    def subtract(*args):
        total = args[0]
        if len(args) > 1:
            for i in range(1, len(args)):
                total -= args[i]
            return total
        return total

#
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
