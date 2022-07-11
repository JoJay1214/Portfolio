"""
Typing Speed Test
file:   score_display_frame.py
author: Joshua Jacobs
date:   7/10/2022
brief:  TKinter Frame that holds the widgets used for the Score Display of the Typing Speed Test app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class ScoreDisplayFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Score Display of the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    __WIDGET_PADY = 5
    __SCORE_START_TEXT = "0/0"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Score Display Frame
        :param parent: The parent frame
        :param args: Argument list
        :param kwargs: Keyword Argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent     # the parent frame
        self.score_label = None  # current score in the test

        # PRIVATE VARIABLES
        self.__score_title_label = None  # score frame title label

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__score_title_label = tk.Label(
            self,
            text="Score",
            pady=self.__WIDGET_PADY,
        )

        # SCORE
        self.score_label = tk.Label(
            self,
            text=self.__SCORE_START_TEXT,
            pady=self.__WIDGET_PADY,
        )

    def __place_widgets(self):

        # TITLE
        self.__score_title_label.grid(
            column=0,
            row=0,
        )

        # SCORE
        self.score_label.grid(
            column=0,
            row=1,
        )
