"""
Text to Morse Code App
file:   output_textbox_frame.py
author: Joshua Jacobs
date:   6/26/2022
brief:  TKinter Frame that holds the widgets used for the Output Textbox of the Text to Morse Code app.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
import source.app_settings as sett


class OutputTextboxFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Output Textbox of the Text to Morse Code app
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Output Textbox Frame of the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent                # the parent container

        self.morse_code_output_text = None  # textbox to output morse code text

        # PRIVATE VARIABLES
        self.__morse_code_scrollbar = None  # horizontal scrollbar to scroll output textbox

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TEXT ENTRY
        self.morse_code_output_text = tk.Text(
            self,
            height=sett.OUTPUT_TEXT_HEIGHT,
            font=sett.MORSE_CODE_FONT,
            bg=sett.OUTPUT_TEXT_BG_COLOR,
            fg=sett.OUTPUT_TEXT_FG_COLOR,
            wrap=tk.NONE,
        )

        # SCROLLBAR
        self.__morse_code_scrollbar = tk.Scrollbar(
            self,
            orient="horizontal",
            command=self.morse_code_output_text.xview,
        )
        self.morse_code_output_text.config(
            xscrollcommand=self.__morse_code_scrollbar.set,
        )

    def __place_widgets(self):

        # TEXT ENTRY
        self.morse_code_output_text.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # SCROLLBAR
        self.__morse_code_scrollbar.grid(
            column=0,
            row=1,
            sticky="EW",
        )
