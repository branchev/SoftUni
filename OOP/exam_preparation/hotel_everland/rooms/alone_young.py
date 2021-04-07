from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_cost = 10
    appliances = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(name=family_name, budget=salary, members_count=1)
        self.monthly_expenses = self.calculate_monthly_expenses(self.appliances, room_price=self.room_cost)
        self.expenses = self.monthly_expenses - self.room_cost


ay = AloneYoung("Pepo", 400)
print(ay.monthly_expenses)