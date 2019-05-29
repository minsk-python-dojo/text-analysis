#!/usr/bin/env python3
import sys

from lib import *


def reader_counter(file_name: str) -> None:
    with open(file_name) as fl:
        text = fl.read()
        len_of_text = length_of_str(text)
        num_of_words = word_count(text)
        number_of_sentence = sentences_count(text) 
        number_of_letter = letter_count(text)
        print(
            f'Length of our text is {len_of_text}\n'
            f'Number of words is {num_of_words}\n'
            f'Number of sentences is {number_of_sentence}\n'
            f'Number of letter is {number_of_letter}\n'
        )


if __name__ == "__main__":
    reader_counter(sys.argv[1])
