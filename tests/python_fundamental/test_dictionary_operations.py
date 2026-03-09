import unittest

from src.python_fundamental.dictionary_operations.common_element import find_common_elements
from src.python_fundamental.dictionary_operations.dictionary_key_invert import invert_dictionary
from src.python_fundamental.dictionary_operations.merge_profiles import merge_dictionary

class TestDictionaryOperations(unittest.TestCase):
	# test find_common_elements()
	def test_find_common_elements(self):
		self.assertEqual(find_common_elements([2, 6, 3, 7], [1, 3, 5, 7]), [3, 7])
		self.assertEqual(find_common_elements([0, 1, 2, 3], [4, 5, 6, 7]), []) 
	
	# test invert_dictionary()
	def test_invert_dictionary(self):
		self.assertEqual(invert_dictionary({"#1": "ali", "#2": "ahmad"}), {"ali": "#1", "ahmad": "#2"})
		self.assertEqual(invert_dictionary({}, {}))
		
	# test merge_dictionary()
	def test_merge_dictionary(self):
		self.assertEqual(merge_dictionary({"name": "ali", "city": "Kabul", "job": "programmer"}, {"city": "Herat", "skills": ["Python", "JS", "Java"]}), {"name": "ali", "city": "Herat", "job": "programmer", "skills": ["Python", "JS", "Java"]})
		self.assertEqual(merge_dictionary({}, {}), {})
		
if __name__ == "__main__":
	unittest.main()