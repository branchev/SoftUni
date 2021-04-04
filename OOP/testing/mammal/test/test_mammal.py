from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.walker = Mammal("Walker", "Dog", "Woof")

    def test_is_properly_initiated(self):
        self.assertEqual(self.walker.name, "Walker")
        self.assertEqual(self.walker.type, "Dog")
        self.assertEqual(self.walker.sound, "Woof")

    def test_kingdom_of_the_instanced_animal(self):
        self.assertEqual(self.walker.get_kingdom(), "animals")

    def test_sound_of_the_instanced_animal(self):
        self.assertEqual(self.walker.make_sound(), "Walker makes Woof")

    def test_get_info_for_the_instanced_animal(self):
        self.assertEqual(self.walker.info(), "Walker is of type Dog")


if __name__ == "__main__":
    main()