class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = sum(toys_cost) + food_cost


child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
