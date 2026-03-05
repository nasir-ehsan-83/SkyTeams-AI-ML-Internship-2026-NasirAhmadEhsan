import unittest

from maximum_value import maximum_value

class TestMaximum(unittest.TestCase):
    def test_maximum_value(self):
        self.assertEqual(maximum_value([2, 65, 4, 7, 3, 7, 45, 3, 78, 34 ,12, 62]), 78)

if __name__ == "__main__":
    unittest.main()