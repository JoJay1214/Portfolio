"""
Image Watermarking App
file:   image_watermarking_application.py
author: Joshua Jacobs
date:   6/6/2022
brief:  Main TKinter GUI for Image Watermarking App.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk
from tkinter import filedialog

# PROJECT IMPORTS
from source.ui.frames.file_manage_section import FileManageSection
from source.ui.frames.text_watermark_section import TextWatermarkSection
from source.ui.frames.image_canvases_section import ImageCanvasesSection
from source.watermark import Watermark

import source.app_settings as sett


class ImageWatermarkingApplication(tk.Frame):
    """
    Main TKinter GUI for Image Watermarking App
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        Constructor for the Image Watermarking app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__orig_img = None                # the original copy of the opened image file

        self.__file_manage_section = None     # UI section for managing image file
        self.__text_watermark_section = None  # UI section for controlling text watermark and its settings
        self.__image_canvases = None          # UI section for displaying image and watermarked image

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # FILE MANAGEMENT
        self.__file_manage_section = FileManageSection(
            self,
            bg=sett.SEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SEC_HL_COLOR,
        )

        # TEXT WATERMARKING
        self.__text_watermark_section = TextWatermarkSection(
            self,
            bg=sett.SEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SEC_HL_COLOR,
        )

        # IMAGE CANVASES
        self.__image_canvases = ImageCanvasesSection(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )

    def __config_commands(self):

        # FILE MANAGEMENT
        self.__file_manage_section.set_browse_btn_cmd(cmd=self.__browse_for_file)
        self.__file_manage_section.set_save_btn_cmd(cmd=self.__save_watermarked_image)

        # TEXT WATERMARK
        self.__text_watermark_section.set_update_watermark_btn_cmd(cmd=self.__update_canvas_images)

        # TEXT WATERMARK -> WATERMARK FONT SETTINGS
        self.__text_watermark_section.watermark_font_settings.set_font_size_scale_cmd(cmd=self.__update_canvas_images)
        self.__text_watermark_section.watermark_font_settings.set_alpha_scale_cmd(cmd=self.__update_canvas_images)
        self.__text_watermark_section.watermark_font_settings.set_radiobutton_cmd(cmd=self.__update_canvas_images)

        # TEXT WATERMARK -> WATERMARK POSITIONING
        self.__text_watermark_section.watermark_positioning.set_x_pos_scale_cmd(cmd=self.__update_canvas_images)
        self.__text_watermark_section.watermark_positioning.set_y_pos_scale_cmd(cmd=self.__update_canvas_images)

    def __place_widgets(self):

        # FILE MANAGEMENT
        self.__file_manage_section.grid(
            column=0,
            row=0,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )

        # TEXT WATERMARKING
        self.__text_watermark_section.grid(
            column=0,
            row=1,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )

        # IMAGE CANVASES
        self.__image_canvases.grid(
            column=3,
            row=0,
            rowspan=2,
            sticky="NESW"
        )

    def __browse_for_file(self):
        """
        Open a TK file dialog box to browse for a file. If one is selected, fills the browse entry and
        updates the canvas images
        """

        # open file browser
        filepath = tk.filedialog.askopenfilename(
            initialdir="./",
            title="Open Image",
            filetypes=sett.OPEN_FILETYPES,
        )

        if filepath:
            self.__file_manage_section.update_browse_entry(filepath)  # fill filepath entry

            self.__orig_img = Watermark.get_image(filepath)  # get ref to image

            self.__update_canvas_images()  # display image on canvases
            self.__text_watermark_section.watermark_positioning.update_position_scales(
                self.__orig_img
            )  # update pos sliders' X/Y max

    def __update_canvas_images(self, _=None):
        """
        Update the resized images on the canvases to reflect the current image
        :param _: Placeholder for any TK Events that may occur
        """

        if self.__orig_img:
            # get image resized
            resized_img = Watermark.resize_image(self.__orig_img, sett.CANVAS_WIDTH, sett.CANVAS_HEIGHT)

            # get RBG and Alpha values
            rgb = self.__text_watermark_section.watermark_font_settings.get_rgb_value()
            alpha = self.__text_watermark_section.watermark_font_settings.get_alpha_value()

            # get image watermarked and resized
            wm_img = Watermark.watermark_image(
                image=self.__orig_img,
                watermark=self.__text_watermark_section.get_watermark_entry_text(),
                font_size=self.__text_watermark_section.watermark_font_settings.get_font_size_value(),
                color=(rgb[0], rgb[1], rgb[2], alpha),
                pos=(self.__text_watermark_section.watermark_positioning.get_x_pos_value(),
                     self.__text_watermark_section.watermark_positioning.get_y_pos_value()),
            )
            resized_wm_img = Watermark.resize_image(wm_img, sett.CANVAS_WIDTH, sett.CANVAS_HEIGHT)

            # store photo images so garbage collector doesn't trash them
            self.__image_canvases.set_canvas_images(img_resized=resized_img, img_wm_resized=resized_wm_img)

    def __save_watermarked_image(self):
        """
        Opens a TK file dialog to save the watermarked image in its original size
        """

        if self.__orig_img:
            # open save file browser
            filepath = tk.filedialog.asksaveasfilename(
                initialdir="./",
                title="Save Image",
                filetypes=sett.SAVE_FILETYPES,
            )

            if filepath:
                self.__update_canvas_images()  # update canvas to reflect any final changes to watermark text

                # get RBG and Alpha values
                rgb = self.__text_watermark_section.watermark_font_settings.get_rgb_value()
                alpha = self.__text_watermark_section.watermark_font_settings.get_alpha_value()

                # save a watermarked copy of the image to the filepath gotten from the save filedialog
                Watermark.save_image(
                    Watermark.watermark_image(
                        image=self.__orig_img,
                        watermark=self.__text_watermark_section.get_watermark_entry_text(),
                        font_size=self.__text_watermark_section.watermark_font_settings.get_font_size_value(),
                        color=(rgb[0], rgb[1], rgb[2], alpha),
                        pos=(self.__text_watermark_section.watermark_positioning.get_x_pos_value(),
                             self.__text_watermark_section.watermark_positioning.get_y_pos_value()),
                    ),
                    filepath
                )
