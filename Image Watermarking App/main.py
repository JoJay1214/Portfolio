"""
Image Watermarking App
file:   main.py
author: Joshua Jacobs
date:   6/10/2022
brief:  Desktop application that allows a user to browse for an image file, then save a copy of the
        image with a user inputted watermark.

"""
import tkinter as tk

from source.image_watermarking_application import ImageWatermarkingApplication
import source.app_settings as sett


def main():
    """
    Create a TKinter window and configure it. Then, configure the Image Watermarking app.
    # """
    root = tk.Tk()

    root.title("Image Watermarking")
    root.config(
        bg=sett.PRIMARY_APP_COLOR,
        padx=sett.WIN_PAD_X,
        pady=sett.WIN_PAD_Y,
    )
    root.geometry(f"+{sett.WIN_START_POS[0]}+{sett.WIN_START_POS[1]}")

    ImageWatermarkingApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
