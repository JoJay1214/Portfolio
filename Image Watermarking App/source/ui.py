"""
Image Watermarking App
file:   ui.py
author: Joshua Jacobs
date:   3/11/2022
brief:  TKinter GUI to give interactivity between the user and the Watermark program.

"""
from tkinter import Tk, Canvas, Label, Button, Entry, filedialog, END
from source.watermark import Watermark
from PIL import ImageTk


class ImageWatermarkingUI:
    """
    TKinter GUI to give interactivity between the user and the Watermark program
    """

    """
    CONSTANTS
    """

    __CANVAS_WIDTH = 600
    __CANVAS_HEIGHT = 338

    """
    CONSTRUCTOR
    """

    def __init__(self, watermark: Watermark):
        """
        Image Watermarking app UI constructor
        :param watermark: Watermark instance for image watermarking logic
        """

        # Variables
        self.__watermark = watermark   # watermark functionality

        self.__window = Tk()           # app window

        self.__orig_img_canvas = None  # canvas that displays original image
        self.__wm_img_canvas = None    # canvas that displays the watermarked image
        self.__orig_img_item = None
        self.__wm_img_item = None

        self.__orig_img = None        # original Image
        self.__img_resized = None     # resized ImageTk for canvas
        self.__img_wm_resized = None  # resized watermarked ImageTk for canvas

        self.__watermark_entry = None  # watermark text entry
        self.__browse_entry = None     # file path text entry
        self.__browse_button = None    # button to browse files
        self.__submit_button = None    # button to submit image file path for watermarking

        # Create UI
        self.__config_window()
        self.__create_image_canvases()
        self.__create_text_watermark_section()
        self.__create_browse_file_section()
        self.__create_submit_section()

        self.__window.mainloop()

    """
    PRIVATE METHODS
    """

    def __browse_for_file(self):
        """
        Open a TK file dialog box to browse for a file. If one is selected, fills the browse entry
        """
        filepath = filedialog.askopenfilename(
            initialdir="./", title="Select File",
            filetypes=(("All Files", "*.*"), ("PNG Files", "*.png"))
        )

        if filepath:
            self.__browse_entry.config(state="normal")
            self.__browse_entry.delete(0, END)
            self.__browse_entry.insert(0, filepath)
            self.__browse_entry.config(state="disabled")

            self.__orig_img = self.__watermark.get_image(self.__browse_entry.get())
            self.__display_images()

    def __display_images(self):
        img = self.__orig_img

        resized_img = self.__watermark.resize_image(img, self.__CANVAS_WIDTH, self.__CANVAS_HEIGHT)

        wm_img = self.__watermark.watermark_image(img, self.__watermark_entry.get())
        resized_wm_img = self.__watermark.resize_image(wm_img, self.__CANVAS_WIDTH, self.__CANVAS_HEIGHT)

        self.__img_resized = ImageTk.PhotoImage(resized_img)
        self.__img_wm_resized = ImageTk.PhotoImage(resized_wm_img)

        self.__update_canvas_items()

    def __update_canvas_items(self):
        if self.__orig_img_item and self.__wm_img_item:
            self.__orig_img_canvas.itemconfig(
                self.__orig_img_item,
                image=self.__img_resized,
            )
            self.__wm_img_canvas.itemconfig(
                self.__wm_img_item,
                image=self.__img_wm_resized,
            )

        else:
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

    """
    UI CONFIG
    """

    def __config_window(self):
        """
        Create and configure TK GUI window
        """

        self.__window.title("Image Watermarking")
        self.__window.config(
            padx=20,
            pady=10,
        )

    def __create_image_canvases(self):
        self.__orig_img_canvas = Canvas(
            width=self.__CANVAS_WIDTH,
            height=self.__CANVAS_HEIGHT,
            bg="#000000"
        )
        self.__wm_img_canvas = Canvas(
            width=self.__CANVAS_WIDTH,
            height=self.__CANVAS_HEIGHT,
            bg="#000000"
        )

        self.__orig_img_canvas.grid(
            column=0,
            row=0,
            columnspan=3
        )
        self.__wm_img_canvas.grid(
            column=3,
            row=0,
            columnspan=3
        )

    def __create_text_watermark_section(self):
        """
        Create and configure the TK entry and label for the user inputted watermark text
        """

        watermark_label = Label(
            text="Text Watermark:",
        )
        self.__watermark_entry = Entry()

        watermark_label.grid(
            column=1,
            row=1,
            sticky="E",
        )
        self.__watermark_entry.grid(
            column=2,
            row=1,
            columnspan=2,
            sticky="EW",
        )

    def __create_browse_file_section(self):
        """
        Create and configure the TK Entry, Button, and Label used to browse for a file
        """

        browse_label = Label(
            text="Image for Watermark:"
        )
        self.__browse_entry = Entry(
            state="disabled"
        )
        self.__browse_button = Button(
            text="Browse",
            command=lambda: self.__browse_for_file()
        )

        browse_label.grid(
            column=1,
            row=2,
            sticky="E",
        )
        self.__browse_entry.grid(
            column=2,
            row=2,
            columnspan=2,
            sticky="EW",
        )
        self.__browse_button.grid(
            column=4,
            row=2,
            sticky="W",
        )

    def __create_submit_section(self):
        """
        Create and configure TK Button for submitting image file and watermark text
        """
        self.__submit_button = Button(
            text="Save Watermarked Copy",
            command=lambda: self.__watermark.save_image(
                self.__watermark.watermark_image(self.__orig_img, self.__watermark_entry.get()),
                self.__browse_entry.get()
            )
        )

        self.__submit_button.grid(
            column=2,
            row=3,
            columnspan=2,
        )
