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
from typing import Callable

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

    __FONT = ("Arial", 16, "normal")  # font of the text in the Entry widgets
    __BORDER_COLOR = "#AAAAAA"        # color of the border of the frame

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
            highlightbackground=self.__BORDER_COLOR,
        )

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

        self.title.focus()

    """
    PUBLIC METHODS
    """

    def set_return_command(self, cmd: Callable):
        """
        Bind a method to the Entry boxes when Return is pressed
        :param cmd: The function to call
        """

        self.title.bind(
            "<Return>",
            cmd,
        )
        self.description.bind(
            "<Return>",
            cmd,
        )
        self.deadline.bind(
            "<Return>",
            cmd,
        )

    def get_inputted_text(self) -> tuple:
        """
        Get the strings inputted into the list input items' entries
        :return: The strings inputted for title, description, and deadline--stripped
        of any spaces at the beginnings and ends
        """

        return self.title.get().strip(), self.description.get().strip(), self.deadline.get().strip()

    """
    PRIVATE METHODS
    """

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
