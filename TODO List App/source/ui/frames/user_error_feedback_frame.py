"""
TODO List App
file:   user_error_feedback_frame.py
author: Joshua Jacobs
date:   8/8/2022
brief:  A TK Frame used to display feedback for the user when they cause an error of any sort

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class UserErrorFeedbackFrame(tk.Frame):
    """
    A TK Frame used to display feedback for the user when they cause an error of any sort
    """

    """
    CONSTANTS
    """

    __FONT = ("Arial", 16, "italic")  # font used for error display text
    __FONT_COLOR = "#FF0000"          # color of error text font
    __FRAME_BG_COL = "#BBBBBB"        # background color
    __PAD = 5                         # widget outer padding

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        A TK Frame used to display feedback for the user when they cause an error of any sort
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.config(
            bg=self.__FRAME_BG_COL,
        )

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__error_text_label = None  # label that displays error text

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_error_text(self, text: str):
        """
        Set the error text to display to the user
        :param text: The text to display
        """

        self.__error_text_label.config(
            text=text,
        )

    def clear_error_text(self):
        """
        Clear the error text so it is no longer displayed
        """

        self.__error_text_label.config(
            text="",
        )

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        self.__error_text_label = tk.Label(
            self,
            bg=self.__FRAME_BG_COL,
            fg=self.__FONT_COLOR,
            font=self.__FONT,
            anchor="w",
        )

    def __place_widgets(self):

        self.__error_text_label.grid(
            column=0,
            row=0,
            sticky="NESW",
            padx=self.__PAD,
            pady=self.__PAD,
        )
