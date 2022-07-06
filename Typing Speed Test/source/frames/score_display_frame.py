"""
Typing Speed Test
file:   .py
author: Joshua Jacobs
date:   7//2022
brief:  TKinter Frame that holds the widgets used for the _____ of the Typing Speed Test app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class Frame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the _____ of the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the _____ Frame
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
        # put here

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):
        pass

    def __place_widgets(self):
        pass
