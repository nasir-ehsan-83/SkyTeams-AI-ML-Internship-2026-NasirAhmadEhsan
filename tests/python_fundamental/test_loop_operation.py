import unittest

from reverse import reverse_list
from sort import insertion_sort

class TestReverse(unittest.TestCase):
    def test_reverse_list(self):
        list = [4, 7, 3, 8, 2, 1, 23, 67, 0, 15, 6]
        # sorting list before reversing
        insertion_sort(list)
        self.assertEqual(reverse_list(list), [67, 23, 15, 8, 7, 6, 4, 3, 2, 1, 0])

if __name__ == "__main__":
    unittest.main()