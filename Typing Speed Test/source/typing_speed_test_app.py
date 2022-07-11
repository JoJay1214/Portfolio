"""
Typing Speed Test
file:   typing_speed_test_app.py
author: Joshua Jacobs
date:   7/5/2022
brief:  Main TKinter GUI for the Typing Speed Test app.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.frames.title_frame import TitleFrame
from source.frames.start_button_frame import StartButtonFrame
from source.frames.score_display_frame import ScoreDisplayFrame
from source.frames.time_display_frame import TimeDisplayFrame
from source.frames.typing_test_frame import TypingTestFrame

from typing_speed_test import TypingSpeedTest


class TypingSpeedTestApp(tk.Frame):
    """
    Main TKinter GUI for the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    # put those here

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        Constructor for the Frame that holds the Typing Speed Test app
        :param parent: The parent window
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent window

        # PRIVATE VARIABLES
        self.__title_frame = None          # the app's title
        self.__start_button_frame = None   # start button to start/stop the test
        self.__score_display_frame = None  # displays the current score in the typing test
        self.__time_display_frame = None   # displays the current time left in the typing test
        self.__typing_test_frame = None    # displays current word and has entry for user interaction

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__title_frame = TitleFrame(
            self,
        )

        # START BUTTON
        self.__start_button_frame = StartButtonFrame(
            self,
        )

        # SCORE DISPLAY
        self.__score_display_frame = ScoreDisplayFrame(
            self,
        )

        # TIME DISPLAY
        self.__time_display_frame = TimeDisplayFrame(
            self,
        )

        # TYPING TEST
        self.__typing_test_frame = TypingTestFrame(
            self,
        )

    def __config_commands(self):
        pass

    def __place_widgets(self):

        # TITLE
        self.__title_frame.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="NESW",
        )

        # START BUTTON
        self.__start_button_frame.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="NESW",
        )

        # SCORE DISPLAY
        self.__score_display_frame.grid(
            column=0,
            row=2,
            sticky="NESW",
        )

        # TIME DISPLAY
        self.__time_display_frame.grid(
            column=1,
            row=2,
            sticky="NESW",
        )

        # TYPING TEST
        self.__typing_test_frame.grid(
            column= 0,
            row=3,
            columnspan=2,
            sticky="NESW",
        )
