class Room:
    days_in_month = 30
    appliances = []

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.monthly_expenses = self.calculate_monthly_expenses(room_price=0)

    @property
    def budget_enough(self):
        if self.budget >= self.monthly_expenses:
            return True
        return False

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for list_with_objects in args:
            for obj in list_with_objects:
                result += obj.cost
        self.expenses(result)

    def calculate_monthly_expenses(self, *appliances, room_price=0):
        result = 0
        for x in appliances:
            for y in x:
                if y.__class__.__name__ != "Child":
                    result += y.cost * self.members_count
                else:
                    result += y.cost
        return result * self.days_in_month + room_price


