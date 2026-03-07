import unittest
import math
from src.python_fundamental.class_operations.circle import Circle


class TestCircle(unittest.TestCase):

    # create circle object
    def setUp(self):
        self.circle = Circle(5)

    # test default radius
    def test_radius_value(self):
        self.assertEqual(self.circle.radius, 5)

    # test perimeter calculation
    def test_get_perimeter(self):
        expected_perimeter = 2 * 5 * math.pi

        self.assertAlmostEqual(
            self.circle.get_perimeter(),
            expected_perimeter
        )

    # test area calculation
    def test_get_area(self):
        expected_area = math.sqrt(5) * math.pi

        self.assertAlmostEqual(
            self.circle.get_area(),
            expected_area
        )

    # test updating radius
    def test_set_radius(self):
        self.circle.set_radius(10)

        self.assertEqual(self.circle.radius, 10)

    # edge case: radius zero
    def test_zero_radius(self):
        circle = Circle(0)

        self.assertEqual(circle.get_perimeter(), 0)
        self.assertEqual(circle.get_area(), 0)


if __name__ == "__main__":
    unittest.main()
