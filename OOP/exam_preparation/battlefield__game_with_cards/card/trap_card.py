from project.card.card import Card


class TrapCard(Card):
    DAMAGE_POINTS = 120
    HEALTH_POINTS = 5

    def __init__(self, username):
        super().__init__(
            username,
            damage_points=TrapCard.DAMAGE_POINTS,
            health_points=TrapCard.HEALTH_POINTS)


