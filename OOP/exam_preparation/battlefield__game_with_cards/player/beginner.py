from project.player.player import Player


class Beginner(Player):
    INITIAL_HEALTH_POINTS = 50

    def __init__(self, username):
        super().__init__(username, health=Beginner.INITIAL_HEALTH_POINTS)

