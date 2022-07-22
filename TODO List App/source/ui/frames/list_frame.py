"""
TODO List App
file:   list_frame.py
author: Joshua Jacobs
date:   7/21/2022
brief:  The TK Frame that is used to display the list of to-do items

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class ListFrame(tk.Frame):
    """
    The TK Frame that is used to display the list of to-do items
    """

    """
    CONSTANTS
    """

    __CANVAS_HEIGHT = 100

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

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    def __create_widgets(self):

        # LIST CANVAS
        self.__list_canvas = tk.Canvas(
            self,
            height=self.__CANVAS_HEIGHT,
        )

        # SCROLLBAR
        self.__scrollbar = tk.Scrollbar(
            self,
            command=self.__list_canvas.yview,
        )
        self.__list_canvas.config(
            yscrollcommand=self.__scrollbar.set,
        )

    def __place_widgets(self):

        # LIST CANVAS
        self.__list_canvas.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # SCROLLBAR
        self.__scrollbar.grid(
            column=1,
            row=0,
            sticky="NESW",
        )
