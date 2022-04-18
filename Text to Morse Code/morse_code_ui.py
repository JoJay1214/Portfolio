"""
Text to Morse Code
file:   morse_code_ui.py
author: Joshua Jacobs
date:   4/17/2022
brief:  TKinter based User Interface to connect a CharToMorseCodeTranslator to.

"""

from tkinter import Tk, Label, Text, WORD, END
from char_to_morse_code import CharToMorseCodeTranslator


class MorseCodeUI:
    __TITLE_FONT = ("Arial", 32, "bold")
    __TITLE_MC_FONT = ("Arial", 20, "bold")

    __MS_TIL_TRANSLATE = 500

    def __init__(self, translator: CharToMorseCodeTranslator):
        self.__translator = translator

        self.__window = Tk()
        self.__window.title("Text to Morse Code")
        self.__window.config(padx=50)

        __title_label = Label(
            text="Text to Morse Code",
            font=self.__TITLE_FONT,
        )
        __title_label.grid(column=0, row=0)

        __title_mc_label = Label(
            text=f"{self.__translator.translate('Text to')}\n"
                 f"{self.__translator.translate('Morse')}\n"
                 f"{self.__translator.translate('Code')}",
            font=self.__TITLE_MC_FONT,
        )
        __title_mc_label.grid(column=0, row=1)

        self.__text_entry = Text(
            width=50,
            height=5,
            wrap=WORD,
        )
        self.__text_entry.focus()
        self.__text_entry.grid(column=0, row=2)

        self.__morse_code_output_label = Label(
            text="",
            pady=32,
            wraplength=400
        )
        self.__morse_code_output_label.grid(column=0, row=3)

        self.__window.after(self.__MS_TIL_TRANSLATE, self.translate_text_in_box)
        self.__window.mainloop()

    def translate_text_in_box(self):
        translated_text = self.__translator.translate(self.__text_entry.get("1.0", END))
        self.__morse_code_output_label.config(text=translated_text)
        self.__window.after(self.__MS_TIL_TRANSLATE, self.translate_text_in_box)
