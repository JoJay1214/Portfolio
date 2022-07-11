"""
Typing Speed Test
file:   typing_test_frame.py
author: Joshua Jacobs
date:   7/10/2022
brief:  TKinter Frame that holds the widgets used for the Typing Test section of the Typing Speed Test app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


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
        self.word_label = None    # displays the current word in the test
        self.typing_entry = None  # entry for user input and typing out words

        # PRIVATE VARIABLES
        self.__hint_label = None  # displays a hint about what the user should do to interact

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # WORD TO TYPE
        self.word_label = tk.Label(
            self,
            text="word",
            pady=self.__WORD_PADY,
        )

        # INPUT ENTRY
        self.typing_entry = tk.Entry(
            self,
            justify="center",
        )
        # self.__typing_entry.bind(
        #     "<Return>",
        #     self.__input_typed_entry,
        # )

        # HINT LABEL
        self.__hint_label = tk.Label(
            self,
            text=self.__HINT_START_TEXT,
            pady=self.__HINT_PADY,
        )

    def __place_widgets(self):

        # WORD TO TYPE
        self.word_label.grid(
            column=0,
            row=0,
        )

        # INPUT ENTRY
        self.typing_entry.grid(
            column=0,
            row=1,
        )

        # HINT LABEL
        self.__hint_label.grid(
            column=0,
            row=2,
        )
