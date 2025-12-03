import unittest
from main import calculate_average, determine_grade_letter, student_report


class TestGrades(unittest.TestCase):

    def test_average_calculation(self):
        self.assertEqual(calculate_average([90, 80, 100]), 90.0)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_average_type_error(self):
        with self.assertRaises(TypeError):
            calculate_average([90, "80", 70])

    def test_letter_grade(self):
        self.assertEqual(determine_grade_letter(95), "A")
        self.assertEqual(determine_grade_letter(82), "B")
        self.assertEqual(determine_grade_letter(75), "C")
        self.assertEqual(determine_grade_letter(65), "D")
        self.assertEqual(determine_grade_letter(40), "F")

    def test_student_report(self):
        result = student_report("Алиса", [100, 90, 80])
        self.assertIn("Алиса", result)
        self.assertIn("Средний балл", result)
        self.assertIn("A", result)


if __name__ == "__main__":
    unittest.main()
