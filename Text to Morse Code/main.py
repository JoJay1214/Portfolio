"""
Text to Morse Code
file:   main.py
author: Joshua Jacobs
date:   4/17/2022
brief:  TKinter app that lets a user enter text into a text box and outputs to the user
        their text translated into Morse Code.

"""
from char_to_morse_code import CharToMorseCodeTranslator
from morse_code_ui import MorseCodeUI


def main():
    """
    Configures and runs the Text to Morse Code app
    """
    translator = CharToMorseCodeTranslator()
    MorseCodeUI(translator)


if __name__ == "__main__":
    main()
