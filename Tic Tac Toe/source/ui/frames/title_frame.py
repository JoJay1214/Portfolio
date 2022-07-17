"""
Tic Tac Toe
file:   title_frame.py
author: Joshua Jacobs
date:   7/3/2022
brief:  TKinter Frame that holds the widgets used for the Title of the Tic Tac Toe app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class TitleFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Title of the Tic Tac Toe app
    """

    """
    CONSTANTS
    """

    __TITLE_FONT = ("Arial", 64, "bold")

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Title Frame
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
        self.__title_label = None  # the title text for the app

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        self.__title_label = tk.Label(
            self,
            text="Tic Tac Toe",
            font=self.__TITLE_FONT,
        )

    def __place_widgets(self):
        self.__title_label.grid(
            column=0,
            row=0,
            sticky="NESW",
        )
