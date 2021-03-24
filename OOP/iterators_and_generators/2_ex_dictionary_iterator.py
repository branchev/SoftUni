class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = list(enumerate(dict_obj.items()))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.dict_obj) == 0:
            raise StopIteration

        index, pair = self.dict_obj.pop(0)
        return pair

#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
