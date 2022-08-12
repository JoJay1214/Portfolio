"""
TODO List App
file:   add_edit_remove_frame.py
author: Joshua Jacobs
date:   7/23/2022
brief:  TK Frame that holds the buttons for adding, editing, and removing a task from the to-do list

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk
from typing import Callable


class AddEditRemoveFrame(tk.Frame):
    """
    TK Frame that holds the buttons for adding, editing, and removing a task from the to-do list
    """

    """
    CONSTANTS
    """

    __FONT = ("Arial", 18, "bold")  # font used for the buttons' text
    __FRAME_BG_COL = "#BBBBBB"      # background color of the frame
    __PAD = 5                       # padding around buttons

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        TK Frame that holds the buttons for adding, editing, and removing a task from the to-do list
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
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__add_button = None     # button used to add new items to the to-do list
        self.__edit_button = None    # button used for editing items on the to-do list
        self.__remove_button = None  # button used for removing items from the to-do list

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

    def set_edit_btn_cmd(self, cmd: Callable):
        """
        Set the command for the Edit Button
        :param cmd: The function to call when the button is pressed
        """

        self.__edit_button.config(
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

    def set_add_btn_state(self, state: str):
        """
        Set the state of the Add Button, normal or disabled
        :param state: The state to set the button, normal or disabled
        """

        if state in ["normal", "disabled"]:
            self.__add_button.config(state=state)

    def set_edit_btn_state(self, state: str):
        """
        Set the state of the Edit Button, normal or disabled
        :param state: The state to set the button, normal or disabled
        """

        if state in ["normal", "disabled"]:
            self.__edit_button.config(state=state)

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # ADD
        self.__add_button = tk.Button(
            self,
            text="ADD",
            font=self.__FONT,
        )

        # EDIT
        self.__edit_button = tk.Button(
            self,
            text="EDIT",
            font=self.__FONT,
        )

        # REMOVE
        self.__remove_button = tk.Button(
            self,
            text="REMOVE",
            font=self.__FONT,
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

        # EDIT
        self.__edit_button.grid(
            column=1,
            row=0,
            sticky="NESW",
            padx=self.__PAD,
            pady=self.__PAD,
        )

        # REMOVE
        self.__remove_button.grid(
            column=2,
            row=0,
            sticky="NESW",
            padx=self.__PAD,
            pady=self.__PAD,
        )
