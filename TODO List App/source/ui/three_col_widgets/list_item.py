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
from typing import Callable

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

    __FONT = ("Arial", 16, "normal")    # text label font

    __BORDER_COLOR = "#AAAAAA"          # color of the border around the frame
    __BG_COLOR = "#FFFFFF"              # color of the item background when not selected
    __TEXT_COLOR = "#000000"            # color of item text when not selected
    __HIGHLIGHT_BG_COLOR = "#0505FF"    # color of item background when selected
    __HIGHLIGHT_TEXT_COLOR = "#FFFFFF"  # color of item text when selected

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
            highlightbackground=self.__BORDER_COLOR,
        )

        # CONFIG SELF
        self.__create_widgets(title, description, deadline)
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def bind_on_click_command(self, cmd: Callable):
        """
        Bind method to trigger when List Item is clicked
        :param cmd: The method to trigger when Item is clicked on
        """

        self.bind("<Button-1>", cmd)
        self.title.bind("<Button-1>", cmd)
        self.description.bind("<Button-1>", cmd)
        self.deadline.bind("<Button-1>", cmd)

    def select_list_item(self):
        """
        Highlight this List Item, changing its appearance
        """

        self.config(
            bg=self.__HIGHLIGHT_BG_COLOR,
        )

        self.title.config(
            bg=self.__HIGHLIGHT_BG_COLOR,
            fg=self.__HIGHLIGHT_TEXT_COLOR,
        )
        self.description.config(
            bg=self.__HIGHLIGHT_BG_COLOR,
            fg=self.__HIGHLIGHT_TEXT_COLOR,
        )
        self.deadline.config(
            bg=self.__HIGHLIGHT_BG_COLOR,
            fg=self.__HIGHLIGHT_TEXT_COLOR,
        )

    def deselect_list_item(self):
        """
        Un-highlight this List Item, changing its appearance
        """

        self.config(
            bg=self.__BG_COLOR,
        )

        self.title.config(
            bg=self.__BG_COLOR,
            fg=self.__TEXT_COLOR,
        )
        self.description.config(
            bg=self.__BG_COLOR,
            fg=self.__TEXT_COLOR,
        )
        self.deadline.config(
            bg=self.__BG_COLOR,
            fg=self.__TEXT_COLOR,
        )

    def get_list_item_text(self) -> tuple:
        """
        Get the text stored in the List Item
        :return: The three text sections from the List Item
        """

        return self.title.cget("text"), self.description.cget("text"), self.deadline.cget("text")

    def set_list_item_text(self, title: str, description: str, deadline: str):
        """
        Set the text in each label
        :param title: Title text string
        :param description: Description text string
        :param deadline: Deadline text string
        """

        self.title.config(text=title)
        self.description.config(text=description)
        self.deadline.config(text=deadline)

    def get_list_item_row(self):
        """
        Get the widget's row placement from the grid it is in
        :return: The widget's row number
        """

        return self.grid_info()["row"]

    """
    PRIVATE METHODS
    """

    def __create_widgets(self, title: str, description: str, deadline: str):

        # TITLE
        self.title = tk.Label(
            self,
            text=title,
            anchor="w",
            font=self.__FONT,
            width=self.TITLE_WIDTH,
        )

        # DESCRIPTION
        self.description = tk.Label(
            self,
            text=description,
            anchor="w",
            font=self.__FONT,
            width=self.DESCRIPTION_WIDTH,
        )

        # DEADLINE
        self.deadline = tk.Label(
            self,
            text=deadline,
            anchor="w",
            font=self.__FONT,
            width=self.DEADLINE_WIDTH,
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
