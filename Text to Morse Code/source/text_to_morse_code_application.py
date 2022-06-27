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
from source.input_textbox_frame import InputTextboxFrame
from source.output_textbox_frame import OutputTextboxFrame


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

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__title_frame = None           # holds the app title section
        self.__input_textbox_frame = None   # holds the input entry textbox section
        self.__output_textbox_frame = None  # holds the output textbox section

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    def __create_widgets(self):

        # TITLE
        self.__title_frame = TitleFrame(
            self,
        )

        # INPUT TEXTBOX
        self.__input_textbox_frame = InputTextboxFrame(
            self,
        )

        # OUTPUT TEXTBOX
        self.__output_textbox_frame = OutputTextboxFrame(
            self,
        )

    def __place_widgets(self):

        # TITLE
        self.__title_frame.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # INPUT TEXTBOX
        self.__input_textbox_frame.grid(
            column=0,
            row=1,
            sticky="NESW",
        )

        # OUTPUT TEXTBOX
        self.__output_textbox_frame.grid(
            column=0,
            row=2,
            sticky="NESW",
        )
