"""
Tic Tac Toe
file:   button_board_frame.py
author: Joshua Jacobs
date:   7/3/2022
brief:  TKinter Frame that holds the widgets used for the Button Board of the Tic Tac Toe app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class ButtonBoardFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Button Board of the Tic Tac Toe app
    """

    """
    CONSTANTS
    """

    __BUTTON_FONT = ("Arial", 40, "bold")
    __BUTTON_PAD = 5

    __FRAME_BG_COLOR = "#000000"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Button Board Frame
        :param parent: The parent frame
        :param args: Argument list
        :param kwargs: Keyword Argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.config(
            bg=self.__FRAME_BG_COLOR,
        )

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent      # the parent frame
        self.button_board = None  # the clickable buttons where game markers are placed

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # empty list of lists for the board buttons
        self.button_board = [
            [],
            [],
            []
        ]

        # create each button and append them properly to the list of lists
        for row in range(3):
            for col in range(3):

                button = tk.Button(
                    self,
                    text=" ",
                    font=self.__BUTTON_FONT,
                    height=1,
                    width=3,
                )

                self.button_board[row].append(button)

    def __place_widgets(self):

        for row in range(3):
            for col in range(3):
                self.button_board[row][col].grid(
                    column=col,
                    row=row,
                    padx=self.__BUTTON_PAD,
                    pady=self.__BUTTON_PAD,
                )
