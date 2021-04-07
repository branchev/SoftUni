from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    appliances = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(name=family_name,budget=pension_one+pension_two, members_count=2)
        self.monthly_expenses = self.calculate_monthly_expenses(self.appliances,room_price=self.room_cost)
        self.expenses = self.monthly_expenses - self.room_cost


oc = OldCouple("Peshevi", 250, 200)
print(oc.monthly_expenses)
