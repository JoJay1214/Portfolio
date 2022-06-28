"""
Text to Morse Code App
file:   main.py
author: Joshua Jacobs
date:   6/23/2022
brief:  TKinter app that lets a user enter text into a text box and outputs to the user
        their text translated into Morse Code. As well, can audibly play the message in
        Morse Code.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.text_to_morse_code_application import TextToMorseCodeApplication

import source.app_settings as sett


def main():
    """
    TKinter app that lets a user enter text into a text box and outputs to the user their text translated into
    Morse Code. As well, can audibly play the message in Morse Code
    """

    # root window
    root = tk.Tk()
    __config_root_window(root)

    # text to morse code app
    text_to_morse_code = TextToMorseCodeApplication(
        root,
        bg=sett.WINDOW_BG_COLOR,
    )
    text_to_morse_code.grid(
        column=0,
        row=0,
        sticky="NESW",
    )

    root.mainloop()


def __config_root_window(root: tk.Tk):
    root.title("Text to Morse Code")
    root.config(
        bg=sett.WINDOW_BG_COLOR,
        padx=sett.WINDOW_PADX,
        pady=sett.WINDOW_PADY,
    )
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    # root.geometry()


if __name__ == "__main__":
    main()
