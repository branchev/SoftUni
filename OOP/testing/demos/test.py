import unittest
from testing.demos.solution import Person


class PersonTest(unittest.TestCase):
    def test_person_is_properly_initiated(self):
        person = Person("Boris")
        uppercase_person_name = person.name.upper()
        self.assertEqual(uppercase_person_name, "BORIS")


if __name__ == "__main__":
    unittest.main()
