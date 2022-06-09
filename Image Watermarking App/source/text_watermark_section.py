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

        # create widgets
        self.watermark_entry = tk.Entry(
            self,
        )
        self.watermark_button = tk.Button(
            self,
            text="Update Watermark",
            width=20,
            bg=sett.PRIMARY_APP_COLOR,
        )

        self.watermark_settings = WatermarkSettings(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )
        self.watermark_positioning = WatermarkPositioning(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )

        watermark_label = tk.Label(
            self,
            text="Text Watermark:",
            bg=sett.PRIMARY_APP_COLOR,
        )

        # place widgets
        watermark_label.grid(
            column=0,
            row=0,
            sticky="W",
            padx=(0, 38),
        )
        self.watermark_entry.grid(
            column=1,
            row=0,
            sticky="EW",
        )
        self.watermark_button.grid(
            column=2,
            row=0,
            sticky="E",
            padx=(10, 0),
        )
        self.watermark_settings.grid(
            column=0,
            row=1,
            columnspan=3,
            sticky="EW"
        )
        self.watermark_positioning.grid(
            column=0,
            row=2,
            columnspan=3,
            sticky="EW",
        )