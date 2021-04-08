from project.card.card import Card
from typing import List


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards: List[Card] = []

    def add(self, card: Card):
        if self.find(card.name):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")

        searched_card = self.find(card)
        if searched_card:
            self.cards.remove(searched_card)
            self.count -= 1

    def find(self, name: str):
        try:
            return [x for x in self.cards if x.name == name][0]
        except IndexError:
            return None

