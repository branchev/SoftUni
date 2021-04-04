from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(50, 100)

    def test_is_properly_initiated(self):
        self.assertEqual(self.car.fuel, 50)
        self.assertEqual(self.car.capacity, 50)
        self.assertEqual(self.car.horse_power, 100)
        self.assertEqual(self.car.fuel_consumption, 1.25)

    def test_drive_if_the_fuel_is_enough(self):
        self.car.drive(4)
        self.assertEqual(self.car.fuel, 45)

    def test_trying_to_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as exc:
            self.car.drive(100000)
        self.assertEqual(str(exc.exception), "Not enough fuel")
        self.assertEqual(self.car.fuel, 50)

    def test_refuel_with_amount_less_then_the_fuel_capacity(self):
        self.car.drive(20)
        self.assertEqual(self.car.fuel, 25)
        self.car.refuel(25)
        self.assertEqual(self.car.fuel, 50)

    def test_trying_to_refuel_with_amount_more_then_the_capacity(self):
        self.car.drive(20)
        with self.assertRaises(Exception) as exc:
            self.car.refuel(50)
        self.assertEqual(str(exc.exception), "Too much fuel")

    def test_string_repr_of_the_class(self):
        self.assertEqual(str(self.car),
                         "The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption"
                         )


if __name__ == "__main__":
    main()
