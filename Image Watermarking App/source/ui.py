"""
Image Watermarking App
file:   ui.py
author: Joshua Jacobs
date:   3/11/2022
brief:  TKinter GUI to give interactivity between the user and the Watermark program.

"""
from tkinter import Tk, Label, Button, Entry, filedialog, END
from source.watermark import Watermark


class ImageWatermarkingUI:
    """
    TKinter GUI to give interactivity between the user and the Watermark program
    """

    """
    CONSTRUCTOR
    """
    def __init__(self, watermark: Watermark):
        """
        Image Watermarking app UI constructor
        :param watermark: Watermark instance for image watermarking logic
        """

        self.__watermark = watermark   # watermark functionality

        self.__window = Tk()           # app window
        self.__watermark_entry = None  # watermark text entry
        self.__browse_entry = None     # file path text entry
        self.__browse_button = None    # button to browse files
        self.__submit_button = None    # button to submit image file path for watermarking

        # Create UI
        self.__config_window()
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
            self.__browse_entry.delete(0, END)
            self.__browse_entry.insert(0, filepath)

    """
    UI CONFIG
    """

    def __config_window(self):
        """
        Create and configure TK GUI window
        """

        self.__window.title("Image Watermarking")
        self.__window.config(
            width=500,
            height=500,
            padx=20,
            pady=10,
        )

    def __create_text_watermark_section(self):
        """
        Create and configure the TK entry and label for the user inputted watermark text
        """

        watermark_label = Label(
            text="Text Watermark:"
        )
        self.__watermark_entry = Entry()

        watermark_label.grid(
            column=0,
            row=0,
        )
        self.__watermark_entry.grid(
            column=1,
            row=0,
        )

    def __create_browse_file_section(self):
        """
        Create and configure the TK Entry, Button, and Label used to browse for a file
        """

        browse_label = Label(
            text="Image for Watermark:"
        )
        self.__browse_entry = Entry()
        self.__browse_button = Button(
            text="Browse",
            command=lambda: self.__browse_for_file()
        )

        browse_label.grid(
            column=0,
            row=1,
        )
        self.__browse_entry.grid(
            column=1,
            row=1,
        )
        self.__browse_button.grid(
            column=2,
            row=1,
        )

    def __create_submit_section(self):
        """
        Create and configure TK Button for submitting image file and watermark text
        """
        self.__submit_button = Button(
            text="Submit",
            command=lambda: self.__watermark.watermark_image(self.__browse_entry.get(), self.__watermark_entry.get())
        )

        self.__submit_button.grid(
            column=1,
            row=2,
        )
