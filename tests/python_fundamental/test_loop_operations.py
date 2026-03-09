import unittest
# Import all functions from src/python_fundamental/class_operatoins
from src.python_fundamental.loop_operations.factor_number import factors_of_number
from src.python_fundamental.loop_operations.factorial import fact_loop, fact_recursion
from src.python_fundamental.loop_operations.fibonacci import fibonacci
from src.python_fundamental.loop_operations.gcd_lcm import gcd, lcm
from src.python_fundamental.loop_operations.prime_number import is_prime
from src.python_fundamental.loop_operations.sum_numbers import sum_of_natural_number, sum_of_odd_number, sum_of_even_number

class TestLoopOperations(unittest.TestCase):
	# test factors_of_number()
	def test_factors_of_number(self):
		self.assertEqual(factors_of_number(14), [1, 2, 7, 14])
		self.assertEqual(factors_of_number(-14), [1, 2, 7, 14])
		self.assertIsNone(factors_of_number(0))

	# test fact_loop()
	def test_factorial_by_loop(self):
		self.assertEqual(fact_loop(5), 120)
		self.assertEqual(fact_loop(0), 0)
		self.assertIsNone(fact_loop(-2))
	
	# test fact_recursion()
	def test_factorial_by_recursion(self):
		self.assertEqual(fact_recursion(5), 120)
		self.assertEqual(fact_recursion(0), 0)
		self.asserIsNone(fact_recursion(-2))
	
	# test fibonacci()
	def test_fibonacci(self):
		self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
	
	# test gcd()
	def test_gcd(self):
		self.assertEqual(gcd(18,12), 6)
		self.assertIsNone(gcd(0, 4))
		self.assertIsNone(gcd(6, 0))
		self.assertIsNone(gcd(0, 0))
	
	# test lcm()
	def test_lcm(self):
		self.assertEqual(lcm(5, 8), 40)
		self.assertIsNone(lcm(0, 6))
		self.assertIsNone(lcm(4, 0))
		self.assertIsNone(lcm(0, 0))
	
	# test is_prime()
	def test_is_prime(self):
		self.assertIsTrue(is_prime(7))
		self.assertIsFalse(is_prime(8))
		self.assertIsNone(is_prime(0))
	
	# test sum_of_natural_number()
	def test_sum_of_natural_number(self):
		self.assertEqual(sum_of_natural_number(5), 15)
		self.assertEqual(sum_of_natural_number(0), 0)
		self.assertIsNone(sum_of_natural_number(-4))
	
	# test sum_of_odd_number()
	def test_sum_of_odd_number(self):
		self.assertEqual(sum_of_odd_number(10), 25)
		self.assertIsNone(sum_of_odd_number(0))
		self.assertIsNone(sum_of_odd_number(-4))
		
	# test sum_of_even_number()
	def test_sum_of_even_number(self):
		self.assertEqual(sum_of_even_number(10), 30)
		self.assertEqual(sum_of_even_number(0), 0)
		self.assertIsNone(sum_of_even_number(-7))
		
        
if __name__ == "__main__":
    unittest.main()