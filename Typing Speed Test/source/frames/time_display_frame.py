"""
Typing Speed Test
file:   time_display_frame.py
author: Joshua Jacobs
date:   7/10/2022
brief:  TKinter Frame that holds the widgets used for the Time Display Frame of the Typing Speed Test app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class TimeDisplayFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Time Display Frame of the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    __WIDGET_PADY = 5
    __TIME_START_TEXT = "00"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Time Display Frame
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
        self.parent = parent    # the parent frame
        self.time_label = None  # current time left in the test

        # PRIVATE VARIABLES
        self.__time_title_label = None  # title of the frame

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__time_title_label = tk.Label(
            self,
            text="Time",
            pady=self.__WIDGET_PADY,
        )

        # TIME
        self.time_label = tk.Label(
            self,
            text=self.__TIME_START_TEXT,
            pady=self.__WIDGET_PADY,
        )

    def __place_widgets(self):

        # TITLE
        self.__time_title_label.grid(
            column=0,
            row=0,
        )

        # TIME
        self.time_label.grid(
            column=0,
            row=1,
        )
