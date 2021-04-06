from survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        if not result:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"]
        if not result:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "PainkillerSupply"]
        if not result:
            raise IndexError("There are no painkillers supplies left!")
        return result

    @property
    def salves(self):
        result = [x for x in self.supplies if x.__class__.__name__ == "SalveSupply"]
        if not result:
            raise IndexError("There are no salves supplies left!")
        return result

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def get_heal(self, survivor, medicine_type):
        for index in range(len(self.medicine) - 1, -1, -1):
            if self.medicine[index].__class__.__name__ == medicine_type:
                medicament = self.medicine.pop(index)
                medicament.apply(survivor)
                return f"{survivor.name} healed successfully with {medicine_type}"

    def heal(self, survivor: Survivor, medicine_type):
        if survivor.needs_healing:
            return self.get_heal(survivor, medicine_type)

    def get_sustain(self, survivor, sustenance_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[index].__class__.__name__ == sustenance_type:
                self.supplies.pop(index).apply(survivor)
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def sustain(self, survivor: Survivor, sustenance_type):
        if survivor.needs_sustenance():
            return self.get_sustain(survivor, sustenance_type)

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            food = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"].pop(0)
            water = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"].pop(0)
            food.apply(survivor)
            water.apply(survivor)

