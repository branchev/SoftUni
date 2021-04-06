from typing import List

from medicine.medicine import Medicine
from supply.supply import Supply
from survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.suppliers = []
        self.medicine = []

    @property
    def food(self):
        result = [x for x in self.suppliers if x.__name__ == "FoodSupply"]
        if not result:
            raise IndexError("There are no food supplies left!")
        return result

    @property
    def water(self):
        result = [x for x in self.suppliers if x.__name__ == "WaterSupply"]
        if not result:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [x for x in self.suppliers if x.__name__ == "PainkillerSupply"]
        if not result:
            raise IndexError("There are no painkillers supplies left!")
        return result

    @property
    def salves(self):
        result = [x for x in self.suppliers if x.__name__ == "SalveSupply"]
        if not result:
            raise IndexError("There are no salves supplies left!")
        return result

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.suppliers.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        for index in range(len(self.medicine), -1 , -1):
            if self.medicine[index].__name__ == medicine_type:
                self.medicine.pop(index).apply(survivor)
                return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type):
        for index in range(len(self.suppliers), -1, -1):
            if self.suppliers[index].__name__ == sustenance_type:
                self.suppliers.pop(index).apply(survivor)
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            food = [x for x in self.suppliers if x.__name__=="FoodSupply"].pop(0)
            water = [x for x in self.suppliers if x.__name__=="WaterSupply"].pop(0)
            food.apply(survivor)
            water.apply(survivor)