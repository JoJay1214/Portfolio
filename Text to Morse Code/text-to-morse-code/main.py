"""
Text to Morse Code
file:   main.py
author: Joshua Jacobs
date:   3/7/2022
brief:  Quick "Hello World" demo of the CharToMorseCodeTranslator.

references:
- Morse Code
https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg

"""
from char_to_morse_code import CharToMorseCodeTranslator


def main():
    """
    Prints "Hello World" and prints the same message, but in Morse Code using the CharToMorseCodeTranslator
    """
    translator = CharToMorseCodeTranslator()

    print("Hello World")
    print(translator.translate("Hello World"))


main()
