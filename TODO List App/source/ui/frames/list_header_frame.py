"""
TODO List App
file:   list_header_frame.py
author: Joshua Jacobs
date:   7/21/2022
brief:  TK Frame that holds the header used with the to-do list

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.list_item import ListItem


class ListHeaderFrame(ListItem):
    """
    List Item that holds the header used with the to-do list
    """

    """
    CONSTANTS
    """

    __FONT = "bold"

    __HEADER_BOARDER_THICKNESS = 1
    __HEADER_BOARDER_COLOR = "#000000"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, title: str, description: str, deadline: str, *args, **kwargs):
        """
        List Item that holds the header used with the to-do list
        :param parent: The parent container
        :param title: Title of the to-do task
        :param description: Description of the to-do task
        :param deadline: Deadline of the to-do task
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG LIST ITEM
        super().__init__(parent, title, description, deadline, *args, **kwargs)

        self.title_label.config(
            highlightthickness=self.__HEADER_BOARDER_THICKNESS,
            highlightbackground=self.__HEADER_BOARDER_COLOR,
            font=self.__FONT,
        )

        self.description_label.config(
            highlightthickness=self.__HEADER_BOARDER_THICKNESS,
            highlightbackground=self.__HEADER_BOARDER_COLOR,
            font=self.__FONT,
        )

        self.deadline_label.config(
            highlightthickness=self.__HEADER_BOARDER_THICKNESS,
            highlightbackground=self.__HEADER_BOARDER_COLOR,
            font=self.__FONT,
        )
