import unittest
from context import wordle_buddy
from wordle_buddy.utilities import get_words


class MyTest(unittest.TestCase):
    def test_get_words(self):
        word_list = get_words("possible_words")
        self.assertEqual(len(word_list), 2315)
        first_word = word_list[0]
        self.assertEqual(first_word, "ABACK")
        last_word = word_list[-1]
        self.assertEqual(last_word, "ZONAL")

        word_list = get_words("allowed_words")
        self.assertEqual(len(word_list), 12972)
        first_word = word_list[0]
        self.assertEqual(first_word, "AAHED")
        last_word = word_list[-1]
        self.assertEqual(last_word, "ZYMIC")


if __name__ == "__main__":
    unittest.main()
