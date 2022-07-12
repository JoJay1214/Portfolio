"""
Typing Speed Test
file:   main.py
author: Joshua Jacobs
date:   7/5/2022
brief:  A simple Typing Speed Test application that has the user typing out and submitting words as
        quickly as they can to try to better their score.
References:
    word list: https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.typing_speed_test_app import TypingSpeedTestApp

__WIN_START_POS = (350, 50)
__WIN_PAD = 20


def main():
    """
    Creates and configures the Typing Speed Test window and application
    """

    # root window
    root = tk.Tk()
    __config_root_window(root)

    # typing speed test app
    typing_speed_test_app = TypingSpeedTestApp(
        root,
    )
    typing_speed_test_app.grid(
        column=0,
        row=0,
        sticky="NESW",
    )

    root.mainloop()


def __config_root_window(root: tk.Tk):
    root.title("Typing Speed Test")
    root.config(
        padx=__WIN_PAD,
        pady=__WIN_PAD,
    )

    root.geometry(f"+{__WIN_START_POS[0]}+{__WIN_START_POS[1]}")
    root.resizable(width=False, height=False)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    main()
