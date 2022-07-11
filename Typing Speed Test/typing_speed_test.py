import random

WORD_LEN_MIN = 4
WORD_LEN_MAX = 7
TEST_LEN_SEC = 60


class TypingSpeedTest:
    def __init__(self):
        self.__words = []
        self.__given_words = []
        self.__typed_words = []

        self.__score = 0

    def restart_game(self):
        with open("words.txt", 'r') as infile:
            words = infile.readlines()

            words_filtered = [word.split('\n')[0] for word in words]  # split off new lines
            words_filtered = [word for word in words_filtered if '-' not in word]  # remove hyphenated words
            words_filtered = [word for word in words_filtered if len(word) >= WORD_LEN_MIN]
            words_filtered = [word for word in words_filtered if len(word) <= WORD_LEN_MAX]
            words_filtered = [word.lower() for word in words_filtered]  # lowercase any proper nouns
        random.shuffle(words_filtered)

        self.__words = words_filtered
        self.__given_words = []
        self.__typed_words = []
        self.__score = 0

    def get_word(self):
        word = self.__words.pop()
        self.__given_words.append(word)
        return word

    def store_typed_word(self, word):
        self.__typed_words.append(word)
        if word == self.__given_words[-1]:
            self.__score += 1

    def get_score_str(self):
        return f"{self.__score}/{len(self.__given_words)}"
