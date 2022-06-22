"""
Image Watermarking App
file:   image_canvases_section.py
author: Joshua Jacobs
date:   6/6/2022
brief:  TKinter Frame that holds the canvases and canvas items to show a resized version of the original image
        and a resized version of the watermarked image.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk
from PIL import ImageTk

# PROJECT IMPORTS
import source.app_settings as sett


class ImageCanvasesSection(tk.Frame):
    """
    TKinter Frame that holds the canvases and canvas items to show a resized version of the
    original image and a resized version of the watermarked image
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Constructor for the Image Canvases section of the Image Watermarking app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__img_resized = None         # image, resized to fit the canvas
        self.__img_canvas = None          # canvas for displaying image
        self.__img_canvas_item = None     # canvas item to hold image

        self.__wm_img_resized = None      # watermarked image, resized to fit a canvas
        self.__wm_img_canvas = None       # canvas for displaying watermarked image
        self.__wm_img_canvas_item = None  # canvas item to hold watermarked image

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def set_canvas_images(self, img_resized: tk.Image, img_wm_resized: tk.Image):
        """
        Set the images to be displayed in the canvases and update the canvas items
        (Store Tk Images so garbage collector doesn't trash them)
        :param img_resized: A resized Tk Image
        :param img_wm_resized: A resized Tk Image with a text watermark on it
        """

        self.__img_resized = ImageTk.PhotoImage(img_resized)
        self.__wm_img_resized = ImageTk.PhotoImage(img_wm_resized)

        self.__update_canvas_items()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # CANVASES
        self.__img_canvas = tk.Canvas(
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

    def __place_widgets(self):

        # CANVASES
        self.__img_canvas.grid(
            column=0,
            row=0,
            pady=(0, sett.CANVAS_PAD_Y),
        )
        self.__wm_img_canvas.grid(
            column=0,
            row=1,
            pady=(sett.CANVAS_PAD_Y, 0),
        )

    def __update_canvas_items(self):
        """
        Update the items on the canvases that hold the images. Creates them if they do not yet exist
        """

        if self.__img_canvas_item and self.__wm_img_canvas_item:
            # configure canvas items if they exist
            self.__img_canvas.itemconfig(
                self.__img_canvas_item,
                image=self.__img_resized,
            )
            self.__wm_img_canvas.itemconfig(
                self.__wm_img_canvas_item,
                image=self.__wm_img_resized,
            )

        else:
            # create canvas items if they do not yet exist
            self.__img_canvas_item = self.__img_canvas.create_image(
                sett.CANVAS_WIDTH / 2,
                sett.CANVAS_HEIGHT / 2,
                anchor="center",
                image=self.__img_resized,
            )
            self.__wm_img_canvas_item = self.__wm_img_canvas.create_image(
                sett.CANVAS_WIDTH / 2,
                sett.CANVAS_HEIGHT / 2,
                anchor="center",
                image=self.__wm_img_resized,
            )
