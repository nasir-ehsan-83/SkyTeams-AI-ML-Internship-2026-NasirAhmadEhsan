import unittest
from src.python_fundamental.class_operations.bmi import BMI


class TestBMI(unittest.TestCase):

    # create a BMI object for testing
    def setUp(self):
        self.bmi = BMI("Nasir", 22, 150, 65)

    # test getter methods
    def test_get_name(self):
        self.assertEqual(self.bmi.getName(), "Nasir")

    def test_get_age(self):
        self.assertEqual(self.bmi.getAge(), 22)

    def test_get_weight(self):
        self.assertEqual(self.bmi.getWeight(), 150)

    def test_get_height(self):
        self.assertEqual(self.bmi.getHeight(), 65)

    # test BMI calculation
    def test_bmi_calculation(self):
        bmi_value = self.bmi.getBMI()

        # BMI must be a float value
        self.assertIsInstance(bmi_value, float)

        # BMI must be greater than zero
        self.assertGreater(bmi_value, 0)

    # test BMI status classification
    def test_bmi_status(self):
        status = self.bmi.getStatus()

        self.assertIn(
            status,
            ["Underweight", "Normal", "Overweight", "Obese"]
        )


if __name__ == "__main__":
    unittest.main()
