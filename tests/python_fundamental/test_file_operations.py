import unittest
import tempfile

from src.python_fundamental.file_operations.character_counter import character_count, character_count_without_spaces
from src.python_fundamental.file_operations.frequency_counter import frequency_count
from src.python_fundamental.file_operations.line_counter import line_count
from src.python_fundamental.file_operations.word_counter import word_count
from src.python_fundamental.file_operations.unique_words import unique_words

class TestFileOperations(unittest.TestCase):
    # Create a temporary file to test 
    def create_test_file(self, content: str):
        temp = tempfile.NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8")
        temp.write(content)
        temp.seek(0)
        return temp

    # test word_count()
    def test_word_count(self):
        file = self.create_test_file("python is easy")
        self.assertEqual(word_count(file), 3)
        file.close()

    # test line_count()
    def test_line_count(self):
        file = self.create_test_file("a\nb\nc")
        self.assertEqual(line_count(file), 3)
        file.close()

    # test character_count()
    def test_character_count(self):
        file = self.create_test_file("AI & ML is great!")
        self.assertEqual(character_count(file), 13)
        file.close()

    # test character_count_without_spaces()
    def test_character_count_without_spaces(self):
        file = self.create_test_file("AI & ML is great!")
        self.assertEqual(character_count_without_spaces(file), 17)
        file.close()

    # test unique_words()
    def test_unique_words(self):
        file = self.create_test_file("python java python c")
        result = unique_words(file)

        self.assertIn("java", result)
        self.assertIn("c", result)

        file.close()

    # test frequency_count
    def test_frequency_count(self):
        words = ["python", "java", "python"]

        result = frequency_count(words)

        self.assertEqual(result["python"], 2)
        self.assertEqual(result["java"], 1)

if __name__ == "__main__":
    unittest.main()