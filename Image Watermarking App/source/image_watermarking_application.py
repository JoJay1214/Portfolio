"""
Image Watermarking App
file:   image_watermarking_application.py
author: Joshua Jacobs
date:   6/6/2022
brief:  Main TKinter GUI for Image Watermarking App.

"""
import tkinter as tk

from source.file_manage_section import FileManageSection
from source.image_canvases import ImageCanvases
from source.text_watermark_section import TextWatermarkSection

import source.app_settings as sett


class ImageWatermarkingApplication(tk.Frame):
    """
    Main TKinter GUI for Image Watermarking App
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create sections
        self.file_manage_section = FileManageSection(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )
        self.text_watermark_section = TextWatermarkSection(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )
        self.image_canvases = ImageCanvases(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )

        # place sections
        self.file_manage_section.grid(
            column=0,
            row=0,
            sticky="EW",
        )
        self.text_watermark_section.grid(
            column=0,
            row=1,
            sticky="EW",
        )
        self.image_canvases.grid(
            column=3,
            row=0,
            rowspan=4,
        )
