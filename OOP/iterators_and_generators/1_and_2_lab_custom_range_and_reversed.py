class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.Iterator(self)

    def __reversed__(self):
        return self.Iterator(self, is_reversed = True)

    class Iterator:
        def __init__(self, custom_range_obj, is_reversed=False):
            self.custom_range_obj = custom_range_obj
            self.is_reversed = is_reversed

            if self.is_reversed:
                self.value = self.custom_range_obj.end
            else:
                self.value = self.custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_range_obj.end \
                    or self.value < self.custom_range_obj.start:
                raise StopIteration

            value = self.value
            if self.is_reversed:
                self.value -= 1
            else:
                self.value += 1
            return value


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)

for x in reversed(one_to_ten):
    print(f"reversed {x}")

