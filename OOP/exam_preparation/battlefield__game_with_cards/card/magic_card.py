from project.card.card import Card


class MagicCard(Card):
    DAMAGE_POINTS = 5
    HEALTH_POINTS = 80

    def __init__(self, username):
        super().__init__(
            username,
            damage_points=MagicCard.DAMAGE_POINTS,
            health_points=MagicCard.HEALTH_POINTS)


