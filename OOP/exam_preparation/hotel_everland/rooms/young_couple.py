from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    room_cost = 20
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(name=family_name,budget=salary_one+salary_two, members_count=2)
        self.monthly_expenses = self.calculate_monthly_expenses(self.appliances, room_price=self.room_cost)
        self.expenses = self.monthly_expenses - self.room_cost


young_couple = YoungCouple("Johnsons", 150, 205)
print(young_couple.monthly_expenses)