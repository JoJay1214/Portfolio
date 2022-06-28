"""
Text to Morse Code App
file:   title_frame.py
author: Joshua Jacobs
date:   6/23/2022
brief:  TKinter Frame that holds the widgets used for the Title of the Text to Morse Code app.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.char_to_morse_code import CharToMorseCodeTranslator

import source.app_settings as sett


class TitleFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Title of the Text to Morse Code app
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Title Frame of the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__title_label = None     # app title
        self.__title_mc_label = None  # title in morse code

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__title_label = tk.Label(
            self,
            text="Text to Morse Code",
            font=sett.TITLE_FONT,
        )

        # TITLE IN MORSE CODE
        self.__title_mc_label = tk.Label(
            self,
            text=f"{CharToMorseCodeTranslator.translate('Text to')}\n"
                 f"{CharToMorseCodeTranslator.translate('Morse Code')}",
            font=sett.TITLE_MC_FONT,
        )

    def __place_widgets(self):

        # TITLE
        self.__title_label.grid(
            column=0,
            row=0,
            sticky="EW",
        )

        # TITLE IN MORSE CODE
        self.__title_mc_label.grid(
            column=0,
            row=1,
            sticky="EW",
        )
