"""
TODO List App
file:   list_frame.py
author: Joshua Jacobs
date:   7/21/2022
brief:  The TK Frame that is used to display the list of to-do items

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.three_col_widgets.list_item import ListItem
from source.ui.three_col_widgets.list_input_item import ListInputItem


class ListFrame(tk.Frame):
    """
    The TK Frame that is used to display the list of to-do items
    """

    """
    CONSTANTS
    """

    __CANVAS_HEIGHT = 250

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        The TK Frame that is used to display the list of to-do items
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__list_canvas = None
        self.__scrollbar = None
        self.__scrollable_frame = None

        self.__item_count = 0

        # CONFIG SELF
        self.__create_widgets()
        self.__setup_scrollable_frame()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def create_new_input_item(self):
        """
        Add a new input item to the end of the list
        """

        ListInputItem(self.__scrollable_frame).grid(column=0, row=self.__item_count, sticky="EW",)

    def scroll_to_list_end(self):
        """
        Scrolls the list scrollbar to the bottom
        """

        self.__list_canvas.yview_moveto(1)

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # LIST CANVAS
        self.__list_canvas = tk.Canvas(
            self,
            height=self.__CANVAS_HEIGHT
        )

        # SCROLLBAR
        self.__scrollbar = tk.Scrollbar(
            self,
            command=self.__list_canvas.yview,
        )
        self.__list_canvas.config(
            yscrollcommand=self.__scrollbar.set,
        )

        # SCROLLABLE FRAME
        self.__scrollable_frame = tk.Frame(
            self.__list_canvas,
        )

    def __setup_scrollable_frame(self):

        # <Configure> triggers whenever the scrollable frame changes size (i.e. when items are added/removed from it)
        # canvas.bbox gives canvas position to define scroll region
        self.__scrollable_frame.bind(
            "<Configure>",
            lambda event: self.__list_canvas.configure(
                scrollregion=self.__list_canvas.bbox("all")
            )
        )

        # place scrollable frame on canvas
        self.__list_canvas.create_window((0, 0), window=self.__scrollable_frame, anchor="nw")

    def __place_widgets(self):

        # LIST CANVAS
        self.__list_canvas.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # SCROLLBAR
        self.__scrollbar.grid(
            column=0,
            row=0,
            sticky="NES",
        )

        for i in range(12):
            ListItem(self.__scrollable_frame, title=f"meowwwwwwwwwwwwwwwwwwwwwwwwwww{i}", description=f"{i}nyaa", deadline="soon").grid(column=0, row=i, sticky="EW")
            self.__item_count += 1
