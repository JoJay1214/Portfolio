"""
TODO List App
file:   list_item.py
author: Joshua Jacobs
date:   7/21/2022
brief:  An item meant to be stored in a to-do list. Includes a title, description, and deadline. Inherits from
        three_col_widget

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.three_col_widgets.three_col_widget import ThreeColWidget


class ListItem(ThreeColWidget):
    """
    An item meant to be stored in a to-do list. Includes a title, description, and deadline.
    Inherits from three_col_widget
    """

    """
    CONSTANTS
    """

    __FONT = ("Arial", 16, "normal")
    __HEADER_BOARDER_COLOR = "#AAAAAA"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, title: str, description: str, deadline: str, *args, **kwargs):
        """
        An item meant to be stored in a to-do list. Includes a title, description, and deadline.
        Inherits from three_col_widget
        :param parent: The parent container
        :param title: Title of the to-do task
        :param description: Description of the to-do task
        :param deadline: Deadline of the to-do task
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT PARENT
        super().__init__(parent, *args, **kwargs)

        # CONFIG TK FRAME
        self.config(
            highlightbackground=self.__HEADER_BOARDER_COLOR,
        )

        # CONFIG SELF
        self.__create_widgets(title, description, deadline)
        self.__place_widgets()

    def __create_widgets(self, title: str, description: str, deadline: str):

        # TITLE
        self.title = tk.Label(
            self,
            text=title,
            width=self.TITLE_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

        # DESCRIPTION
        self.description = tk.Label(
            self,
            text=description,
            width=self.DESCRIPTION_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

        # DEADLINE
        self.deadline = tk.Label(
            self,
            text=deadline,
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
