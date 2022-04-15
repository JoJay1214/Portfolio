from tkinter import Tk, Label, Button, Entry, filedialog, END
from watermark import Watermark


class WatermarkInterface:
    def __init__(self, watermark: Watermark):
        self.__watermark = watermark

        self.__window = Tk()
        self.__window.title("Image Watermarking")
        self.__window.config(width=500, height=500, padx=20, pady=10)

        self.__watermark_label = Label(text="Text Watermark:")
        self.__watermark_label.pack()

        self.__watermark_entry = Entry()
        self.__watermark_entry.pack()

        self.__browse_label = Label(text="Image for Watermark:")
        self.__browse_label.pack()

        self.__browse_entry = Entry()
        self.__browse_entry.pack()

        self.__browse_button = Button(text="Browse", command=lambda: self.__browse_for_file(self.__browse_entry))
        self.__browse_button.pack()

        self.__submit_button = Button(text="Submit",
                                      command=lambda: self.__watermark.watermark_image(self.__browse_entry.get(),
                                                                                       self.__watermark_entry.get()))
        self.__submit_button.pack()

        self.__window.mainloop()

    @staticmethod
    def __browse_for_file(entry):
        filepath = filedialog.askopenfilename(initialdir="./", title="Select File",
                                              filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))

        if filepath:
            entry.delete(0, END)
            entry.insert(0, filepath)
