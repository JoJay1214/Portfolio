"""
Image Watermarking App
file:   main.py
author: Joshua Jacobs
date:   6/10/2022
brief:  Desktop application that allows a user to browse for an image file, then save a copy of the
        image with a user inputted watermark.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.image_watermarking_application import ImageWatermarkingApplication

import source.app_settings as sett

"""
MAIN
"""


def main():
    """
    Create a TKinter window and configure it. Then, configure the Image Watermarking app.
    """

    # root window
    root = tk.Tk()
    __config_root_window(root)

    # image watermarking app
    image_wm_app = ImageWatermarkingApplication(
        root,
        bg=sett.PRIMARY_APP_COLOR,
    )
    image_wm_app.grid(
        column=0,
        row=0,
        sticky="NESW"
    )

    root.mainloop()
    
    
"""
PRIVATE METHODS
"""


def __config_root_window(root: tk.Tk):
    root.title("Image Watermarking")
    root.config(
        bg=sett.PRIMARY_APP_COLOR,
        padx=sett.WIN_PAD_X,
        pady=sett.WIN_PAD_Y,
    )

    root.geometry(f"+{sett.WIN_START_POS[0]}+{sett.WIN_START_POS[1]}")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    main()
