import unittest
import tempfile
import json

# import all functions from src/python_fundamental/json_operations/ modul
from src.python_fundamental.json_operations.load_json import load_json
from src.python_fundamental.json_operations.update_json import update_json 
from src.python_fundamental.json_operations.validate_json import validate_keys
from src.python_fundamental.json_operations.write_json import write_json

class TestJsonOperations(unittest.TestCase):
    # test load_json()
    def test_load_json(self):
        data = {'a' : 1}
        
        with tempfile.NamedTemporaryFile('w+', delete = False) as temp:
            json.dump(data, temp)
            temp_path = temp.name

        self.assertEqual(load_json(temp_path), data)
    
    # test write_json()
    def test_write_json(self):
        data = {'b' : 2}
        with tempfile.NamedTemporaryFile('w+', delete = False) as temp:
            temp_path = temp.name
        write_json(temp_path, data)
        self.assertEqual(load_json(temp_path), data)

    # test update_json()
    def test_update_json(self):
        data = {'a' : 1}
        with tempfile.NamedTemporaryFile('w+', delete = False) as temp_file:
            json.dump(data, temp_file)
            temp_path = temp_file.name

        update_json(temp_path, 'b', 2)
        self.assertEqual(load_json(temp_path), {'a' : 1, 'b' : 2})

    # test validate_json()
    def test_validate_json(self):
        data = {'a' : 1, 'b' : 2}

        self.assertTrue(data, ['a', 'b'])
        self.assertFalse(data, ['a', 'b', 'c'])

if __name__ == "__main__":
    unittest.main()