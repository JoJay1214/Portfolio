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
        self.__browse_entry = tk.Entry(
            self,
            state="disabled"
        )

        __browse_label = tk.Label(
            self,
            text="Image for Watermark:",
            bg=sett.PRIMARY_APP_COLOR,
        )
        __browse_button = tk.Button(
            self,
            text="Browse",
            # command=self.__browse_for_file,
            width=20,
            bg=sett.PRIMARY_APP_COLOR,
        )
        __save_button = tk.Button(
            self,
            text="Save Watermarked Copy",
            # command=self.__save_watermarked_image,
            bg=sett.PRIMARY_APP_COLOR,
        )

        # place widgets
        __browse_label.grid(
            column=0,
            row=0,
            sticky="W",
            padx=(0, 10),
        )
        self.__browse_entry.grid(
            column=1,
            row=0,
            sticky="EW",
        )
        __browse_button.grid(
            column=2,
            row=0,
            padx=(10, 0),
        )
        __save_button.grid(
            column=1,
            row=1,
        )
