"""
Image Watermarking App
file:   image_watermarking_application.py
author: Joshua Jacobs
date:   6/6/2022
brief:  Main TKinter GUI for Image Watermarking App.

"""
import tkinter as tk
from tkinter import filedialog

from source.file_manage_section import FileManageSection
from source.image_canvases import ImageCanvases
from source.text_watermark_section import TextWatermarkSection
from source.watermark import Watermark

import source.app_settings as sett


class ImageWatermarkingApplication(tk.Frame):
    """
    Main TKinter GUI for Image Watermarking App
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.orig_img = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # create sections
        self.file_manage_section = FileManageSection(
            self,
            bg=sett.SEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SEC_HL_COLOR,
        )
        self.text_watermark_section = TextWatermarkSection(
            self,
            bg=sett.SEC_BG_COLOR,
            highlightthickness=sett.SEC_HL_THICKNESS,
            highlightbackground=sett.SEC_HL_COLOR,
        )
        self.image_canvases = ImageCanvases(
            self,
            bg=sett.PRIMARY_APP_COLOR,
        )

        # configure commands
        self.file_manage_section.browse_button.config(
            command=self.browse_for_file,
        )
        self.file_manage_section.save_button.config(
            command=self.save_watermarked_image,
        )

        self.text_watermark_section.watermark_button.config(
            command=self.update_canvas_images,
        )

        self.text_watermark_section.watermark_settings.font_size_scale.config(
            command=self.update_canvas_images,
        )
        self.text_watermark_section.watermark_settings.alpha_scale.config(
            command=self.update_canvas_images,
        )

        self.text_watermark_section.watermark_positioning.x_pos_scale.config(
            command=self.update_canvas_images,
        )
        self.text_watermark_section.watermark_positioning.y_pos_scale.config(
            command=self.update_canvas_images,
        )

        # place sections
        self.file_manage_section.grid(
            column=0,
            row=0,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )
        self.text_watermark_section.grid(
            column=0,
            row=1,
            sticky="NESW",
            padx=sett.SEC_OUTER_PAD,
            pady=sett.SEC_OUTER_PAD,
        )
        self.image_canvases.grid(
            column=3,
            row=0,
            rowspan=2,
            sticky="NESW"
        )

    def browse_for_file(self):
        """
        Open a TK file dialog box to browse for a file. If one is selected, fills the browse entry and
        updates the canvas images
        """

        # open file browser, ignore PyCharm highlighting bug
        filepath = tk.filedialog.askopenfilename(
            initialdir="./",
            title="Open Image",
            filetypes=sett.OPEN_FILETYPES,
        )

        if filepath:
            self.file_manage_section.update_browse_entry(filepath)  # fill filepath entry

            # get ref to image
            self.orig_img = Watermark.get_image(filepath)
            self.update_canvas_images()  # display image on canvases
            self.text_watermark_section.watermark_positioning.update_position_scales(
                self.orig_img
            )  # update pos sliders' X/Y max

    def update_canvas_images(self, _=None):
        """
        Update the resized images on the canvases to shadow the current image
        :param _: Placeholder for any TK Events that may occur
        """

        if self.orig_img:
            # get image resized
            resized_img = Watermark.resize_image(self.orig_img, sett.CANVAS_WIDTH, sett.CANVAS_HEIGHT)

            # get image watermarked and resized
            wm_img = Watermark.watermark_image(
                image=self.orig_img,
                watermark=self.text_watermark_section.watermark_entry.get(),
                font_size=self.text_watermark_section.watermark_settings.font_size_scale.get(),
                color=(255, 255, 255, self.text_watermark_section.watermark_settings.alpha_scale.get()),
                pos=(self.text_watermark_section.watermark_positioning.x_pos_scale.get(),
                     self.text_watermark_section.watermark_positioning.y_pos_scale.get()),
            )
            resized_wm_img = Watermark.resize_image(wm_img, sett.CANVAS_WIDTH, sett.CANVAS_HEIGHT)

            # store photo images so garbage collector doesn't trash them
            self.image_canvases.set_canvas_images(img_resized=resized_img, img_wm_resized=resized_wm_img)

    def save_watermarked_image(self):
        """
        Opens a TK file dialog to save the watermarked image in its original size
        """

        if self.orig_img:
            # open save file browser, ignore PyCharm highlighting bug
            filepath = tk.filedialog.asksaveasfilename(
                initialdir="./",
                title="Select File",
                filetypes=sett.SAVE_FILETYPES,
            )

            if filepath:
                self.update_canvas_images()  # update canvas to reflect any final changes to watermark text

                # save a watermarked copy of the image to the filepath gotten from the save filedialog
                Watermark.save_image(
                    Watermark.watermark_image(
                        image=self.orig_img,
                        watermark=self.text_watermark_section.watermark_entry.get(),
                        font_size=self.text_watermark_section.watermark_settings.font_size_scale.get(),
                        color=(255, 255, 255, self.text_watermark_section.watermark_settings.alpha_scale.get()),
                        pos=(self.text_watermark_section.watermark_positioning.x_pos_scale.get(),
                             self.text_watermark_section.watermark_positioning.y_pos_scale.get()),
                    ),
                    filepath
                )
