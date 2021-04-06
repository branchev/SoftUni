class Survivor:
    def __init__(self, name, age):
        if name == "":
            raise ValueError("Name not valid!")
        self.name = name

        if age < 0:
            raise ValueError("Age not valid!")
        self.age = age

        self.__health = 100
        self.__needs = 100

    @property
    def needs_sustenance(self):
        if self.needs < 100:
            return True

    @property
    def needs_healing(self):
        if self.health < 100:
            return True

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if value > 100:
            value = 100
        self.__health = value

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        if value > 100:
            value = 100
        self.__needs = value


