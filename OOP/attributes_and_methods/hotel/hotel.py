class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def find_room_by_number(self, room_number):
        return [r for r in self.rooms if r.number == room_number][0]

    def take_room(self, room_number, people):
        room = self.find_room_by_number(room_number)
        room.take_room(people)

    def free_room(self, room_number):
        room = self.find_room_by_number(room_number)
        room.free_room()

    def print_status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]

        taken_rooms = []
        for r in self.rooms:
            if r.is_taken:
                self.guests += r.guests
                taken_rooms.append(r.number)

        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(map(str, free_rooms))}")
        print(f"Taken rooms: {', '.join(map(str, taken_rooms))}")