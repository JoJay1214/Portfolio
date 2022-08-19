"""
Image Watermarking App
file:   watermark_font_settings_section.py
author: Joshua Jacobs
date:   6/7/2022
brief:  TKinter Frame that holds the widgets used for the text watermark font settings.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

from typing import Callable

# PROJECT IMPORTS
import source.app_settings as sett


class WatermarkFontSettingsSection(tk.Frame):
    """
    TKinter Frame that holds the widgets used for the text watermark font settings
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent, *args, **kwargs):
        """
        Constructor for the Watermark Font Settings section of the Image Watermarking app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__font_size_scale = None      # scale that controls watermark text font size
        self.__alpha_scale = None          # scale that controls watermark text transparency
        self.__radiobutton_white = None    # radio button to pick the color white
        self.__radiobutton_black = None    # radio button to pick the color black

        self.__section_title_label = None  # watermark font settings section title label
        self.__font_size_label = None      # font size label for scale
        self.__font_alpha_label = None     # font alpha label for scale
        self.__text_color_label = None     # text color label for radio buttons

        self.__current_color = tk.StringVar(value="255, 255, 255")

        # CONFIG SELF
        self.__create_widgets()
        self.__place_widgets()

    """
    PUBLIC METHODS
    """

    def sel(self):
        print("meow")

    def get_font_size_value(self):
        """
        Get the value stored in the font size scale
        :returns: The font size value
        """

        return self.__font_size_scale.get()

    def get_alpha_value(self):
        """
        Get the value stored in the alpha scale
        :returns: The alpha value
        """

        return self.__alpha_scale.get()

    def set_font_size_scale_cmd(self, cmd: Callable):
        """
        Set the command for when the scale is interacted with
        :param cmd: The function to call when the scale is interacted with
        """

        self.__font_size_scale.config(
            command=cmd,
        )

    def set_alpha_scale_cmd(self, cmd: Callable):
        """
        Set the command for when the scale is interacted with
        :param cmd: The function to call when the scale is interacted with
        """

        self.__alpha_scale.config(
            command=cmd,
        )

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__section_title_label = tk.Label(
            self,
            text="Text Settings",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_TITLE_FONT,
        )

        # TEXT COLOR
        self.__text_color_label = tk.Label(
            self,
            text="Color:",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__radiobutton_white = tk.Radiobutton(
            self,
            text="White",
            value="255, 255, 255",
            variable=self.__current_color,
            command=self.sel,
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__radiobutton_black = tk.Radiobutton(
            self,
            text="Black",
            value="0, 0, 0",
            variable=self.__current_color,
            command=self.sel,
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )

        # FONT ALPHA
        self.__font_alpha_label = tk.Label(
            self,
            text="Alpha:",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__alpha_scale = tk.Scale(
            self,
            from_=sett.ALPHA_MIN,
            to=sett.ALPHA_MAX,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.__alpha_scale.set(sett.ALPHA_SCALE_DEFAULT)

        # FONT SIZE
        self.__font_size_label = tk.Label(
            self,
            text="Font Size:",
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
        )
        self.__font_size_scale = tk.Scale(
            self,
            from_=sett.FONT_SIZE_MIN,
            to=sett.FONT_SIZE_MAX,
            orient=tk.HORIZONTAL,
            bg=sett.SUBSEC_BG_COLOR,
            font=sett.SEC_CONTENT_FONT,
            highlightbackground=sett.SUBSEC_BG_COLOR,
            troughcolor=sett.TROUGH_COLOR,
        )
        self.__font_size_scale.set(sett.FONT_SIZE_SCALE_DEFAULT)

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

        # TEXT COLOR
        self.__text_color_label.grid(
            column=0,
            row=1,
            sticky="SW",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.__radiobutton_white.grid(
            column=1,
            row=1,
            sticky="EW",
        )
        self.__radiobutton_black.grid(
            column=2,
            row=1,
            sticky="EW",
            padx=(0, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        # FONT ALPHA
        self.__font_alpha_label.grid(
            column=0,
            row=2,
            sticky="SW",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.__alpha_scale.grid(
            column=1,
            row=2,
            columnspan=2,
            sticky="EW",
            padx=(sett.SEC_SCALE_PAD_LEFT, sett.SEC_CONTENT_OUTER_PAD_X),
        )

        # FONT SIZE
        self.__font_size_label.grid(
            column=0,
            row=3,
            sticky="SW",
            padx=(sett.SEC_CONTENT_OUTER_PAD_X, 0),
        )
        self.__font_size_scale.grid(
            column=1,
            row=3,
            columnspan=2,
            sticky="EW",
            padx=(sett.SEC_SCALE_PAD_LEFT, sett.SEC_CONTENT_OUTER_PAD_X),
        )
