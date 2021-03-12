
class Product:
    def __init__(self,name, price):
        self.__name = name
        self.__price = round(price, 2)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

