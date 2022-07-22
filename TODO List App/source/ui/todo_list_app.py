"""
TODO List App
file:   todo_list_app.py
author: Joshua Jacobs
date:   7/21/2022
brief:  An application built using TKinter that acts as a to-do list viewer/manager

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.frames.list_header_frame import ListHeaderFrame
from source.ui.list_item import ListItem
from source.ui.frames.list_frame import ListFrame


class TODOListApp(tk.Frame):
    """
    An application built using TKinter that acts as a to-do list viewer/manager
    """

    """
    CONSTANTS
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        An application built using TKinter that acts as a to-do list viewer/manager
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
        self.__list_header = None
        self.__list_frame = None

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

    def __create_widgets(self):

        # HEADER
        self.__list_header = ListHeaderFrame(
            self,
            title="TITLE",
            description="DESCRIPTION",
            deadline="DEADLINE",
        )

        # LIST
        self.__list_frame = ListFrame(
            self,
        )

    def __config_commands(self):
        pass

    def __place_widgets(self):

        # HEADER
        self.__list_header.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # LIST
        self.__list_frame.grid(
            column=0,
            row=1,
            sticky="NESW",
        )
