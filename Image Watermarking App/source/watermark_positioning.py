"""
Image Watermarking App
file:   watermark_positioning.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for the text watermark positioning.

"""
import tkinter as tk

import source.app_settings as sett


class WatermarkPositioning(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the text watermark positioning
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.grid_columnconfigure(1, weight=1)

        # create widgets
        self.x_pos_scale = tk.Scale(
            self,
            from_=0,
            to=0,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.y_pos_scale = tk.Scale(
            self,
            from_=0,
            to=0,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )

        section_title_label = tk.Label(
            self,
            text="Text Position",
            bg=sett.SUBSEC_BG_COLOR,
        )

        x_pos_label = tk.Label(
            self,
            text="Horizontal Position:",
            bg=sett.SUBSEC_BG_COLOR,
        )
        y_pos_label = tk.Label(
            self,
            text="Vertical Position:",
            bg=sett.SUBSEC_BG_COLOR,
        )

        # set scale defaults
        self.x_pos_scale.set(0)
        self.y_pos_scale.set(0)

        # place widgets
        section_title_label.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="NW",
            padx=sett.SEC_TITLE_PAD_X,
            pady=sett.SEC_TITLE_PAD_Y,
        )

        x_pos_label.grid(
            column=0,
            row=1,
            sticky="SW",
            padx=(sett.SEC_CONTENT_PAD, 0),
        )
        self.x_pos_scale.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=(0, sett.SEC_CONTENT_PAD),
        )

        y_pos_label.grid(
            column=0,
            row=2,
            sticky="SW",
            padx=(sett.SEC_CONTENT_PAD, 0),
        )
        self.y_pos_scale.grid(
            column=1,
            row=2,
            sticky="EW",
            padx=(0, sett.SEC_CONTENT_PAD),
        )

    # noinspection PyTypeChecker
    def update_position_scales(self, img: tk.Image):
        """
        Update the watermark text position scales' X/Y max to reflect the width and height of the current image
        """

        if img:
            # reset pos to (0, 0)
            self.x_pos_scale.set(0)
            self.y_pos_scale.set(0)

            # set scales' max to image width and height, respectively
            self.x_pos_scale.config(
                to=img.width,
            )
            self.y_pos_scale.config(
                to=img.height,
            )
