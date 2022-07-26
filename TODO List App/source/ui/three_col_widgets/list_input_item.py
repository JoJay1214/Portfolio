"""
TODO List App
file:   list_input_item.py
author: Joshua Jacobs
date:   7/25/2022
brief:  A TK Frame with three input widgets, used for entering new items into the to-do list.
        Inherits from three_col_widget

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.three_col_widgets.three_col_widget import ThreeColWidget


class ListInputItem(ThreeColWidget):
    """
    A TK Frame with three input widgets, used for entering new items into the to-do list.
    Inherits from three_col_widget
    """

    """
    CONSTANTS
    """

    __FONT = ("Arial", 16, "normal")
    __BOARDER_COLOR = "#AAAAAA"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        A TK Frame with three input widgets, used for entering new items into the to-do list.
        Inherits from three_col_widget
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT PARENT
        super().__init__(parent, *args, **kwargs)

        # CONFIG TK FRAME
        self.config(
            highlightbackground=self.__BOARDER_COLOR,
        )

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

        self.title.focus()

    def __create_widgets(self):

        # TITLE
        self.title = tk.Entry(
            self,
            width=self.TITLE_WIDTH,
            font=self.__FONT,
        )

        # DESCRIPTION
        self.description = tk.Entry(
            self,
            width=self.DESCRIPTION_WIDTH,
            font=self.__FONT,
        )

        # DEADLINE
        self.deadline = tk.Entry(
            self,
            width=self.DEADLINE_WIDTH,
            font=self.__FONT,
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
