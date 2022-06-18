"""
Image Watermarking App
file:   text_watermark_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for the text watermark and its settings.

"""
import tkinter as tk

from source.watermark_settings import WatermarkSettings
from source.watermark_positioning import WatermarkPositioning

import source.app_settings as sett


class TextWatermarkSection(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the text watermark and its settings
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # create widgets
        self.watermark_entry = tk.Entry(
            self,
            font=sett.SEC_CONTENT_FONT,
        )
        self.watermark_button = tk.Button(
            self,
            text="Update Text",
            width=20,
            bg=sett.PRIMARY_APP_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

        self.watermark_settings = WatermarkSettings(
            self,
            bg=sett.SUBSEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SUBSEC_HL_COLOR,
        )
        self.watermark_positioning = WatermarkPositioning(
            self,
            bg=sett.SUBSEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SUBSEC_HL_COLOR,
        )

        section_title_label = tk.Label(
            self,
            text="Watermark",
            bg=sett.SEC_BG_COLOR,
            font=sett.SEC_TITLE_FONT,
        )

        watermark_text_label = tk.Label(
            self,
            text="Text:",
            bg=sett.SEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

        # place widgets
        section_title_label.grid(
            column=0,
            row=0,
            columnspan=3,
            sticky="NW",
            padx=sett.SEC_TITLE_PAD_X,
            pady=sett.SEC_TITLE_PAD_Y,
        )

        watermark_text_label.grid(
            column=0,
            row=1,
            sticky="W",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.watermark_entry.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=sett.SEC_ENTRY_PAD_X,
        )
        self.watermark_button.grid(
            column=2,
            row=1,
            sticky="E",
            padx=(0, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        self.watermark_settings.grid(
            column=0,
            row=2,
            columnspan=3,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )
        self.watermark_positioning.grid(
            column=0,
            row=3,
            columnspan=3,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )
