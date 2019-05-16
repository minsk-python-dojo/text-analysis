import unittest


import main

class Case(unittest.TestCase):
    def test_lenght_of_str(self):
        text = 'vasia'
        result = main.length_of_str(text)
        self.assertEqual(result, 5)

    def test_length_is_empty(self):
        text = ""
        result = main.length_of_str(text)
        self.assertEqual(result, 0)
    
    def test_word_count(self):
        text = 'Hello, World!'
        result = main.word_count(text)
        self.assertEqual(result, 2)

        text2 = "The Lord of the Rings"    
        result = main.word_count(text2)
        self.assertEqual(result, 5)
    
    def test_word_count_empty(self):
        text = ''
        result = main.word_count(text)
        self.assertEqual(result, 0)

    def test_word_count_spaces(self):
        text = 'Hello, World!  '
        result = main.word_count(text)
        self.assertEqual(result, 2)