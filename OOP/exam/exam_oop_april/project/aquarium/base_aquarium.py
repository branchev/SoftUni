from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration]= []
        self.fish: List[BaseFish] = []

    def calculate_comfort(self):
        return sum([dec.comfort for dec in self.decorations])

    def add_fish(self, fish):
        if self.is_enough_capacity and \
                self.is_the_fish_is_for_the_current_aquarium(fish):
            self.fish.append(fish)
            return f"Successfully added " \
                   f"{fish.__class__.__name__} to {self.name}."
        return "Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def is_the_fish_is_for_the_current_aquarium(self, fish):
        current_aquarium_name = self.__class__.__name__[:2]
        if fish.__class__.__name__.startswith(current_aquarium_name):
            return True
        return False

    def __str__(self):
        fishes = ' '.join([f.name for f in self.fish])
        if not fishes:
            fishes = "none"

        output = f"{self.name}:\n"
        output += f"Fish: {fishes}\n"
        output += f"Decorations: {len(self.decorations)}\n"
        output += f"Comfort: {self.calculate_comfort()}"
        return output

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    @property
    def is_enough_capacity(self):
        if len(self.fish) < self.capacity:
            return True
        return False

