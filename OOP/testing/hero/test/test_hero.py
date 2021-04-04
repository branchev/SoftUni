from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self):
        self.my_hero = Hero("Hero", 10, 100, 10)
        self.enemy_hero = Hero("Enemy", 5, 50, 5)

    def test_is_properly_initiated(self):
        self.assertEqual(self.my_hero.username, "Hero")
        self.assertEqual(self.my_hero.level, 10)
        self.assertEqual(self.my_hero.health, 100)
        self.assertEqual(self.my_hero.damage, 10)

    def test_trying_to_fight_with_hero_with_same_name(self):
        enemy_with_same_name = Hero("Hero", 1, 1, 1)
        with self.assertRaises(Exception) as exc:
            self.my_hero.battle(enemy_with_same_name)
        self.assertEqual(str(exc.exception), "You cannot fight yourself")

    def test_trying_to_fight_without_health(self):
        self.my_hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(exc.exception),
                         "Your health is lower than or equal to 0. You need to rest")

    def test_trying_to_fight_vs_enemy_without_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(exc.exception),
                         "You cannot fight Enemy. He needs to rest")

    def test_draw_battle_both_heroes_are_death(self):
        self.my_hero.health = 25
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(result, "Draw")

    def test_battle_that_my_hero_is_winner(self):
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(result, "You win")

    def test_battle_that_enemy_hero_is_winner(self):
        self.my_hero.health = 1
        self.my_hero.level = 1
        self.my_hero.damage = 1
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(result, "You lose")

    def test_str_repr_of_the_instanced_object(self):
        self.assertEqual(str(self.my_hero),
                         "Hero Hero: 10 lvl\nHealth: 100\nDamage: 10\n"
                         )


if __name__ == "__main__":
    main()