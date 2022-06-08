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
        self.__font_size_scale = tk.Scale(
            self,
            from_=1,
            to=200,
            orient=tk.HORIZONTAL,
            # command=self.__update_canvas_images,
            bg=sett.PRIMARY_APP_COLOR,
            highlightbackground=sett.PRIMARY_APP_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.__alpha_scale = tk.Scale(
            self,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            # command=self.__update_canvas_images,
            bg=sett.PRIMARY_APP_COLOR,
            highlightbackground=sett.PRIMARY_APP_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )

        __font_size_label = tk.Label(
            self,
            text="Font Size:",
            bg=sett.PRIMARY_APP_COLOR,
        )
        font_alpha_label = tk.Label(
            self,
            text="Alpha:",
            bg=sett.PRIMARY_APP_COLOR,
        )

        # set scale defaults
        self.__font_size_scale.set(50)
        self.__alpha_scale.set(255)

        # place widgets
        __font_size_label.grid(
            column=0,
            row=0,
            sticky="SW",
            padx=(0, 10),
        )
        self.__font_size_scale.grid(
            column=1,
            row=0,
            columnspan=2,
            sticky="EW"
        )

        font_alpha_label.grid(
            column=0,
            row=1,
            sticky="SW",
            padx=(0, 10),
        )
        self.__alpha_scale.grid(
            column=1,
            row=1,
            columnspan=2,
            sticky="EW",
        )