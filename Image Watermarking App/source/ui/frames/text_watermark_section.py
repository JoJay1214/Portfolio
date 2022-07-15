"""
Image Watermarking App
file:   text_watermark_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for the text watermark and its settings.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

from typing import Callable

# PROJECT IMPORTS
from source.ui.frames.watermark_font_settings_section import WatermarkFontSettingsSection
from source.ui.frames.watermark_positioning_section import WatermarkPositioningSection

import source.app_settings as sett


class TextWatermarkSection(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the text watermark and its settings
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Constructor for the Text Watermark section of the Image Watermarking app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent                 # the parent container

        self.watermark_font_settings = None  # section used to control watermark font settings
        self.watermark_positioning = None    # section used to control watermark position

        # PRIVATE VARIABLES
        self.__watermark_entry = None          # entry for inputting watermark text
        self.__update_watermark_button = None  # button used to update watermark text on image
        self.__section_title_label = None      # text watermark section title label
        self.__watermark_text_label = None     # Text label for watermark entry

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def get_watermark_entry_text(self) -> str:
        """
        Get the string of text that has been entered in the Watermark Entry
        :returns: The string of text to be used to watermark
        """

        return self.__watermark_entry.get()

    def set_update_watermark_btn_cmd(self, cmd: Callable):
        """
        Set the command of the TK Button used for updating the watermark on the image
        """

        self.__update_watermark_button.config(
            command=cmd,
        )

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__section_title_label = tk.Label(
            self,
            text="Watermark",
            bg=sett.SEC_BG_COLOR,
            font=sett.SEC_TITLE_FONT,
        )

        # WATERMARK TEXT
        self.__watermark_text_label = tk.Label(
            self,
            text="Text:",
            bg=sett.SEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__watermark_entry = tk.Entry(
            self,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__update_watermark_button = tk.Button(
            self,
            text="Update Text",
            width=sett.UPDATE_WATERMARK_BTN_WIDTH,
            bg=sett.PRIMARY_APP_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

        # WATERMARK FONT SETTINGS
        self.watermark_font_settings = WatermarkFontSettingsSection(
            self,
            bg=sett.SUBSEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SUBSEC_HL_COLOR,
        )

        # WATERMARK POSITIONING
        self.watermark_positioning = WatermarkPositioningSection(
            self,
            bg=sett.SUBSEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SUBSEC_HL_COLOR,
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

        # WATERMARK TEXT
        self.__watermark_text_label.grid(
            column=0,
            row=1,
            sticky="W",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.__watermark_entry.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=sett.SEC_ENTRY_PAD_X,
        )
        self.__update_watermark_button.grid(
            column=2,
            row=1,
            sticky="E",
            padx=(0, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        # WATERMARK FONT SETTINGS
        self.watermark_font_settings.grid(
            column=0,
            row=2,
            columnspan=3,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )

        # WATERMARK POSITIONING
        self.watermark_positioning.grid(
            column=0,
            row=3,
            columnspan=3,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )
