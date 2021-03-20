from polymorphism.wild_farm.animals.animal import Mammal
from polymorphism.wild_farm.food import *


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += 0.1
            self.food_eaten += food.quantity
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.4 * food.quantity
            self.food_eaten += food.quantity
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += 0.3 * food.quantity
            self.food_eaten += food.quantity
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1 * food.quantity
            self.food_eaten += food.quantity
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


