import unittest

from src.python_fundamental.string_manipulations.check_isbn10 import check_isbn_10
from src.python_fundamental.string_manipulations.count_vowels import count_of_vowel
from src.python_fundamental.string_manipulations.is_palindrome import is_palindrome
from src.python_fundamental.string_manipulations.reverse_string import reverse
from src.python_fundamental.string_manipulations.word_count import word_count


class TestStringManipulations(unittest.TestCase):
	# test check_isbn_10()
	def test_check_isbn_10(self):
		self.assertEqual(check_isbn_10("013031997"), "013031997X")
		self.assertEqual(check_isbn_10("013601267"), "0136012671")
	
	# test count_of_vowels()
	def test_count_vowels(self):
		self.assertEqual(count_of_vowel("ahmad"), 2)
		self.assertEqual(count_of_vowel("I'm learning AI"), 6)
	
	# test is_palindrome()
	def test_is_palindrome(self):
		self.assertIsTrue(is_palindrome("alila"))
		self.assertIsFalse(is_palindrome("ali"))
		self.assertIsTrue(is_palindrome("ali is ali"))
		slef.assertIsFalse(is_palindrome("he is ali"))
	
	# test reverse()
	def test_reverse_string(self):
		self.assertEqusl(reverse("university"), "ytisrevinu")
		self.assertEqual(reverse("He is an AI developer"), "repoleved IA na si eh")
		
	# test word_count()
	def test_word_count(self):
		self.assertEqual(word_count("He is an AI developer"), 5)
		self.assertEqual(word_count(""), 0)
		self.assertEqual(word_count("ali"), 1)
		
if __name__ == "__main__":
	unittest.main()