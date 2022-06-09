"""
Image Watermarking App
file:   file_manage_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for file management in the Image Watermarking App.

"""
import tkinter as tk

import source.app_settings as sett


class FileManageSection(tk.Frame):
    """
    TKinter Frame that holds the widgets used for file management in the Image Watermarking App
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.grid_columnconfigure(1, weight=1)

        # create widgets
        self.browse_entry = tk.Entry(
            self,
            state="disabled"
        )
        self.browse_button = tk.Button(
            self,
            text="Browse",
            width=20,
            bg=sett.PRIMARY_APP_COLOR,
        )
        self.save_button = tk.Button(
            self,
            text="Save Watermarked Copy",
            bg=sett.PRIMARY_APP_COLOR,
        )

        browse_label = tk.Label(
            self,
            text="Image for Watermark:",
            bg=sett.PRIMARY_APP_COLOR,
        )

        # place widgets
        browse_label.grid(
            column=0,
            row=0,
            sticky="W",
            padx=(0, 10),
        )
        self.browse_entry.grid(
            column=1,
            row=0,
            sticky="EW",
        )
        self.browse_button.grid(
            column=2,
            row=0,
            padx=(10, 0),
        )
        self.save_button.grid(
            column=1,
            row=1,
        )

    def update_browse_entry(self, filepath: str):
        """
        Fill the browse entry with a given filepath string
        :param filepath: The path to the image file
        """

        self.browse_entry.config(state="normal")
        self.browse_entry.delete(0, tk.END)
        self.browse_entry.insert(0, filepath)
        self.browse_entry.config(state="disabled")
