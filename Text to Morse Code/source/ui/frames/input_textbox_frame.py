"""
Text to Morse Code App
file:   input_textbox_frame.py
author: Joshua Jacobs
date:   6/24/2022
brief:  TKinter Frame that holds the widgets used for the Input Textbox of the Text to Morse Code app.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
import source.app_settings as sett


class InputTextboxFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Input Textbox of the Text to Morse Code app
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Input Textbox Frame of the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__input_text_entry = None      # text entry for inputting text
        self.__text_entry_scrollbar = None  # scrollbar for when text entry is overflowing to extra lines

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def get_input_text(self):
        """
        Get the text from the Input Textbox
        :return: The string of text from the Input Textbox
        """

        return self.__input_text_entry.get("1.0", tk.END)

    def enable_input_textbox(self):
        """
        Enable the Input Textbox for typing
        """

        self.__input_text_entry.config(state="normal")

    def disable_input_textbox(self):
        """
        Disable the Input Textbox for typing
        """

        self.__input_text_entry.config(state="disabled")

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TEXT ENTRY
        self.__input_text_entry = tk.Text(
            self,
            font=sett.ENTRY_FONT,
            height=sett.INPUT_TEXT_HEIGHT,
            wrap=tk.WORD,
        )
        self.__input_text_entry.insert("1.0", sett.INPUT_STARTING_TEXT)
        self.__input_text_entry.focus()

        # SCROLLBAR
        self.__text_entry_scrollbar = tk.Scrollbar(
            self,
            command=self.__input_text_entry.yview,
        )
        self.__input_text_entry.config(
            yscrollcommand=self.__text_entry_scrollbar.set,
        )

    def __place_widgets(self):

        # TEXT ENTRY
        self.__input_text_entry.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # SCROLLBAR
        self.__text_entry_scrollbar.grid(
            column=1,
            row=0,
            sticky="NS",
        )
