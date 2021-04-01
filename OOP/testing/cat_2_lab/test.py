from testing.cat_2_lab.cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Katy")

    def test_is_initialized(self):
        self.assertEqual(self.cat.name, "Katy")

    def test_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_is_error_raised_after_trying_to_eat_twice(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual(str(exc.exception), "Already fed.")

    def test_is_error_raised_after_trying_to_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(str(exc.exception), "Cannot sleep while hungry")

    def test_is_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

