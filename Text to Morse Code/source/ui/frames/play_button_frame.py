"""
Text to Morse Code App
file:   play_button_frame.py
author: Joshua Jacobs
date:   6/27/2022
brief:  TKinter Frame that holds the widgets used for the Play Button of the Text to Morse Code app.

"""


# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

from typing import Callable

# PROJECT IMPORTS
import source.app_settings as sett


class PlayButtonFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Play Button of the Text to Morse Code app
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Play Button Frame of the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.play_button = None  # button to play the morse code

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_play_button_command(self, cmd: Callable):
        """
        Set the command of the TK Button
        :param cmd: The function to be called when the button is pressed
        """

        self.play_button.config(command=cmd)

    def set_play_button_text(self, text: str):
        """
        Set the text displayed by the Play Button
        :param text: The text to display
        """

        self.play_button.config(text=text)

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # PLAY BUTTON
        self.play_button = tk.Button(
            self,
            # command=self.__toggle_play_stop,
            font=sett.BUTTON_FONT,
            text="Play",
        )

    def __place_widgets(self):

        # PLAY BUTTON
        self.play_button.grid(
            column=0,
            row=0,
            sticky="NESW",
        )
