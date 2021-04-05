from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("Bob")

    def test_is_properly_initiated(self):
        self.assertEqual(self.student.name, "Bob")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(len(self.student.courses), 0)

    def test_enroll_not_existing_course(self):
        result = self.student.enroll("Python", ["OOP", "Advanced"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(len(self.student.courses), 1)
        self.assertEqual(len(self.student.courses["Python"]), 2)

    def test_enroll_existing_course_with_additional_notes(self):
        self.student.enroll("Python", ["OOP", "Advanced"], "Y")
        result = self.student.enroll("Python", ["Funds"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertIn("Funds", self.student.courses["Python"])
        self.assertEqual(len(self.student.courses["Python"]), 3)

    def test_enroll_not_existing_course_without_add_course_notes(self):
        result = self.student.enroll("Python", "test", "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(len(self.student.courses["Python"]), 0)

    def test_add_notes_to_existing_course(self):
        self.student.enroll("Python", ["Funds"])
        result = self.student.add_notes("Python", "Adv")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(len(self.student.courses["Python"]), 2)
        self.assertIn("Adv", self.student.courses["Python"])

    def test_trying_to_add_notes_to_not_existing_course(self):
        with self.assertRaises(Exception) as exc:
            self.student.add_notes("Python", "Funds")
        self.assertEqual(str(exc.exception), "Cannot add notes. Course not found.")

    def test_leave_course_that_is_existing(self):
        self.student.enroll("Python", ["Adv"])
        result = self.student.leave_course("Python")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(len(self.student.courses), 0)

    def test_trying_to_leave_course_which_is_not_existing(self):
        with self.assertRaises(Exception) as exc:
            self.student.leave_course("Python")
        self.assertEqual(str(exc.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()