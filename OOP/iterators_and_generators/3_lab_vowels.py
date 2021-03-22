class Vowels:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self.Iterator(self)

    def __reversed__(self):
        return self.Iterator(self, is_reversed=True)

    class Iterator:
        def __init__(self, vowels_obj, is_reversed=False):
            self.vowels_obj = vowels_obj
            self.is_reversed = is_reversed
            if is_reversed:
                self.index = len(self.vowels_obj.data) - 1
            else:
                self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            vowels_mapper = ("a", "e", "i", "o", "u", "y")

            if self.is_reversed:
                ci = self.index
                self.index -= 1
            else:
                ci = self.index
                self.index += 1

            if ci == len(self.vowels_obj.data) or ci < 0:
                raise StopIteration()

            if self.vowels_obj.data[ci].lower() in vowels_mapper:
                return self.vowels_obj.data[ci]

            return self.__next__()


my_string = Vowels('Abcedifuty0o')
for char in my_string:
    print(char)

for c in reversed(my_string):
    print(f"rev {c}")
