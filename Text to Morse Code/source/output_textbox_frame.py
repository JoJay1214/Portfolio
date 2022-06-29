"""
Text to Morse Code App
file:   output_textbox_frame.py
author: Joshua Jacobs
date:   6/26/2022
brief:  TKinter Frame that holds the widgets used for the Output Textbox of the Text to Morse Code app.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
import source.app_settings as sett


class OutputTextboxFrame(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the Output Textbox of the Text to Morse Code app
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Frame, *args, **kwargs):
        """
        Constructor for the Output Textbox Frame of the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__output_text = None           # textbox to output morse code text
        self.__morse_code_scrollbar = None  # horizontal scrollbar to scroll output textbox

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_output_text(self, text: str):
        """
        Set the text in the Morse Code Output Textbox
        :param text: The text to be displayed in the Output Textbox
        """

        self.__output_text.config(state="normal")
        self.__output_text.delete("1.0", tk.END)  # delete old text in output box
        self.__output_text.insert("1.0", text)    # insert new text into output box
        self.__output_text.config(state="disabled")

    def get_output_text(self):
        """
        Get the text from the Output Textbox
        :return: A string of text from the Output Textbox
        """

        return self.__output_text.get("1.0", tk.END)

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TEXT ENTRY
        self.__output_text = tk.Text(
            self,
            height=sett.OUTPUT_TEXT_HEIGHT,
            font=sett.MORSE_CODE_FONT,
            bg=sett.OUTPUT_TEXT_BG_COLOR,
            fg=sett.OUTPUT_TEXT_FG_COLOR,
            wrap=tk.NONE,
        )

        # SCROLLBAR
        self.__morse_code_scrollbar = tk.Scrollbar(
            self,
            orient="horizontal",
            command=self.__output_text.xview,
        )
        self.__output_text.config(
            xscrollcommand=self.__morse_code_scrollbar.set,
        )

    def __place_widgets(self):

        # TEXT ENTRY
        self.__output_text.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # SCROLLBAR
        self.__morse_code_scrollbar.grid(
            column=0,
            row=1,
            sticky="EW",
        )
