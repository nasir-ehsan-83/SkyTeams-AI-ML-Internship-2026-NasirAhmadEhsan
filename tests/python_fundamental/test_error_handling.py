import unittest
import os

from src.python_fundamental.error_handling_operations.divide import safe_divide
from src.python_fundamental.error_handling_operations.log_error import logging_error
from src.python_fundamental.error_handling_operations.open_file import open_file_safe, FileNotFound
from src.python_fundamental.error_handling_operations.validate_int import validate_int_convert

# Helper function for test logging_error()
def raise_error():
    raise ValueError("Test error")

class TestErrorHandlingOperations(unittest.TestCase):
    # test safe_divide() in normal case
    def test_devide_normal(self):
        self.assertEqual(safe_divide(10, 2), 5)

    # test safe_divide() in error case
    def test_divide_zero(self):
        self.assertEqual(safe_divide(10, 0), "can not divide by zero")

    # test open_file_safe() 
    def test_file_mising(self):
        with self.assertRaises(FileNotFound):
            open_file_safe("non_existent_file.txt")

    # test validate_int_convert() in valid input case
    def test_valid_input(self):
        self.assertEqual(validate_int_convert("20"), 20)
        self.assertEqual(validate_int_convert(35.6), 35)
        self.assertEqual(validate_int_convert(True), 1)

    # test validate_int_convert() in invalid input case
    def test_invalid_input(self):
        self.assertIsNone(validate_int_convert("ai"))
        self.assertIsNone(validate_int_convert("34.5e"))

    # test loggin_error() 
    def test_logging_error(self):
        result = logging_error(raise_error)
        self.assertIsNone(result)

        with open('error.log', 'r') as file:
            logs = file.read()
        
        self.assertIn("Test error", logs)
        # cleanup
        os.remove('error.log') 

if __name__ == "__main__":
    unittest.main()