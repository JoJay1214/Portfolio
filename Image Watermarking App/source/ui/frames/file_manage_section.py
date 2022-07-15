"""
Image Watermarking App
file:   file_manage_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for file management in the Image Watermarking App.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

from typing import Callable

# PROJECT IMPORTS
import source.app_settings as sett


class FileManageSection(tk.Frame):
    """
    TKinter Frame that holds the widgets used for file management in the Image Watermarking App
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Constructor for the File Manage section of the Image Watermarking app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__browse_entry = None         # entry to file with file path
        self.__browse_button = None        # button to browse for file
        self.__save_button = None          # button to save file

        self.__section_title_label = None  # file section title label
        self.__image_for_wm_label = None   # image for watermarking label

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def update_browse_entry(self, filepath: str):
        """
        Fill the browse entry with a given filepath string
        :param filepath: The path to the image file
        """

        self.__browse_entry.config(state="normal")
        self.__browse_entry.delete(0, tk.END)
        self.__browse_entry.insert(0, filepath)
        self.__browse_entry.config(state="disabled")

    def set_browse_btn_cmd(self, cmd: Callable):
        """
        Set the command for the TK Button use for file browsing
        :param cmd: The function to call when the button is pressed
        """

        self.__browse_button.config(
            command=cmd,
        )

    def set_save_btn_cmd(self, cmd: Callable):
        """
        Set the command for the TK Button use for saving files
        :param cmd: The function to call when the button is pressed
        """

        self.__save_button.config(
            command=cmd,
        )

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__section_title_label = tk.Label(
            self,
            text="File",
            bg=sett.SEC_BG_COLOR,
            font=sett.SEC_TITLE_FONT,
        )

        # BROWSE
        self.__image_for_wm_label = tk.Label(
            self,
            text="Image for Watermark:",
            bg=sett.SEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__browse_entry = tk.Entry(
            self,
            font=sett.SEC_CONTENT_FONT,
            state="disabled",
        )
        self.__browse_button = tk.Button(
            self,
            text="Browse",
            width=sett.BROWSE_BTN_WIDTH,
            bg=sett.PRIMARY_APP_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

        # SAVE
        self.__save_button = tk.Button(
            self,
            text="Save Watermarked Copy",
            bg=sett.PRIMARY_APP_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

    def __place_widgets(self):

        # TITLE
        self.__section_title_label.grid(
            column=0,
            row=0,
            columnspan=3,
            sticky="NW",
            padx=sett.SEC_TITLE_PAD_X,
            pady=sett.SEC_TITLE_PAD_Y,
        )

        # BROWSE
        self.__image_for_wm_label.grid(
            column=0,
            row=1,
            sticky="W",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.__browse_entry.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=sett.SEC_ENTRY_PAD_X,
        )
        self.__browse_button.grid(
            column=2,
            row=1,
            padx=(0, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        # SAVE
        self.__save_button.grid(
            column=1,
            row=2,
            pady=sett.SAVE_BUTTON_PAD_Y,
        )
