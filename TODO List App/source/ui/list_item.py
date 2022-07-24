"""
TODO List App
file:   list_item.py
author: Joshua Jacobs
date:   7/21/2022
brief:  An item meant to be stored in a to-do list. Includes a title, description, and deadline

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class ListItem(tk.Frame):
    """
    An item meant to be stored in a to-do list. Includes a title, description, and deadline
    """

    """
    CONSTANTS
    """

    __TITLE_WIDTH = 15
    __DESCRIPTION_WIDTH = 40
    __DEADLINE_WIDTH = 15

    __FONT = ("Arial", 16, "normal")

    __HEADER_BOARDER_THICKNESS = 1
    __HEADER_BOARDER_COLOR = "#AAAAAA"

    __PADX = 6

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, title: str, description: str, deadline: str, *args, **kwargs):
        """
        An item meant to be stored in a to-do list. Includes a title, description, and deadline
        :param parent: The parent container
        :param title: Title of the to-do task
        :param description: Description of the to-do task
        :param deadline: Deadline of the to-do task
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.config(
            highlightthickness=self.__HEADER_BOARDER_THICKNESS,
            highlightbackground=self.__HEADER_BOARDER_COLOR,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.title_label = None
        self.description_label = None
        self.deadline_label = None

        # CONFIG SELF
        self.__create_widgets(title, description, deadline)
        self.__place_widgets()

    def __create_widgets(self, title: str, description: str, deadline: str):

        # TITLE
        self.title_label = tk.Label(
            self,
            text=title,
            width=self.__TITLE_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

        # DESCRIPTION
        self.description_label = tk.Label(
            self,
            text=description,
            width=self.__DESCRIPTION_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

        # DEADLINE
        self.deadline_label = tk.Label(
            self,
            text=deadline,
            width=self.__DEADLINE_WIDTH,
            font=self.__FONT,
            anchor="w",
        )

    def __place_widgets(self):

        # TITLE
        self.title_label.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # DESCRIPTION
        self.description_label.grid(
            column=1,
            row=0,
            sticky="NESW",
            padx=self.__PADX,
        )

        # DEADLINE
        self.deadline_label.grid(
            column=2,
            row=0,
            sticky="NESW",
        )
