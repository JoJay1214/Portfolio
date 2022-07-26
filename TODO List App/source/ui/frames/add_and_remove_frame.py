"""
TODO List App
file:   add_and_remove_frame.py
author: Joshua Jacobs
date:   7/23/2022
brief:  TK Frame that holds the buttons for adding and removing a task from the to-do list

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk
from typing import Callable


class AddAndRemoveFrame(tk.Frame):
    """
    TK Frame that holds the buttons for adding and removing a task from the to-do list
    """

    """
    CONSTANTS
    """

    __FONT = ("Arial", 18, "bold")
    __FRAME_BG_COL = "#BBBBBB"
    __PAD = 5
    __WIDTH = 3

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        TK Frame that holds the buttons for adding and removing a task from the to-do list
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.config(
            bg=self.__FRAME_BG_COL,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__add_button = None
        self.__remove_button = None

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_add_btn_cmd(self, cmd: Callable):
        """
        Set the command for the Add Button
        :param cmd: The function to call when the button is pressed
        """

        self.__add_button.config(
            command=cmd,
        )

    def set_remove_btn_cmd(self, cmd: Callable):
        """
        Set the command for the Remove Button
        :param cmd: The function to call when the button is pressed
        """

        self.__remove_button.config(
            command=cmd,
        )

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # ADD
        self.__add_button = tk.Button(
            self,
            text="+",
            font=self.__FONT,
            width=self.__WIDTH,
        )

        # REMOVE
        self.__remove_button = tk.Button(
            self,
            text="-",
            font=self.__FONT,
            width=self.__WIDTH,
        )

    def __place_widgets(self):

        # ADD
        self.__add_button.grid(
            column=0,
            row=0,
            sticky="NESW",
            padx=self.__PAD,
            pady=self.__PAD,
        )

        # REMOVE
        self.__remove_button.grid(
            column=1,
            row=0,
            sticky="NESW",
            padx=self.__PAD,
            pady=self.__PAD,
        )
