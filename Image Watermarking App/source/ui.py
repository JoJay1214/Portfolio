"""
Image Watermarking App
file:   ui.py
author: Joshua Jacobs
date:   3/11/2022
brief:  TKinter GUI to give interactivity between the user and the Watermark program.

"""
from tkinter import Tk, Canvas, Label, Button, Entry, filedialog, END
from PIL import ImageTk
from source.watermark import Watermark


class ImageWatermarkingUI:
    """
    TKinter GUI to give interactivity between the user and the Watermark program
    """

    """
    CONSTANTS
    """

    # Widget Settings
    __CANVAS_WIDTH = 600   # width of the canvases the images sit on
    __CANVAS_HEIGHT = 338  # height of the canvases the images sit on

    # File Dialog Settings
    __OPEN_FILETYPES = [
        ("All Files", "*.*"),
    ]
    __SAVE_FILETYPES = [
        ("PNG Files", "*.png"),
    ]

    # Color
    __COLOR_BLACK = "#000000"

    # Padding
    __WIN_PAD_X = 20
    __WIN_PAD_Y = 10

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
        self.__orig_img = None         # original Image

        self.__window = Tk()           # app window

        self.__orig_img_canvas = None  # canvas that displays original image
        self.__orig_img_item = None    # canvas item that holds resized original image
        self.__img_resized = None      # resized ImageTk for canvas

        self.__wm_img_canvas = None    # canvas that displays the watermarked image
        self.__wm_img_item = None      # canvas item that holds resized watermarked image
        self.__img_wm_resized = None   # resized watermarked ImageTk for canvas

        self.__browse_entry = None     # file path text entry
        self.__watermark_entry = None  # watermark text entry

        # Create UI
        self.__config_window()
        self.__create_image_canvases()
        self.__create_browse_file_section()
        self.__create_text_watermark_section()
        self.__create_save_btn_section()

        self.__window.mainloop()

    """
    PRIVATE METHODS
    """

    def __browse_for_file(self):
        """
        Open a TK file dialog box to browse for a file. If one is selected, fills the browse entry and
        updates the canvas images
        """

        filepath = filedialog.askopenfilename(
            initialdir="./",
            title="Open Image",
            filetypes=self.__OPEN_FILETYPES,
        )

        if filepath:
            self.__update_browse_entry(filepath)

            self.__orig_img = self.__watermark.get_image(self.__browse_entry.get())
            self.__update_canvas_images()

    def __update_browse_entry(self, filepath: str):
        """
        Fill the browse entry with a given filepath string
        :param filepath: The path to the image file
        """

        self.__browse_entry.config(state="normal")
        self.__browse_entry.delete(0, END)
        self.__browse_entry.insert(0, filepath)
        self.__browse_entry.config(state="disabled")

    def __update_canvas_images(self):
        """
        Update the resized images on the canvases to shadow the current image
        """

        if self.__orig_img:
            resized_img = self.__watermark.resize_image(self.__orig_img, self.__CANVAS_WIDTH, self.__CANVAS_HEIGHT)

            wm_img = self.__watermark.watermark_image(self.__orig_img, self.__watermark_entry.get())
            resized_wm_img = self.__watermark.resize_image(wm_img, self.__CANVAS_WIDTH, self.__CANVAS_HEIGHT)

            self.__img_resized = ImageTk.PhotoImage(resized_img)
            self.__img_wm_resized = ImageTk.PhotoImage(resized_wm_img)

            self.__update_canvas_items()

    def __update_canvas_items(self):
        """
        Update the items on the canvases that hold the images. Creates them if they do not yet exist
        """

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

    def __save_watermarked_image(self):
        """
        Opens a TK file dialog to save the watermarked image in its original size
        """

        if self.__orig_img:
            filepath = filedialog.asksaveasfilename(
                initialdir="./",
                title="Select File",
                filetypes=self.__SAVE_FILETYPES,
            )

            if filepath:
                self.__update_canvas_images()
                self.__watermark.save_image(
                    self.__watermark.watermark_image(self.__orig_img, self.__watermark_entry.get()),
                    filepath
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
            padx=self.__WIN_PAD_X,
            pady=self.__WIN_PAD_Y,
        )

    def __create_image_canvases(self):
        """
        Create and configure the TK canvases that will hold the images to display
        """

        self.__orig_img_canvas = Canvas(
            width=self.__CANVAS_WIDTH,
            height=self.__CANVAS_HEIGHT,
            bg=self.__COLOR_BLACK
        )
        self.__wm_img_canvas = Canvas(
            width=self.__CANVAS_WIDTH,
            height=self.__CANVAS_HEIGHT,
            bg=self.__COLOR_BLACK
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
        __browse_button = Button(
            text="Browse",
            command=self.__browse_for_file
        )

        browse_label.grid(
            column=1,
            row=1,
            sticky="E",
        )
        self.__browse_entry.grid(
            column=2,
            row=1,
            columnspan=2,
            sticky="EW",
        )
        __browse_button.grid(
            column=4,
            row=1,
            sticky="EW",
        )

    def __create_text_watermark_section(self):
        """
        Create and configure the TK label, entry, and button for inputting and updating the watermark
        """

        watermark_label = Label(
            text="Text Watermark:",
        )
        self.__watermark_entry = Entry(
        )
        watermark_button = Button(
            text="Update Watermark",
            command=self.__update_canvas_images
        )

        watermark_label.grid(
            column=1,
            row=2,
            sticky="E",
        )
        self.__watermark_entry.grid(
            column=2,
            row=2,
            columnspan=2,
            sticky="EW",
        )
        watermark_button.grid(
            column=4,
            row=2,
            sticky="EW",
        )

    def __create_save_btn_section(self):
        """
        Create and configure TK Button for saving watermarked image
        """

        __save_button = Button(
            text="Save Watermarked Copy",
            command=self.__save_watermarked_image,
        )

        __save_button.grid(
            column=2,
            row=3,
            columnspan=2,
        )
