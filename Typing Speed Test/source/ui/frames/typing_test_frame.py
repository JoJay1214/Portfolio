"""
Typing Speed Test
file:   typing_test_frame.py
author: Joshua Jacobs
date:   7/10/2022
brief:  TKinter Frame that holds the widgets used for the Typing Test section of the Typing Speed Test app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

from typing import Callable


class TypingTestFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Typing Test section of the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    __WORD_PADY = 5
    __HINT_PADY = 10

    __HINT_START_TEXT = "Hit Enter Key to Submit each Word"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Typing Test Frame
        :param parent: The parent frame
        :param args: Argument list
        :param kwargs: Keyword Argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent      # the parent frame

        # PRIVATE VARIABLES
        self.__word_label = None    # displays the current word in the test
        self.__typing_entry = None  # entry for user input and typing out words
        self.__hint_label = None    # displays a hint about what the user should do to interact

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_word_label(self, text: str):
        """
        Set the text in the Word Label
        :param text: The text to be displayed by the label
        """

        self.__word_label.config(text=text)

    def bind_text_entry(self, event: str, handler: Callable):
        """
        Bind a function for the Text Entry to a given Event
        :param event: The Event that will trigger the function
        :param handler: The function to be bound
        """

        self.__typing_entry.bind(
            event,
            handler,
        )

    def get_text_entry(self) -> str:
        """
        Get the text from the Text Entry
        :return: The string of text in the Text Entry
        """

        return self.__typing_entry.get()

    def focus_text_entry(self):
        """
        Focuses on the Typing Test text Entry
        """

        self.__typing_entry.focus()

    def delete_text_entry(self):
        """
        Deletes the text in the Text Entry
        """

        self.__typing_entry.delete(0, tk.END)

    def set_text_entry_state(self, state: str):
        """
        Set the State of the Text Entry--either "normal" or "disabled"
        """

        if state == "normal" or state == "disabled":
            self.__typing_entry.config(state=state)
        else:
            print("Invalid Text Entry State!")

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # WORD TO TYPE
        self.__word_label = tk.Label(
            self,
            text="word",
            pady=self.__WORD_PADY,
        )

        # INPUT ENTRY
        self.__typing_entry = tk.Entry(
            self,
            justify="center",
            state="disabled",
        )

        # HINT LABEL
        self.__hint_label = tk.Label(
            self,
            text=self.__HINT_START_TEXT,
            pady=self.__HINT_PADY,
        )

    def __place_widgets(self):

        # WORD TO TYPE
        self.__word_label.grid(
            column=0,
            row=0,
        )

        # INPUT ENTRY
        self.__typing_entry.grid(
            column=0,
            row=1,
        )

        # HINT LABEL
        self.__hint_label.grid(
            column=0,
            row=2,
        )
