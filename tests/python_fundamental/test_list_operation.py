import unittest

# 		src/python_fundamental/list_operations/frequency_counter
from src.python_fundamental.list_operations.frequency_counter import count_of_frequency

# 		src/python_fundamental/list_operations/min_max
from src.python_fundamental.list_operations.min_max import max_value, min_value

# 		src/python_fundamental/list_operations/reverse_list
from src.python_fundamental.list_operations.reverse_list import reverse

#		src/python_fundamental/list_operations/sort
from src.python_fundamental.list_operations.sort import insertion_sort, merge_sort



class TestListOperation(unittest.TestCase):
	# test count_of_frequency() in normal case
	def test_count_of_frequency_normal(self):
		self.assertEqual(count_of_frequency([1, 3, 5, 6, 3, 5, 2, 6, 6]), {1:1, 2:1, 3:2, 5:2, 6:3})
	
	# test count_of_frequency() in empty case
	def test_count_of_frequency_empty(self):
		self.assertEqual(count_of_frequency([]), {})

	# test min() in normal cases
	def test_min_normal(self):
		self.assertEqual(min_value([4, 56, 34, 11, 28, 12, 67, 34]), 4)
		self.assertEqual(min_value([4]), 4)

	# test min() in empty case
	def test_min_empty(self):
		self.assertEqual(min_value([]), None)

	# test max() in normal case
	def test_max_normal(self):
		self.assertEqual(max_value([4, 56, 34, 11, 28, 12, 67, 34]), 67)
		self.assertEqual(max_value([5]), 5)
	
	# test max() in empty case
	def test_max_empty(self):
		self.assertEqual(max_value([]), None)

	# test reverse() in normal case
	def test_reverse_normal(self):
		self.assertEqual(reverse([3, 5, 34, 67, 45, 23, 6, 34]), [34, 6, 23, 45, 67, 34, 5, 3])
		self.assertEqual(reverse([5]), [5])

	# test reverse() in empty case
	def test_reverse_empty(self):
		self.assertEqual(reverse([]), [])

	# test insertion_sort() in normal case
	def test_insertion_sort_normal(self):
		arr: list[int] = [5, 3, 7, 9, 13, 38, 2, 78, 51, 0, 1]
		insertion_sort(arr)
		self.assertEqual(arr, [0, 1, 2, 3, 5, 7, 9, 13, 38, 51, 78]) 

	# test insertoin_sort() in empty case
	def test_insertion_sort_empty(self):
		arr: list[int] = []
		insertion_sort(arr)
		self.assertEqual(arr, [])

	# test merge_sort() in normal case
	def test_merge_sort_normal(self):
		arr: list[int] = [5, 3, 2, 7, 3, 23, 11, 8, 34, 52, 1]
		merge_sort(arr)
		self.assertEqual(arr, [1, 2, 3, 3, 5, 7, 8, 11, 23, 34, 52])

	# test merger_sort() in empty case
	def test_merge_sort_empty(self):
		arr: list[int] = []
		merge_sort(arr)
		self.assertEqual(arr, [])

if __name__ == "__main__":
	unittest.main() 
