import unittest

# Import all functions from src/python_fundamental/
from src.python_fundamental.list_operations.frequency_counter import count_of_frequency
from src.python_fundamental.list_operations.min_max import max_value, min_value
from src.python_fundamental.list_operations.reverse_list import reverse
from src.python_fundamental.list_operations.sort import insertion_sort, merge_sort

class TestListOperations(unittest.TestCase):

    def setUp(self):
        
        self.normal_list = [1, 3, 5, 6, 3, 5, 2, 6, 6]
        self.empty_list = []
        self.single_element_list = [42]
        self.unsorted_list = [5, 3, 7, 9, 13, 38, 2, 78, 51, 0, 1]
        self.duplicate_list = [5, 3, 2, 7, 3, 23, 11, 8, 34, 52, 1]

    # ------------------ Frequency Counter ------------------ #
    
	# test count_of_frequency() in normal case
    def test_count_of_frequency_normal(self):
        expected = {1:1, 2:1, 3:2, 5:2, 6:3}
        self.assertEqual(count_of_frequency(self.normal_list), expected)

	# test count_of_frequency() in empty case
    def test_count_of_frequency_empty(self):
        self.assertEqual(count_of_frequency(self.empty_list), {})

	# test count_of_frequency() in single case
    def test_count_of_frequency_single(self):
        self.assertEqual(count_of_frequency(self.single_element_list), {42: 1})


    # ------------------ Min & Max ------------------ #
    
	# test min_value() in normal case
    def test_min_normal(self):
        self.assertEqual(min_value(self.normal_list), 1)

	# test min_value() in empty case
    def test_min_empty(self):
        self.assertIsNone(min_value(self.empty_list))

	# test min_value in single case
    def test_min_single(self):
        self.assertEqual(min_value(self.single_element_list), 42)

	# test max_value() in normal case
    def test_max_normal(self):
        self.assertEqual(max_value(self.normal_list), 6)

	# test max_value() in empty case
    def test_max_empty(self):
        self.assertIsNone(max_value(self.empty_list))

	# test max_value() in single case
    def test_max_single(self):
        self.assertEqual(max_value(self.single_element_list), 42)


    # ------------------ Reverse ------------------ #
    
	# test reverse() in normal case
    def test_reverse_normal(self):
        self.assertEqual(reverse(self.normal_list), [6, 6, 2, 5, 3, 6, 5, 3, 1])

	# test reverse() in empty case
    def test_reverse_empty(self):
        self.assertEqual(reverse(self.empty_list), [])

	# test reverse() in single case
    def test_reverse_single(self):
        self.assertEqual(reverse(self.single_element_list), [42])


    # ------------------ Insertion Sort ------------------ #
    
	# test insertion_sort() in normal case
    def test_insertion_sort_normal(self):
        arr = self.unsorted_list.copy()
        insertion_sort(arr)
        self.assertEqual(arr, sorted(self.unsorted_list))

	# test insertion_sort() in empty case
    def test_insertion_sort_empty(self):
        arr = self.empty_list.copy()
        insertion_sort(arr)
        self.assertEqual(arr, [])

	# test insertion_sort() in single case
    def test_insertion_sort_single(self):
        arr = self.single_element_list.copy()
        insertion_sort(arr)
        self.assertEqual(arr, [42])


    # ------------------ Merge Sort ------------------ #
    
	# test merge_sort() in normal case
    def test_merge_sort_normal(self):
        arr = self.duplicate_list.copy()
        merge_sort(arr)
        self.assertEqual(arr, sorted(self.duplicate_list))

	# test merge_sort() in empty case
    def test_merge_sort_empty(self):
        arr = self.empty_list.copy()
        merge_sort(arr)
        self.assertEqual(arr, [])

	# test merge_sort() in single case
    def test_merge_sort_single(self):
        arr = self.single_element_list.copy()
        merge_sort(arr)
        self.assertEqual(arr, [42])


if __name__ == "__main__":
    unittest.main()