"""
Image Watermarking App
file:   main.py
author: Joshua Jacobs
date:   3/11/2022
brief:  Desktop application that allows a user to browse for an image file, then save a copy of the
        image with a user inputted watermark.

"""
from source.watermark import Watermark
from source.ui import ImageWatermarkingUI
import tkinter as tk
from source.image_watermarking_application import ImageWatermarkingApplication


def main():
    """
    Creates a Watermark instance and configures the Watermarking UI, then runs the Image Watermarking app.
    # """
    # watermark = Watermark()
    # ImageWatermarkingUI(watermark)
    root = tk.Tk()

    root.title("Image Watermarking")

    ImageWatermarkingApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
