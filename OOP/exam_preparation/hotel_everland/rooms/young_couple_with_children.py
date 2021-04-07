from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    room_cost = 30
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2+len(children))
        self.monthly_expenses = self.calculate_monthly_expenses(self.appliances, children, room_price=self.room_cost)
        for c in children:
            self.children.append(c)
        self.expenses = self.expenses_calculator(self.appliances, self.members_count)

    @staticmethod
    def expenses_calculator(appliances, members_count):
        return sum([x.cost * members_count for x in appliances])


child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
print(young_couple_with_children.members_count)
print(young_couple_with_children.expenses)