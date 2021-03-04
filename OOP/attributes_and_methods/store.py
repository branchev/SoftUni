from collections import defaultdict


class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = defaultdict(int)

    @classmethod
    def from_size (cls, name, type, size):
        capacity = size // 2
        return cls(name, type, capacity)

    def add_item(self, item_name):
        if self.items_amount() < self.capacity:
            self.items[item_name] += 1
            return f"{item_name} added to the store"
        return f"Not enough capacity in the store"

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"

    def items_amount(self):
        return sum(value for _, value in self.items.items())

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
