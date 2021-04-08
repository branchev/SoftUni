from project.player.player import Player


class Advanced(Player):
    INITIAL_HEALTH_POINTS = 250

    def __init__(self, username):
        super().__init__(username, health=Advanced.INITIAL_HEALTH_POINTS)
