"""
Image Watermarking App
file:   image_watermarking_application.py
author: Joshua Jacobs
date:   6/6/2022
brief:  Main TKinter GUI for Image Watermarking App.

"""
import tkinter as tk

from source.image_canvases import ImageCanvases


class ImageWatermarkingApplication(tk.Frame):
    """
    Main TKinter GUI for Image Watermarking App
    """

    def __init__(self, parent: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # create
        self.image_canvases = ImageCanvases(self)

        # place
        self.image_canvases.grid(
            column=1,
            row=0,
        )
