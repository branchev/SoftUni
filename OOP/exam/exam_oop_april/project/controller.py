from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        searched_aquarium = self.get_aquarium(aquarium_name)
        searched_decoration = self.get_decoration(decoration_type)
        if searched_aquarium and searched_decoration and searched_decoration:
            searched_aquarium.add_decoration(searched_decoration)
            self.decorations_repository.remove(searched_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        if not searched_decoration:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."
        searched_aquarium = self.get_aquarium(aquarium_name)
        if searched_aquarium.__class__.__name__ != fish_type:
            return "Water not suitable."
        if not searched_aquarium.is_enough_capacity:
            return "Not enough capacity."
        if fish_type == "FreshwaterFish":
            result = searched_aquarium.add_fish(FreshwaterFish(fish_name, fish_species, price))
        else:
            result = searched_aquarium.add_fish(SaltwaterFish(fish_name, fish_species, price))
        return result

    def feed_fish(self, aquarium_name: str):
        searched_aquarium = self.get_aquarium(aquarium_name)
        [x.eat() for x in searched_aquarium.fish]
        return f"Fish fed: {len(searched_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        searched_aquarium = self.get_aquarium(aquarium_name)
        fish_total_price = sum([x.price for x in searched_aquarium.fish])
        decoration_total_price = sum([x.price for x in searched_aquarium.decorations])
        value = fish_total_price + decoration_total_price
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        output = []
        for aq in self.aquariums:
            output.append(str(aq))
        return '\n'.join(output)

    def get_aquarium(self, aquarium_name):
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                return aq
        return None

    def get_decoration(self, dec_type):
        for d in self.decorations_repository.decorations:
            if d.__class__.__name__ == dec_type:
                return d
        return None
