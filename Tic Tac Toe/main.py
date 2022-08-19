"""
Tic Tac Toe
file:   main.py
author: Joshua Jacobs
date:   7/3/2022
brief:  The classic Tic Tac Toe game presented in a GUI that was built using
        TKinter. The game is built for two players to switch off taking their
        turns; and resets after a round is decided.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.tic_tac_toe_app import TicTacToeApplication

"""
CONSTANTS
"""

__WIN_START_POS = (350, 50)
__WINDOW_PAD = 20

"""
MAIN
"""


def main():
    """
    The classic Tic Tac Toe game presented in a GUI that was built using TKinter. The game is
    built for two players to switch off taking their turns; and resets after a round is decided
    """

    # root window
    root = tk.Tk()
    __config_root_window(root)

    # tic-tac-toe app
    tic_tac_toe_app = TicTacToeApplication(
        root,
    )
    tic_tac_toe_app.grid(
        column=0,
        row=0,
        sticky="NESW",
    )

    root.mainloop()
    
    
"""
PRIVATE METHODDS
"""


def __config_root_window(root: tk.Tk):

    root.title("Tic Tac Toe")
    root.config(
        padx=__WINDOW_PAD,
        pady=__WINDOW_PAD,
    )

    root.geometry(f"+{__WIN_START_POS[0]}+{__WIN_START_POS[1]}")
    root.resizable(width=False, height=False)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    main()
