"""
Text to Morse Code
file:   char_to_morse_code.py
author: Joshua Jacobs
date:   3/7/2022
brief:  Create a CharToMorseCodeTranslator object and use it to translate strings into
        Morse Code. Handles symbol characters, but does not translate them.

references:
- Morse Code
https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg

"""

# Placeholders to remind which chars I used for the Morse Code dots and dashes.
# Unused as it's far more space efficient to use the single chars.
# Though a nice addition to include with the file if people want to compare the symbols.
DIT = "•"
DAH = "—"


class CharToMorseCodeTranslator:
    """
    Translates characters (A-Z, a-z, 0-9) to Morse Code. Used to take a string written in
    normal characters and convert it to a string of the letters in Morse Code.
    """

    """
    CONSTANTS
    """

    # Dictionary for converting characters to their Morse Code equivalent.
    __ALPHA_TO_MORSE_CODE = {
        "A": "• —",
        "B": "— • • •",
        "C": "— • — •",
        "D": "— • •",
        "E": "•",
        "F": "• • — •",
        "G": "— — •",
        "H": "• • • •",
        "I": "• •",
        "J": "• — — —",
        "K": "— • —",
        "L": "• — • •",
        "M": "— —",
        "N": "— •",
        "O": "— — —",
        "P": "• — — •",
        "Q": "— — • —",
        "R": "• — •",
        "S": "• • •",
        "T": "—",
        "U": "• • —",
        "V": "• • • —",
        "W": "• — —",
        "X": "— • • —",
        "Y": "— • — —",
        "Z": "— — • •",
        "1": "• — — — —",
        "2": "• • — — —",
        "3": "• • • — —",
        "4": "• • • • —",
        "5": "• • • • •",
        "6": "— • • • •",
        "7": "— — • • •",
        "8": "— — — • •",
        "9": "— — — — •",
        "0": "— — — — —",

    }
    __LETTER_SPACE = " " * 3  # Spacing between characters in Morse Code
    __WORD_SPACE = " " * 7  # Spacing between words in Morse Code

    """
    PUBLIC METHODS
    """

    def translate(self, str_to_trans: str):
        """
        Translates a given string into Morse Code
        :param str_to_trans: The string to be translated.
        :return: The string in Morse Code.
        """
        # Cast to upper for conversion and remove symbols
        str_no_symbols = self.__remove_symbols(str_to_trans.upper())

        words = str_no_symbols.split()  # Separate words
        morse_code_strs = []  # Holds words translated into Morse Code

        for word in words:
            # Append word in Morse Code
            morse_code_strs.append(self.__word_to_morse_code(word))

        # Join all words by proper Morse Code word spacing
        return self.__WORD_SPACE.join(morse_code_strs)

    """
    PRIVATE METHODS
    """

    def __word_to_morse_code(self, word):
        """
        Converts a string with no spaces to Morse Code
        :param word: The string to convert
        :return: The string in Morse Code
        """
        word_morse_code = ""

        # Append first letter
        word_morse_code += self.__ALPHA_TO_MORSE_CODE[word[0]]

        # Append following letters with proper spacing
        for letter in word[1:]:
            word_morse_code += self.__LETTER_SPACE
            word_morse_code += self.__ALPHA_TO_MORSE_CODE[letter]

        return word_morse_code

    def __remove_symbols(self, str_with_sym: str):
        """
        Removes any characters that are not found in the ALPHA_TO_MORSE dictionary
        :param str_with_sym: Original string, possibly contains symbols
        :return: The string stripped of any symbols
        """
        str_no_sym = str_with_sym

        for char in str_with_sym:
            if (char not in self.__ALPHA_TO_MORSE_CODE.keys()) and (not char == " "):
                str_no_sym = str_no_sym.replace(char, "")

        return str_no_sym
