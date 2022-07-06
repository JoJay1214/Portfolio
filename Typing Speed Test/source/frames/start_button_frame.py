"""
Typing Speed Test
file:   start_button_frame.py
author: Joshua Jacobs
date:   7/5/2022
brief:  TKinter Frame that holds the widgets used for the Start Button for the Typing Speed Test app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class StartButtonFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Start Button for the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Start Button Frame
        :param parent: The parent frame
        :param args: Argument list
        :param kwargs: Keyword Argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent frame

        # PRIVATE VARIABLES
        self.__start_button = None  # button that starts the typing speed test

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        self.__start_button = tk.Button(
            self,
            text="Start Typing",
            # command=self.__start_test,
        )

    def __place_widgets(self):

        self.__start_button.grid(
            column=0,
            row=0,
            sticky="NESW",
        )
