"""
Image Watermarking App
file:   image_canvases.py
author: Joshua Jacobs
date:   6/6/2022
brief:  TKinter Frame that holds the canvases and canvas items to show a resized version of the original image
        and a resized version of the watermarked image.

"""
import tkinter as tk
from PIL import ImageTk

import source.app_settings as sett


class ImageCanvases(tk.Frame):
    """
    TKinter Frame that holds the canvases and canvas items to show a resized version of the
    original image and a resized version of the watermarked image
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.img_resized = None
        self.img_wm_resized = None

        # create widgets
        self.orig_img_canvas = tk.Canvas(
            self,
            width=sett.CANVAS_WIDTH,
            height=sett.CANVAS_HEIGHT,
            bg=sett.CANVAS_BG_COLOR,
            highlightbackground=sett.PRIMARY_APP_COLOR,
        )
        self.wm_img_canvas = tk.Canvas(
            self,
            width=sett.CANVAS_WIDTH,
            height=sett.CANVAS_HEIGHT,
            bg=sett.CANVAS_BG_COLOR,
            highlightbackground=sett.PRIMARY_APP_COLOR,
        )

        self.orig_img_item = None
        self.wm_img_item = None

        # place widgets
        self.orig_img_canvas.grid(
            column=0,
            row=0,
            pady=(0, sett.CANVAS_PAD_Y),
        )
        self.wm_img_canvas.grid(
            column=0,
            row=1,
            pady=(sett.CANVAS_PAD_Y, 0),
        )

    def set_canvas_images(self, img_resized: tk.Image, img_wm_resized: tk.Image):
        # store photo images so garbage collector doesn't trash them
        self.img_resized = ImageTk.PhotoImage(img_resized)
        self.img_wm_resized = ImageTk.PhotoImage(img_wm_resized)

        self.__update_canvas_items()

    def __update_canvas_items(self):
        """
        Update the items on the canvases that hold the images. Creates them if they do not yet exist
        """

        if self.orig_img_item and self.wm_img_item:
            # configure canvas items if they exist
            self.orig_img_canvas.itemconfig(
                self.orig_img_item,
                image=self.img_resized,
            )
            self.wm_img_canvas.itemconfig(
                self.wm_img_item,
                image=self.img_wm_resized,
            )

        else:
            # create canvas items if they do not yet exist
            self.orig_img_item = self.orig_img_canvas.create_image(
                sett.CANVAS_WIDTH / 2,
                sett.CANVAS_HEIGHT / 2,
                anchor="center",
                image=self.img_resized,
            )
            self.wm_img_item = self.wm_img_canvas.create_image(
                sett.CANVAS_WIDTH / 2,
                sett.CANVAS_HEIGHT / 2,
                anchor="center",
                image=self.img_wm_resized,
            )
