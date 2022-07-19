"""
TODO List App
file:   main.py
author: Joshua Jacobs
date:   7/19/2022
brief:  descrip

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
# put here

__WIN_START_POS = (350, 50)


def main():
    """
    descrip
    """

    # root window
    root = tk.Tk()
    __config_root_window(root)

    # app
    # put here

    root.mainloop()


def __config_root_window(root: tk.Tk):
    root.title("TODO List")
    root.config(

    )

    root.geometry(f"+{__WIN_START_POS[0]}+{__WIN_START_POS[1]}")
    root.resizable(width=False, height=False)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    main()
