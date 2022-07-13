"""
Typing Speed Test
file:   typing_speed_test.py
author: Joshua Jacobs
date:   3/14/2022
brief:  Typing Speed Test game that stores typed words and scores based on if the word was typed correctly. No
        time is applied in this class--only the word storing and scoring functionality.

"""

# EXTERNAL LIBRARY IMPORTS
import random


class TypingSpeedTest:
    """
    Typing Speed Test game that stores typed words and scores based on if the word was
    typed correctly. No time is applied in this class--only the word storing and scoring functionality
    """

    """
    CONSTANTS
    """

    WORD_LEN_MIN = 1
    WORD_LEN_MAX = 7

    """
    CONSTRUCTOR
    """

    def __init__(self):
        """
        Constructor for the Typing Speed Test object
        """

        self.__words = []        # the word pool
        self.__given_words = []  # the words that have been pulled from the word pool
        self.__typed_words = []  # the words that have been submitted by the user

        self.__score = 0         # the current score in the test

    def restart_game(self):
        """
        Fill word pool and shuffle it, then init data members
        """

        # read from word list, then filter and shuffle
        with open("assets/words.txt", 'r') as infile:
            words = infile.readlines()

            words_filtered = [word.split('\n')[0] for word in words]  # split off new lines
            words_filtered = [word for word in words_filtered if '-' not in word]  # remove hyphenated words
            words_filtered = [word for word in words_filtered if len(word) >= self.WORD_LEN_MIN]
            words_filtered = [word for word in words_filtered if len(word) <= self.WORD_LEN_MAX]
            words_filtered = [word.lower() for word in words_filtered]  # lowercase any proper nouns

        random.shuffle(words_filtered)

        # init data members
        self.__words = words_filtered
        self.__given_words = []
        self.__typed_words = []
        self.__score = 0

    def get_word(self) -> str:
        """
        Get word from the word pool
        :return: The gotten word
        """

        word = self.__words.pop()
        self.__given_words.append(word)

        return word

    def store_typed_word(self, word: str):
        """
        Store word and increase score if it matches the last word appended to the given words
        :param word: The word to store
        """

        self.__typed_words.append(word)

        if word == self.__given_words[-1]:
            self.__score += 1

    def get_score_str(self) -> str:
        """
        Calculate and return the current score in the test
        :return: A string of the current score
        """

        score = 0

        for i in range(len(self.__typed_words)):

            # if the word was typed correctly...
            if self.__typed_words[i] == self.__given_words[i]:
                score += len(self.__typed_words[i]) + 1  # append amount of characters from word, +1 for return key

        # return the total number of characters from the words gotten correct, divided by 5
        return f"{score / 5}"
