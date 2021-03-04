class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        try:
            return cls(int(value))
        except ValueError:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        string = value
        string = string.upper()
        total = 0
        while string:
            if len(string) == 1 or val[string[0]] >= val[string[1]]:
                total += val[string[0]]
                string = string[1:]
            else:
                total += val[string[1]] - val[string[0]]
                string = string[2:]
        return cls(total)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return f"wrong type"

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))