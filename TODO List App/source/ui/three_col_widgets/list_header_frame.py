"""
TODO List App
file:   list_header_frame.py
author: Joshua Jacobs
date:   7/21/2022
brief:  three_col_widget that holds the header used with the to-do list

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.three_col_widgets.three_col_widget import ThreeColWidget


class ListHeaderFrame(ThreeColWidget):
    """
    three_col_widget that holds the header used with the to-do list
    """

    """
    CONSTANTS
    """

    __FONT = ("Arial", 15, "bold")
    __FRAME_BG_COLOR = "#000000"
    __BOARDER_COLOR = "#555555"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        three_col_widget that holds the header used with the to-do list
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT PARENT
        super().__init__(parent, *args, **kwargs)

        # CONFIG TK FRAME
        self.config(
            bg=self.__FRAME_BG_COLOR,
            highlightbackground=self.__BOARDER_COLOR,
        )

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    def __create_widgets(self):

        # TITLE
        self.title = tk.Label(
            self,
            text="TITLE",
            width=self.TITLE_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

        # DESCRIPTION
        self.description = tk.Label(
            self,
            text="DESCRIPTION",
            width=self.DESCRIPTION_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

        # DEADLINE
        self.deadline = tk.Label(
            self,
            text="DEADLINE",
            width=self.DEADLINE_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

    def __place_widgets(self):

        # TITLE
        self.title.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # DESCRIPTION
        self.description.grid(
            column=1,
            row=0,
            sticky="NESW",
            padx=self.DESCRIPTION_PADX,
        )

        # DEADLINE
        self.deadline.grid(
            column=2,
            row=0,
            sticky="NESW",
        )
