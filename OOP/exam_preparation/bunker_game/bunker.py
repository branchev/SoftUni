from typing import List

from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: List[Survivor] = []
        self.supplies: List[Supply] = []
        self.medicine: List[Medicine] = []
    
    @property
    def food(self):
        result = [x for x in self.supplies
                  if x.__class__.__name__ == "FoodSupply"]
        if not result:
            raise IndexError("There are no food supplies left!")
        return result
    
    @property
    def water(self):
        result = [x for x in self.supplies
                  if x.__class__.__name__ == "WaterSupply"]
        if not result:
            raise IndexError("There are no water supplies left!")
        return result

    @property
    def painkillers(self):
        result = [x for x in self.supplies
                  if x.__class__.__name__ == "Painkiller"]
        if not result:
            raise IndexError("There are no painkillers left!")
        return result
    
    @property
    def salves(self):
        result = [x for x in self.supplies
                  if x.__class__.__name__ == "Salve"]
        if not result:
            raise IndexError("There are no salves left!")
        return result

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(
                f"Survivor with name {survivor.name} already exists.")

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            searched_medicine_product = self.get_medicine(medicine_type)
            searched_medicine_product.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            searched_sustenance_product = self.get_supply(sustenance_type)
            searched_sustenance_product.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")

    def get_medicine(self, medicine_type):
        for index in range(len(self.medicine) - 1, -1, -1):
            if medicine_type == self.medicine[index].__class__.__name__:
                return self.medicine.pop(index)

    def get_supply(self, sustenance_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            if sustenance_type == self.supplies[index].__class__.__name__:
                return self.supplies.pop(index)
