"""
Image Watermarking App
file:   image_watermarking_application.py
author: Joshua Jacobs
date:   6/6/2022
brief:  TKinter Frame that holds the canvases and canvas items to show a resized version of the original image
        and a resized version of the watermarked image.

"""
import tkinter as tk


class ImageCanvases(tk.Frame):
    """
    TKinter Frame that holds the canvases and canvas items to show a resized version of the
    original image and a resized version of the watermarked image
    """

    __CANVAS_WIDTH = 540               # width of the canvases the images sit on
    __CANVAS_HEIGHT = 304              # height of the canvases the images sit on

    __CANVAS_BG_COLOR = "#000000"         # canvas background color
    __CANVAS_HIGHLIGHT_COLOR = "#CCCCCC"  # canvas border color

    __CANVAS_PAD_Y = 5

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # create widgets
        self.__orig_img_canvas = tk.Canvas(
            self,
            width=self.__CANVAS_WIDTH,
            height=self.__CANVAS_HEIGHT,
            bg=self.__CANVAS_BG_COLOR,
            highlightbackground=self.__CANVAS_HIGHLIGHT_COLOR,
        )
        self.__wm_img_canvas = tk.Canvas(
            self,
            width=self.__CANVAS_WIDTH,
            height=self.__CANVAS_HEIGHT,
            bg=self.__CANVAS_BG_COLOR,
            highlightbackground=self.__CANVAS_HIGHLIGHT_COLOR,
        )

        # place widgets
        self.__orig_img_canvas.grid(
            column=0,
            row=0,
            pady=(0, self.__CANVAS_PAD_Y),
        )
        self.__wm_img_canvas.grid(
            column=0,
            row=1,
            pady=(self.__CANVAS_PAD_Y, 0),
        )
