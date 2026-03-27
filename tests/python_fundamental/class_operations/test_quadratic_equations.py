import unittest
from src.python_fundamental.class_operations.quadratic_equations import QuadraticEquations


class TestQuadraticEquations(unittest.TestCase):

    # create equation object
    def setUp(self):
        # equation: x² + 5x + 6
        self.eq = QuadraticEquations(1, 5, 6)

    # test coefficients
    def test_coefficients(self):
        self.assertEqual(self.eq.get_a(), 1)
        self.assertEqual(self.eq.get_b(), 5)
        self.assertEqual(self.eq.get_c(), 6)

    # test discriminant calculation
    def test_discriminant(self):
        self.assertEqual(self.eq.get_discriminant(), 1)

    # test first root
    def test_root1(self):
        self.assertAlmostEqual(self.eq.get_root1(), -2)

    # test second root
    def test_root2(self):
        self.assertAlmostEqual(self.eq.get_root2(), -3)

    # edge case: discriminant < 0
    def test_no_real_roots(self):
        eq = QuadraticEquations(1, 2, 5)

        self.assertEqual(eq.get_root1(), (-1 +2j))
        self.assertEqual(eq.get_root2(), (-1 -2j))


if __name__ == "__main__":
    unittest.main()
