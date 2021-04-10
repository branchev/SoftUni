from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self):
        self.train = Train("OrientExpress", 100)
        self.sec_train = Train("A", 2)

    def test_initialisation(self):
        self.assertEqual("OrientExpress", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_pass(self):
        a = self.sec_train.add("Gogo")
        self.assertEqual(1, len(self.sec_train.passengers))
        self.assertEqual("Added passenger Gogo", a)

    def test_full_cap_and_add(self):
        self.sec_train.add("a")
        self.sec_train.add("b")
        with self.assertRaises(ValueError) as ex:
            self.sec_train.add("c")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_same_named_passangers(self):
        self.sec_train.add("a")
        with self.assertRaises(ValueError) as ex:
            self.sec_train.add("a")
        self.assertEqual("Passenger a Exists", str(ex.exception))

    def test_remove_p(self):
        self.sec_train.add("a")
        a = self.sec_train.remove("a")
        self.assertEqual("Removed a", a)
        self.assertEqual(0, len(self.sec_train.passengers))

    def test_remove_unexisting(self):
        with self.assertRaises(ValueError) as ex:
            self.sec_train.remove("a")
        self.assertEqual("Passenger Not Found", str(ex.exception))


if __name__ == "__main__":
    main()
