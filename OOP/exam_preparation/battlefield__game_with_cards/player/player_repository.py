from project.player.player import Player
from typing import List


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players: List[Player] = []

    def add(self, player: Player):
        if self.find(player.username):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")

        searched_player =  self.find(player)
        if searched_player:
            self.players.remove(searched_player)
            self.count -= 1

    def find(self, username: str):
        try:
            return [x for x in self.players if x.username == username][0]
        except IndexError:
            return None
