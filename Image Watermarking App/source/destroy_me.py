"""
Image Watermarking App
file:   ui.py
author: Joshua Jacobs
date:   3/11/2022
brief:  TKinter GUI to give interactivity between the user and the Watermark program.

"""
from tkinter import Tk, Canvas, Frame, Label, Button, Entry, Scale, filedialog, END, HORIZONTAL
from PIL import ImageTk
from source.watermark import Watermark


class ImageWatermarkingUI:
    """
    TKinter GUI to give interactivity between the user and the Watermark program
    """

    # File Dialog Settings
    __OPEN_FILETYPES = [
        ("All Files", "*.*"),
    ]
    __SAVE_FILETYPES = [
        ("PNG Files", "*.png"),
    ]

    """
    CONSTRUCTOR
    """

    def __init__(self, watermark: Watermark):
        """
        Image Watermarking app UI constructor
        :param watermark: Watermark instance for image watermarking logic
        """

        # Variables
        self.__watermark = watermark  # watermark functionality
        self.__orig_img = None  # original Image

        self.__window = Tk()  # app window

        self.__orig_img_canvas = None  # canvas that displays original image
        self.__orig_img_item = None  # canvas item that holds resized original image

        self.__img_resized = None  # resized ImageTk for canvas

        self.__wm_img_canvas = None  # canvas that displays the watermarked image
        self.__wm_img_item = None  # canvas item that holds resized watermarked image

        self.__img_wm_resized = None  # resized watermarked ImageTk for canvas

        self.__watermark_entry = None  # watermark text entry

        self.__font_size_scale = None  # slider to adjust watermark font size
        self.__alpha_scale = None  # slider to adjust watermark transparency
        self.__x_pos_scale = None  # slider to adjust watermark horizontal position
        self.__y_pos_scale = None  # slider to adjust watermark vertical position

        # Create UI and run app
        self.__window.mainloop()

    """
    PRIVATE METHODS
    """

    def __browse_for_file(self):
        """
        Open a TK file dialog box to browse for a file. If one is selected, fills the browse entry and
        updates the canvas images
        """

        # open file browser
        filepath = filedialog.askopenfilename(
            initialdir="./",
            title="Open Image",
            filetypes=self.__OPEN_FILETYPES,
        )

        if filepath:
            self.__update_browse_entry(filepath)  # fill filepath entry

            # get ref to image
            self.__orig_img = self.__watermark.get_image(self.__browse_entry.get())
            self.__update_canvas_images()  # display image on canvases
            self.__update_position_scales()  # update pos sliders' X/Y max

    def __update_browse_entry(self, filepath: str):
        """
        Fill the browse entry with a given filepath string
        :param filepath: The path to the image file
        """

        self.__browse_entry.config(state="normal")
        self.__browse_entry.delete(0, END)
        self.__browse_entry.insert(0, filepath)
        self.__browse_entry.config(state="disabled")

    def __update_canvas_images(self, _=None):
        """
        Update the resized images on the canvases to shadow the current image
        :param _: Placeholder for any TK Events that may occur
        """

        if self.__orig_img:
            # get image resized
            resized_img = self.__watermark.resize_image(self.__orig_img, self.__CANVAS_WIDTH, self.__CANVAS_HEIGHT)

            # get image watermarked and resized
            wm_img = self.__watermark.watermark_image(
                image=self.__orig_img,
                watermark=self.__watermark_entry.get(),
                font_size=self.__font_size_scale.get(),
                color=(255, 255, 255, self.__alpha_scale.get()),
                pos=(self.__x_pos_scale.get(), self.__y_pos_scale.get()),
            )
            resized_wm_img = self.__watermark.resize_image(wm_img, self.__CANVAS_WIDTH, self.__CANVAS_HEIGHT)

            # store photo images so garbage collector doesn't trash them
            self.__img_resized = ImageTk.PhotoImage(resized_img)
            self.__img_wm_resized = ImageTk.PhotoImage(resized_wm_img)

            self.__update_canvas_items()

    def __update_position_scales(self):
        """
        Update the watermark text position scales' X/Y max to reflect the width and height of the current image
        """

        if self.__orig_img:
            # reset pos to (0, 0)
            self.__x_pos_scale.set(0)
            self.__y_pos_scale.set(0)

            # set scales' max to image width and height, respectively
            self.__x_pos_scale.config(
                to=self.__orig_img.width,
            )
            self.__y_pos_scale.config(
                to=self.__orig_img.height,
            )

    def __update_canvas_items(self):
        """
        Update the items on the canvases that hold the images. Creates them if they do not yet exist
        """

        if self.__orig_img_item and self.__wm_img_item:
            # configure canvas items if they exist
            self.__orig_img_canvas.itemconfig(
                self.__orig_img_item,
                image=self.__img_resized,
            )
            self.__wm_img_canvas.itemconfig(
                self.__wm_img_item,
                image=self.__img_wm_resized,
            )

        else:
            # create canvas items if they do not yet exist
            self.__orig_img_item = self.__orig_img_canvas.create_image(
                self.__CANVAS_WIDTH / 2,
                self.__CANVAS_HEIGHT / 2,
                anchor="center",
                image=self.__img_resized,
            )
            self.__wm_img_item = self.__wm_img_canvas.create_image(
                self.__CANVAS_WIDTH / 2,
                self.__CANVAS_HEIGHT / 2,
                anchor="center",
                image=self.__img_wm_resized,
            )

    def __save_watermarked_image(self):
        """
        Opens a TK file dialog to save the watermarked image in its original size
        """

        if self.__orig_img:
            # open save file browser
            filepath = filedialog.asksaveasfilename(
                initialdir="./",
                title="Select File",
                filetypes=self.__SAVE_FILETYPES,
            )

            if filepath:
                self.__update_canvas_images()  # update canvas to reflect any final changes to watermark text

                # save a watermarked copy of the image to the filepath gotten from the save filedialog
                self.__watermark.save_image(
                    self.__watermark.watermark_image(
                        image=self.__orig_img,
                        watermark=self.__watermark_entry.get(),
                        font_size=self.__font_size_scale.get(),
                        color=(255, 255, 255, self.__alpha_scale.get()),
                        pos=(self.__x_pos_scale.get(), self.__y_pos_scale.get()),
                    ),
                    filepath
                )
