"""
TODO List App
file:   list_frame.py
author: Joshua Jacobs
date:   7/21/2022
brief:  The TK Frame that is used to display the list of to-do items

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk
from typing import Callable

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

        self.__current_input_item = None

        self.__item_count = 0

        # CONFIG SELF
        self.__create_widgets()

        self.__setup_scrollable_frame()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def input_item_is_active(self) -> bool:
        """
        Check to see if there is an active input item
        :return: The current input item
        """

        return self.__current_input_item

    def create_new_input_item(self, cmd: Callable):
        """
        Add a new input item to the end of the list
        :param cmd: The function to be called upon input item event
        """

        if not self.__current_input_item:
            self.__current_input_item = ListInputItem(
                self.__scrollable_frame
            )

            self.__current_input_item.set_return_command(cmd=cmd)

            self.__current_input_item.grid(
                column=0,
                row=self.__item_count,
                sticky="EW",
            )

    def destroy_current_input_item(self):
        """
        If there is currently an Input Item in the List Frame, destroy it
        """

        if self.__current_input_item:
            self.__current_input_item.grid_forget()
            self.__current_input_item.destroy()
            self.__current_input_item = None

    def get_inputted_text(self) -> tuple:
        """
        Get the inputted texts from the list input item
        :return: The inputted text strings
        """

        return self.__current_input_item.get_inputted_text()

    def create_new_list_item(self, title: str, description: str, deadline: str) -> ListItem:
        """
        Add a new List Item to the end of the list
        :param title: The List Item's Title
        :param description: The List Item's Description
        :param deadline: The List Item's Deadline
        :return: The newly created List Item
        """

        new_item = ListItem(
            self.__scrollable_frame,
            title=title,
            description=description,
            deadline=deadline,
        )
        new_item.grid(
            column=0,
            row=self.__item_count,
            sticky="EW"
        )
        self.__item_count += 1

        return new_item

    def edit_list_item(self, item: ListItem, cmd: Callable):
        """
        Edit an existing list item
        :param item: The list item to edit
        :param cmd: The function to bind to the Return Key press when finished editing
        :return:
        """

        if not self.__current_input_item:
            self.__current_input_item = ListInputItem(
                self.__scrollable_frame
            )

            item_texts = item.get_list_item_text()
            self.__current_input_item.title.insert(0, item_texts[0])
            self.__current_input_item.description.insert(0, item_texts[1])
            self.__current_input_item.deadline.insert(0, item_texts[2])

            self.__current_input_item.set_return_command(cmd=cmd)

            self.__current_input_item.grid(
                column=0,
                row=item.grid_info()["row"],
            )

    def scroll_to_list_end(self):
        """
        Scrolls the list scrollbar to the bottom
        """

        self.__list_canvas.yview_moveto(1)

    def clear_list(self):
        """
        Completely empty the list
        """

        items = self.__scrollable_frame.winfo_children()

        for item in items:
            item.grid_forget()
            item.destroy()

        self.__item_count = 0

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
