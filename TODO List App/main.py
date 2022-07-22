"""
TODO List App
file:   main.py
author: Joshua Jacobs
date:   7/19/2022
brief:  An application used to manage digital to-do lists, built using TKinter

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.todo_list_app import TODOListApp

__WIN_START_POS = (100, 50)


def main():
    """
    An application used to manage digital to-do lists, built using TKinter
    """

    # root window
    root = tk.Tk()
    __config_root_window(root)

    # app
    todo_list_app = TODOListApp(
        root,
    )
    todo_list_app.grid(
        column=0,
        row=0,
        sticky="NESW",
    )

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
