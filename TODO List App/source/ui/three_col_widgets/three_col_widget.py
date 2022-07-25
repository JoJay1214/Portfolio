"""
TODO List App
file:   three_col_widget.py
author: Joshua Jacobs
date:   7/24/2022
brief:  TK Frame that acts as a three column widget, containing a column for a Title, Description, and Deadline

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class ThreeColWidget(tk.Frame):
    """
    TK Frame that acts as a three column widget, containing a column for a Title, Description, and Deadline
    """

    """
    CONSTANTS
    """

    TITLE_WIDTH = 15
    DESCRIPTION_WIDTH = 40
    DEADLINE_WIDTH = 15

    DESCRIPTION_PADX = 6

    __HEADER_BOARDER_THICKNESS = 1

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        TK Frame that acts as a three column widget, containing a column for a Title, Description, and Deadline
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.config(
            highlightthickness=self.__HEADER_BOARDER_THICKNESS,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        self.title = None
        self.description = None
        self.deadline = None
