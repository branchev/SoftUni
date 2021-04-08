from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type.upper() == "BEGINNER":
            self.player_repository.add(Beginner(username))
        elif type.upper() == "ADVANCED":
            self.player_repository.add(Advanced(username))
        return f"Successfully added player" \
               f" of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            self.card_repository.add(MagicCard(name))
        elif type == "Trap":
            self.card_repository.add(TrapCard(name))
        return f"Successfully added card " \
               f"of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.find_player(username)
        card = self.find_card(card_name)
        player.card_repository.add(card)

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.find_player(attack_name)
        enemy = self.find_player(enemy_name)
        BattleField().fight(attacker, enemy)

    def report(self):
        output = ""
        for player in self.player_repository.players:
            output += f"Username: {player.username} - " \
                      f"Health: {player.health} - Cards {len(player.card_repository.cards)}\n"

            for card in player.card_repository.cards:
                output += f"### Card: {card.name} - Damage: {card.damage_points}\n"

    def find_player(self, username):
        return [
            x for x in self.player_repository.players
            if x.username == username][0]

    def find_card(self, name):
        return [
            x for x in self.card_repository.cards
            if x.name == name
        ][0]


