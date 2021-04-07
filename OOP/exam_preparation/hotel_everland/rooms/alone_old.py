from project.rooms.room import Room


class AloneOld(Room):
    room_cost = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(name=family_name, budget=pension, members_count=1)
        self.monthly_expenses = self.calculate_monthly_expenses(room_price=10)
        self.expenses = self.monthly_expenses - self.room_cost


ao = AloneOld("Pepo", 200)
print(ao.monthly_expenses)
