from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            self.bonus_for_beginners(attacker)

        if enemy.__class__.__name__ == "Beginner":
            self.bonus_for_beginners(enemy)

        self.pre_fight_bonus(attacker, enemy)

        while True:
            try:
                attacker_card = attacker.card_repository.cards.pop(0)
                enemy_card = enemy.card_repository.cards.pop(0)
            except IndexError:
                break

            enemy.take_damage(attacker_card.damage_points)
            if enemy.is_dead:
                break
            attacker.take_damage(enemy_card.damage_points)
            if attacker.is_dead:
                break

    @staticmethod
    def pre_fight_bonus(*args):
        for player in args:
            player.health += sum([x.health_points for x in player.card_repository.cards])

    @staticmethod
    def bonus_for_beginners(player):
        player.health += 40
        for x in player.card_repository.cards:
            x.damage_points += 30



