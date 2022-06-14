"""
Image Watermarking App
file:   watermark_settings.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for the text watermark font settings.

"""
import tkinter as tk

import source.app_settings as sett


class WatermarkSettings(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the text watermark font settings
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.grid_columnconfigure(1, weight=1)

        # create widgets
        self.font_size_scale = tk.Scale(
            self,
            from_=1,
            to=200,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.alpha_scale = tk.Scale(
            self,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )

        section_title_label = tk.Label(
            self,
            text="Text Settings",
            bg=sett.SUBSEC_BG_COLOR,
        )
        font_size_label = tk.Label(
            self,
            text="Font Size:",
            bg=sett.SUBSEC_BG_COLOR,
        )
        font_alpha_label = tk.Label(
            self,
            text="Alpha:",
            bg=sett.SUBSEC_BG_COLOR,
        )

        # set scale defaults
        self.font_size_scale.set(50)
        self.alpha_scale.set(255)

        # place widgets
        section_title_label.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="NW",
            padx=sett.SEC_TITLE_PAD_X,
            pady=sett.SEC_TITLE_PAD_Y,
        )

        font_size_label.grid(
            column=0,
            row=1,
            sticky="SW",
            padx=(sett.SEC_CONTENT_PAD, 0),
        )
        self.font_size_scale.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=(0, sett.SEC_CONTENT_PAD),
        )

        font_alpha_label.grid(
            column=0,
            row=2,
            sticky="SW",
            padx=(sett.SEC_CONTENT_PAD, 0),
        )
        self.alpha_scale.grid(
            column=1,
            row=2,
            sticky="EW",
            padx=(0, sett.SEC_CONTENT_PAD),
        )
