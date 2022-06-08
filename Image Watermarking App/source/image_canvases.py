"""
Image Watermarking App
file:   image_canvases.py
author: Joshua Jacobs
date:   6/6/2022
brief:  TKinter Frame that holds the canvases and canvas items to show a resized version of the original image
        and a resized version of the watermarked image.

"""
import tkinter as tk

import source.app_settings as sett


class ImageCanvases(tk.Frame):
    """
    TKinter Frame that holds the canvases and canvas items to show a resized version of the
    original image and a resized version of the watermarked image
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create widgets
        self.__orig_img_canvas = tk.Canvas(
            self,
            width=sett.CANVAS_WIDTH,
            height=sett.CANVAS_HEIGHT,
            bg=sett.CANVAS_BG_COLOR,
            highlightbackground=sett.PRIMARY_APP_COLOR,
        )
        self.__wm_img_canvas = tk.Canvas(
            self,
            width=sett.CANVAS_WIDTH,
            height=sett.CANVAS_HEIGHT,
            bg=sett.CANVAS_BG_COLOR,
            highlightbackground=sett.PRIMARY_APP_COLOR,
        )

        # place widgets
        self.__orig_img_canvas.grid(
            column=0,
            row=0,
            pady=(0, sett.CANVAS_PAD_Y),
        )
        self.__wm_img_canvas.grid(
            column=0,
            row=1,
            pady=(sett.CANVAS_PAD_Y, 0),
        )
