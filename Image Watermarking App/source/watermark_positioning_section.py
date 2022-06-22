"""
Image Watermarking App
file:   watermark_positioning_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for the text watermark positioning.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
import source.app_settings as sett


class WatermarkPositioningSection(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the text watermark positioning
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Constructor for the Watermark Positioning section of the Image Watermarking app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent     # the parent container

        self.x_pos_scale = None  # watermark horizontal positioning scale
        self.y_pos_scale = None  # watermark vertical positioning scale

        # PRIVATE VARIABLES
        self.__section_title_label = None  # watermark positioning section title label
        self.__x_pos_label = None          # horizontal label for scale
        self.__y_pos_label = None          # vertical label for scale

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def update_position_scales(self, img: tk.Image):
        """
        Update the watermark text position scales' X/Y max to reflect the width and height of the current image
        :param img: The Image to take the width/height from to use as max scale values
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

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__section_title_label = tk.Label(
            self,
            text="Text Position",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_TITLE_FONT,
        )

        # X-POS
        self.__x_pos_label = tk.Label(
            self,
            text="Horizontal Position:",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.x_pos_scale = tk.Scale(
            self,
            from_=0,
            to=0,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.x_pos_scale.set(0)

        # Y-POS
        self.__y_pos_label = tk.Label(
            self,
            text="Vertical Position:",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.y_pos_scale = tk.Scale(
            self,
            from_=0,
            to=0,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.y_pos_scale.set(0)

    def __place_widgets(self):

        # TITLE
        self.__section_title_label.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="NW",
            padx=sett.SEC_TITLE_PAD_X,
            pady=sett.SEC_TITLE_PAD_Y,
        )

        # X-POS
        self.__x_pos_label.grid(
            column=0,
            row=1,
            sticky="SW",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.x_pos_scale.grid(
            column=1,
            row=1,
            sticky="EW",
            padx=(sett.SEC_SCALE_PAD_LEFT, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        # Y-POS
        self.__y_pos_label.grid(
            column=0,
            row=2,
            sticky="SW",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.y_pos_scale.grid(
            column=1,
            row=2,
            sticky="EW",
            padx=(sett.SEC_SCALE_PAD_LEFT, sett.SEC_CONTENT_OUTER_PAD_X),
        )
