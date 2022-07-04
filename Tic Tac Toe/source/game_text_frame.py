"""
Tic Tac Toe
file:   game_text_frame.py
author: Joshua Jacobs
date:   7/3/2022
brief:  TKinter Frame that holds the widgets used for the Game Text of the Tic Tac Toe app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk


class GameTextFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Game Text of the Tic Tac Toe app
    """

    """
    CONSTANTS
    """

    __GAME_TEXT_FONT = ("Arial", 40, "bold")

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Title Frame
        :param parent: The parent frame
        :param args: Argument list
        :param kwargs: Keyword Argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent     # the parent frame

        # PRIVATE VARIABLES
        self.__game_text = None  # text showing player turn and end game result

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_game_text(self, text: str):
        """
        Set the Game Text string
        :param text: Text to fill Game Text
        """

        self.__game_text.config(
            text=text,
        )

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        self.__game_text = tk.Label(
            self,
            font=self.__GAME_TEXT_FONT,
        )

    def __place_widgets(self):

        self.__game_text.grid(
            column=0,
            row=0,
            sticky="NESW",
        )
