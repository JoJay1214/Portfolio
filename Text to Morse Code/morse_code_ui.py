"""
Text to Morse Code
file:   morse_code_ui.py
author: Joshua Jacobs
date:   4/17/2022
brief:  TKinter based User Interface to connect a CharToMorseCodeTranslator to.

"""
import tkinter
from tkinter import Tk, Label, Text, Scrollbar, Frame, Entry, WORD, END, NONE
from char_to_morse_code import CharToMorseCodeTranslator


class MorseCodeUI:
    __TITLE_FONT = ("Arial", 36, "bold")
    __TITLE_MC_FONT = ("Arial", 18, "bold")
    __ENTRY_FONT = ("Arial", 16)
    __MORSE_CODE_FONT = ("Arial", 16, "bold")

    __MS_TIL_TRANSLATE = 100

    def __init__(self, translator: CharToMorseCodeTranslator):
        # Translator
        self.__translator = translator

        # Window
        self.__window = Tk()
        self.__window.title("Text to Morse Code")
        self.__window.config(
            padx=50,
            pady=20
        )

        # Title
        title_label = Label(
            text="Text to Morse Code",
            font=self.__TITLE_FONT,
        )
        title_label.grid(
            column=0,
            row=0
        )

        title_mc_label = Label(
            text=f"{self.__translator.translate('Text to')}\n"
                 f"{self.__translator.translate('Morse Code')}",
            font=self.__TITLE_MC_FONT,
        )
        title_mc_label.grid(
            column=0,
            row=1,
            pady=10
        )

        # Text Entry
        self.__text_entry = Text(
            width=50,
            height=5,
            wrap=WORD,
            font=self.__ENTRY_FONT
        )
        self.__text_entry.insert("1.0", "Text to Morse Code")
        self.__text_entry.focus()
        self.__text_entry.grid(
            column=0,
            row=2,
            sticky="EW"
        )

        text_entry_scrollbar = Scrollbar(
            command=self.__text_entry.yview
        )
        text_entry_scrollbar.grid(
            column=1,
            row=2,
            sticky="NS"
        )
        self.__text_entry.config(
            yscrollcommand=text_entry_scrollbar.set
        )

        # Text Output
        output_frame = Frame()
        output_frame.grid(
            column=0,
            row=3,
            pady=20
        )

        self.__morse_code_output_text = Text(
            output_frame,
            width=55,
            height=1,
            font=self.__MORSE_CODE_FONT,
            bg="Black",
            fg="White",
            wrap=NONE
        )
        self.__morse_code_output_text.grid(
            column=0,
            row=0,
            sticky="EW"
        )

        morse_code_scrollbar = Scrollbar(
            output_frame,
            orient="horizontal",
            command=self.__morse_code_output_text.xview
        )
        morse_code_scrollbar.grid(
            column=0,
            row=1,
            sticky="EW"
        )
        self.__morse_code_output_text.config(
            xscrollcommand=morse_code_scrollbar.set
        )

        # Run Window
        self.__window.after(self.__MS_TIL_TRANSLATE, self.translate_text_in_box)
        self.__window.mainloop()

    def translate_text_in_box(self):
        translated_text = self.__translator.translate(self.__text_entry.get("1.0", END))
        self.__morse_code_output_text.delete("1.0", END)
        self.__morse_code_output_text.insert("1.0", translated_text)
        self.__window.after(self.__MS_TIL_TRANSLATE, self.translate_text_in_box)
