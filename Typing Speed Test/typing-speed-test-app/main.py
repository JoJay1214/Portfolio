"""
References:
    word list: https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/
"""
from typing_speed_test import TypingSpeedTest
from ui import TypingSpeedTestUI


def main():
    typing_speed_test = TypingSpeedTest()
    TypingSpeedTestUI(typing_speed_test)


main()
