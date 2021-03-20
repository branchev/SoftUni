from polymorphism.animals.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return "Hiss"

#
# t = Tomcat("Tom", 4)
# print(t.make_sound())
# print(t.gender)

