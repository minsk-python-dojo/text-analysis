import unittest

import lib


class Case(unittest.TestCase):
    def test_lenght_of_str(self):
        text = 'vasia'
        result = lib.length_of_str(text)
        self.assertEqual(result, 5)

    def test_length_is_empty(self):
        text = ""
        result = lib.length_of_str(text)
        self.assertEqual(result, 0)
    
    def test_word_count(self):
        text = 'Hello, World!'
        result = lib.word_count(text)
        self.assertEqual(result, 2)

        text2 = "The Lord of the Rings"    
        result = lib.word_count(text2)
        self.assertEqual(result, 5)
    
    def test_word_count_empty(self):
        text = ''
        result = lib.word_count(text)
        self.assertEqual(result, 0)

    def test_word_count_spaces(self):
        text = 'Hello, World!  '
        result = lib.word_count(text)
        self.assertEqual(result, 2)

    def test_sentences_count_valid(self):
        text = 'I have come. It was fun!'
        result = lib.sentences_count(text)
        self.assertEqual(result, 2)

    def test_sentences_count_valid2(self):
        text = 'I have come. Was it fun?!'
        result = lib.sentences_count(text)
        self.assertEqual(result, 2)

    def test_sentences_count_valid3(self):
        text = 'My name Illia... I want!'
        result = lib.sentences_count(text)
        self.assertEqual(result, 2)

    def test_letter_count__single_word__word_length(self):
        text = 'Hello'
        expected = 5
        result = lib.letter_count(text)
        self.assertEqual(result, expected)

    def test_letter_count__single_word_with_punctuation__only_letters_counts(self):
        text = 'Hello!'
        expected = 5
        result = lib.letter_count(text)
        self.assertEqual(result, expected)

    def test_letter_count__single_word_with_digits__only_letters_without_digits(self):
        text = 'Hello123'
        expected = 5
        result = lib.letter_count(text)
        self.assertEqual(result, expected)

    def test_letter_count__two_words__only_letters(self):
        text = 'Hello world'
        expected = 10
        result = lib.letter_count(text)
        self.assertEqual(result, expected)

    def test_filter_of_letters__return_True_for_char(self):
        char = 'Q'
        result = lib.filter_of_letter(char)
        self.assertTrue(result)

    def test_filter_of_letters__return_False_for_string(self):
        char = 'YIGYILvfjhvf'
        result = lib.filter_of_letter(char)
        self.assertFalse(result)

    def test_filter_of_letters__return_False_for_punctuation(self):    
        char = '!'
        result = lib.filter_of_letter(char)
        self.assertFalse(result)
    
    def test_filter_of_letters__return_False_for_number(self):    
        char = '7'
        result = lib.filter_of_letter(char)
        self.assertFalse(result)
