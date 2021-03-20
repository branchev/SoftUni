from polymorphism.wild_farm.animals.animal import Bird
from polymorphism.wild_farm.food import *


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
        return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity
