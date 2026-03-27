import unittest
import os
import tempfile

# import all functions from src/python_fundamental/os_operations/ modul
from src.python_fundamental.os_operations.create_dir import create_dir
from src.python_fundamental.os_operations.delete_file import delete_file
from src.python_fundamental.os_operations.list_files import list_files
from src.python_fundamental.os_operations.rename_file import rename_file

class TestOSOerations(unittest.TestCase):
    # test create_dir() 
    def test_create_dir(self):
        with tempfile.TemporaryDirectory() as tem_dir:
            new_dir = os.path.join(tem_dir, "folder")
            create_dir(new_dir)
            self.assertTrue(os.path.exists(new_dir))

    # test delete_file()
    def test_delete_file(self):
        with tempfile.NamedTemporaryFile() as temp_file:
            path = temp_file.name
            delete_file(path)
            self.assertFalse(os.path.exists(path))

    def test_list_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            open(os.path.join(temp_dir, "first_file.txt"), 'w').close()
            open(os.path.join(temp_dir, "second_file.txt"), 'w').close()
            self.assertEqual(set(list_files(temp_dir)), {"first_file.txt", "second_file.txt"})

    # test rename_file()
    def test_rename_file(self):
        with tempfile.NamedTemporaryFile() as temp_file:
            old_name = temp_file.name
            new_name = str(old_name) + "_new"
            rename_file(old_name, new_name)
            self.assertTrue(os.path.exists(new_name))
            os.remove(new_name)

if __name__ == "__main__":
    unittest.main()