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

    """
    CONSTANTS
    """

    # Widget Settings
    __WIN_START_POS = (0, 0)

    __CANVAS_WIDTH = 600  # width of the canvases the images sit on
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
    __COLOR_GREY = "#CCCCCC"
    __COLOR_DARK_GREY = "#AAAAAA"

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
        self.__watermark = watermark  # watermark functionality
        self.__orig_img = None  # original Image

        self.__window = Tk()  # app window

        self.__orig_img_canvas = None  # canvas that displays original image
        self.__orig_img_item = None  # canvas item that holds resized original image

        self.__img_resized = None  # resized ImageTk for canvas

        self.__wm_img_canvas = None  # canvas that displays the watermarked image
        self.__wm_img_item = None  # canvas item that holds resized watermarked image

        self.__img_wm_resized = None  # resized watermarked ImageTk for canvas

        self.__browse_entry = None  # file path text entry
        self.__watermark_entry = None  # watermark text entry

        self.__font_size_scale = None  # slider to adjust watermark font size
        self.__alpha_scale = None  # slider to adjust watermark transparency
        self.__x_pos_scale = None  # slider to adjust watermark horizontal position
        self.__y_pos_scale = None  # slider to adjust watermark vertical position

        # Create UI and run app
        self.__create_and_configure_ui()
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

    """
    UI CONFIG
    """
    def __create_and_configure_ui(self):
        """
        Organizational function to hold and execute the functions that build the UI
        """

        def __config_window():
            """
            Create and configure TK GUI window
            """

            self.__window.title("Image Watermarking")
            self.__window.config(
                bg=self.__COLOR_GREY,
                padx=self.__WIN_PAD_X,
                pady=self.__WIN_PAD_Y,
            )
            self.__window.geometry(f"+{self.__WIN_START_POS[0]}+{self.__WIN_START_POS[1]}")

        def __create_image_canvases():
            """
            Create and configure the TK canvases that will hold the images to display
            """

            self.__orig_img_canvas = Canvas(
                width=self.__CANVAS_WIDTH,
                height=self.__CANVAS_HEIGHT,
                bg=self.__COLOR_BLACK,
                highlightbackground=self.__COLOR_GREY,
            )
            self.__wm_img_canvas = Canvas(
                width=self.__CANVAS_WIDTH,
                height=self.__CANVAS_HEIGHT,
                bg=self.__COLOR_BLACK,
                highlightbackground=self.__COLOR_GREY,
            )

            self.__orig_img_canvas.grid(
                column=0,
                row=0,
                columnspan=3,
                padx=(0, 20),
            )
            self.__wm_img_canvas.grid(
                column=3,
                row=0,
                columnspan=3
            )

        def __create_browse_file_section():
            """
            Create and configure the TK Entry, Button, and Label used to browse for a file
            """

            browse_file_frame = Frame(bg=self.__COLOR_GREY)
            browse_file_frame.grid_columnconfigure(1, weight=1)

            browse_label = Label(
                browse_file_frame,
                text="Image for Watermark:",
                bg=self.__COLOR_GREY,
            )
            self.__browse_entry = Entry(
                browse_file_frame,
                state="disabled"
            )
            __browse_button = Button(
                browse_file_frame,
                text="Browse",
                command=self.__browse_for_file,
                width=20,
                bg=self.__COLOR_GREY,
            )

            browse_file_frame.grid(
                column=0,
                row=1,
                columnspan=3,
                sticky="EW",
                padx=(0, 20),
            )

            browse_label.grid(
                column=0,
                row=0,
                sticky="W",
                padx=(0, 10),
            )
            self.__browse_entry.grid(
                column=1,
                row=0,
                sticky="EW",
            )
            __browse_button.grid(
                column=2,
                row=0,
                padx=(10, 0),
            )

        def __create_text_watermark_section():
            """
            Create and configure the TK label, entry, and button for inputting and updating the watermark
            """

            watermark_text_frame = Frame(bg=self.__COLOR_GREY)
            watermark_text_frame.grid_columnconfigure(1, weight=1)

            watermark_label = Label(
                watermark_text_frame,
                text="Text Watermark:",
                bg=self.__COLOR_GREY,
            )
            self.__watermark_entry = Entry(
                watermark_text_frame,
            )
            watermark_button = Button(
                watermark_text_frame,
                text="Update Watermark",
                command=self.__update_canvas_images,
                width=20,
                bg=self.__COLOR_GREY,
            )

            watermark_text_frame.grid(
                column=0,
                row=2,
                columnspan=3,
                sticky="EW",
                padx=(0, 20),
            )

            watermark_label.grid(
                column=0,
                row=0,
                sticky="W",
                padx=(0, 38),
            )
            self.__watermark_entry.grid(
                column=1,
                row=0,
                sticky="EW",
            )
            watermark_button.grid(
                column=2,
                row=0,
                sticky="E",
                padx=(10, 0),
            )

        def __create_save_btn_section():
            """
            Create and configure TK Button for saving watermarked image
            """

            __save_button = Button(
                text="Save Watermarked Copy",
                command=self.__save_watermarked_image,
                bg=self.__COLOR_GREY,
            )

            __save_button.grid(
                column=1,
                row=4,
                columnspan=1,
            )

        def __create_watermark_settings_section():
            """
            Create and configure TK Scales and Labels for adjusting watermark font settings
            """

            # create widgets
            watermark_settings_frame = Frame(bg=self.__COLOR_GREY)
            watermark_settings_frame.grid_columnconfigure(1, weight=1)

            font_size_label = Label(
                watermark_settings_frame,
                text="Font Size:",
                bg=self.__COLOR_GREY,
            )
            self.__font_size_scale = Scale(
                watermark_settings_frame,
                from_=1,
                to=200,
                orient=HORIZONTAL,
                command=self.__update_canvas_images,
                bg=self.__COLOR_GREY,
                highlightbackground=self.__COLOR_GREY,
                troughcolor=self.__COLOR_DARK_GREY,
            )

            font_alpha_label = Label(
                watermark_settings_frame,
                text="Alpha:",
                bg=self.__COLOR_GREY,
            )
            self.__alpha_scale = Scale(
                watermark_settings_frame,
                from_=0,
                to=255,
                orient=HORIZONTAL,
                command=self.__update_canvas_images,
                bg=self.__COLOR_GREY,
                highlightbackground=self.__COLOR_GREY,
                troughcolor=self.__COLOR_DARK_GREY,
            )

            # set scale defaults
            self.__font_size_scale.set(50)
            self.__alpha_scale.set(255)

            # place widgets
            watermark_settings_frame.grid(
                column=3,
                row=1,
                columnspan=3,
                sticky="EW",
            )

            font_size_label.grid(
                column=0,
                row=0,
                sticky="SW",
                padx=(0, 10),
            )
            self.__font_size_scale.grid(
                column=1,
                row=0,
                columnspan=2,
                sticky="EW"
            )

            font_alpha_label.grid(
                column=0,
                row=1,
                sticky="SW",
                padx=(0, 10),
            )
            self.__alpha_scale.grid(
                column=1,
                row=1,
                columnspan=2,
                sticky="EW",
            )

        def __create_watermark_position_section():
            """
            Create and configure TK Scales and Labels for adjusting watermark text position
            """

            # create widgets
            watermark_position_frame = Frame(bg=self.__COLOR_GREY)
            watermark_position_frame.grid_columnconfigure(1, weight=1)

            x_pos_label = Label(
                watermark_position_frame,
                text="Horizontal Position:",
                bg=self.__COLOR_GREY,
            )
            self.__x_pos_scale = Scale(
                watermark_position_frame,
                from_=0,
                to=0,
                orient=HORIZONTAL,
                command=self.__update_canvas_images,
                bg=self.__COLOR_GREY,
                highlightbackground=self.__COLOR_GREY,
                troughcolor=self.__COLOR_DARK_GREY,
            )

            y_pos_label = Label(
                watermark_position_frame,
                text="Vertical Position:",
                bg=self.__COLOR_GREY,
            )
            self.__y_pos_scale = Scale(
                watermark_position_frame,
                from_=0,
                to=0,
                orient=HORIZONTAL,
                command=self.__update_canvas_images,
                bg=self.__COLOR_GREY,
                highlightbackground=self.__COLOR_GREY,
                troughcolor=self.__COLOR_DARK_GREY,
            )

            # set scale defaults
            self.__x_pos_scale.set(0)
            self.__y_pos_scale.set(0)

            # place widgets
            watermark_position_frame.grid(
                column=3,
                row=2,
                columnspan=3,
                sticky="EW",
            )

            x_pos_label.grid(
                column=0,
                row=0,
                sticky="SW",
                padx=(0, 10),
            )
            self.__x_pos_scale.grid(
                column=1,
                row=0,
                columnspan=2,
                sticky="EW"
            )

            y_pos_label.grid(
                column=0,
                row=1,
                sticky="SW",
                padx=(0, 10),
            )
            self.__y_pos_scale.grid(
                column=1,
                row=1,
                columnspan=2,
                sticky="EW",
            )

        __config_window()
        __create_image_canvases()
        __create_browse_file_section()
        __create_text_watermark_section()
        __create_save_btn_section()
        __create_watermark_settings_section()
        __create_watermark_position_section()
