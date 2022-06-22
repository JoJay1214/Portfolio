"""
Image Watermarking App
file:   file_manage_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for file management in the Image Watermarking App.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

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
        self.parent = parent       # the parent container

        self.browse_entry = None   # entry to file with file path
        self.browse_button = None  # button to browse for file
        self.save_button = None    # button to save file

        # PRIVATE VARIABLES
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

        self.browse_entry.config(state="normal")
        self.browse_entry.delete(0, tk.END)
        self.browse_entry.insert(0, filepath)
        self.browse_entry.config(state="disabled")

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
        self.browse_entry = tk.Entry(
            self,
            font=sett.SEC_CONTENT_FONT,
            state="disabled",
        )
        self.browse_button = tk.Button(
            self,
            text="Browse",
            width=sett.BROWSE_BTN_WIDTH,
            bg=sett.PRIMARY_APP_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

        # SAVE
        self.save_button = tk.Button(
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
        self.browse_entry.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=sett.SEC_ENTRY_PAD_X,
        )
        self.browse_button.grid(
            column=2,
            row=1,
            padx=(0, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        # SAVE
        self.save_button.grid(
            column=1,
            row=2,
            pady=sett.SAVE_BUTTON_PAD_Y,
        )
