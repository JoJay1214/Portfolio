"""
TODO List App
file:   list_item.py
author: Joshua Jacobs
date:   descrip
brief:  descrip

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
# put here


class frame(tk.Frame):
    """
    descrip
    """

    """
    CONSTANTS
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        descrip
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG SELF
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        # put here

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

    def __create_widgets(self):
        pass

    def __config_commands(self):
        pass

    def __place_widgets(self):
        pass
