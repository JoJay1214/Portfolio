"""
Text to Morse Code App
file:   text_to_morse_code_application.py
author: Joshua Jacobs
date:   6/23/2022
brief:  Main TKinter GUI for Text to Morse Code App.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.title_frame import TitleFrame


class TextToMorseCodeApplication(tk.Frame):
    """
    Main TKinter GUI for Text to Morse Code App
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        Constructor for the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__title_frame = TitleFrame(
            self,
        )
        self.__title_frame.grid(
            column=0,
            row=0,
        )