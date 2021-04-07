from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.monthly_expenses
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            if room.budget_enough:
                new_budget = room.budget - room.monthly_expenses
                output.append(f"{room.family_name} paid {room.monthly_expenses:.2f}$ and have {new_budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return "\n".join(output)

    def status(self):
        output = ""
        all_people_in_the_hotel = sum([x.members_count for x in self.rooms])
        output += f"Total population: {all_people_in_the_hotel}\n"

        for room in self.rooms:
            output += f"{room.family_name} with {room.members_count} members. " \
                      f"Budget: {room.budget}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                for c in room.children:
                    output += f"--- Child {room.children.index(c) + 1} monthly cost: {c.cost * 30:.2f}$\n"
            cost_of_all_appliances_for_one_month = sum([x.cost for room in self.rooms for x in room.appliances])
            output += f"--- Appliances monthly cost: {cost_of_all_appliances_for_one_month * 30:.2f}$\n"

        return output



