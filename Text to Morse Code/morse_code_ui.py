"""
Text to Morse Code
file:   morse_code_ui.py
author: Joshua Jacobs
date:   4/17/2022
brief:  TKinter based User Interface to connect a CharToMorseCodeTranslator to.

"""
from tkinter import Tk, Label, Text, Scrollbar, Frame, Button, WORD, END, NONE
from char_to_morse_code import CharToMorseCodeTranslator, DIT, DAH
from winsound import Beep


class MorseCodeUI:
    """
    Interface used to give interaction between the User and the
    Morse Code program.
    """

    # CONSTANTS
    __TITLE_FONT = ("Arial", 36, "bold")
    __TITLE_MC_FONT = ("Arial", 18, "bold")
    __ENTRY_FONT = ("Arial", 16)
    __MORSE_CODE_FONT = ("Arial", 16, "bold")
    __BUTTON_FONT = ("Arial", 18, "bold")

    __MS_TIL_TRANSLATE = 200

    __BEEP_FREQ = 500
    __DIT_BEEP_LENGTH_MS = 120

    # CONSTRUCTOR
    def __init__(self, translator: CharToMorseCodeTranslator):
        # Translator
        self.__translator = translator
        self.__timer = None

        # Configure UI
        self.__window = self.__config_window()
        self.__config_title()
        self.__text_entry = self.__config_text_entry()
        self.__morse_code_output_text = self.__config_text_output()
        self.__play_button = self.__config_play_button()

        # Main Loop
        self.__window.after(self.__MS_TIL_TRANSLATE, self.__translate_text_in_box)
        self.__window.mainloop()

    # PRIVATE METHODS
    def __translate_text_in_box(self):
        translated_text = self.__translator.translate(self.__text_entry.get("1.0", END))
        self.__morse_code_output_text.delete("1.0", END)
        self.__morse_code_output_text.insert("1.0", translated_text)
        self.__window.after(self.__MS_TIL_TRANSLATE, self.__translate_text_in_box)

    def __toggle_play_stop(self):
        if self.__timer:
            self.__reset_on_player_stop()
        else:
            self.__text_entry.config(state="disabled")
            self.__morse_code_output_text.config(state="disabled")
            self.__play_button.config(text="Stop")
            self.__play_morse_code(0)

    def __reset_on_player_stop(self):
        self.__window.after_cancel(self.__timer)
        self.__timer = None
        self.__text_entry.config(state="normal")
        self.__morse_code_output_text.config(state="normal")
        self.__play_button.config(text="Play")

    def __play_morse_code(self, interval: int):
        morse_code_text = self.__morse_code_output_text.get("1.0", END)

        if interval < len(morse_code_text):
            if morse_code_text[interval] == DIT:
                Beep(self.__BEEP_FREQ, self.__DIT_BEEP_LENGTH_MS)
            elif morse_code_text[interval] == DAH:
                Beep(self.__BEEP_FREQ, self.__DIT_BEEP_LENGTH_MS * 3)
            self.__timer = self.__window.after(self.__DIT_BEEP_LENGTH_MS, self.__play_morse_code, interval + 1)
        else:
            self.__reset_on_player_stop()

    # APP UI CONFIG
    @staticmethod
    def __config_window():
        window = Tk()
        window.title("Text to Morse Code")
        window.config(
            padx=50,
            pady=20,
            bg="#CCCCCC"
        )

        return window

    def __config_title(self):
        # Base Title
        title_label = Label(
            text="Text to Morse Code",
            font=self.__TITLE_FONT,
        )
        title_label.grid(
            column=0,
            row=0
        )

        # Title in Morse Code
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

    def __config_text_entry(self):
        # Text Box
        text_entry = Text(
            width=50,
            height=5,
            wrap=WORD,
            font=self.__ENTRY_FONT
        )
        text_entry.insert("1.0", "Text to Morse Code")
        text_entry.focus()
        text_entry.grid(
            column=0,
            row=2,
            sticky="EW"
        )

        # Scrollbar
        text_entry_scrollbar = Scrollbar(
            command=text_entry.yview
        )
        text_entry_scrollbar.grid(
            column=1,
            row=2,
            sticky="NS"
        )
        text_entry.config(
            yscrollcommand=text_entry_scrollbar.set
        )

        return text_entry

    def __config_text_output(self):
        # Frame to hold Entry and Scrollbar
        output_frame = Frame()
        output_frame.grid(
            column=0,
            row=3,
            pady=20
        )

        # Text Box
        morse_code_output_text = Text(
            output_frame,
            width=55,
            height=1,
            font=self.__MORSE_CODE_FONT,
            bg="Black",
            fg="White",
            wrap=NONE
        )
        morse_code_output_text.grid(
            column=0,
            row=0,
            sticky="EW"
        )

        # Scrollbar
        morse_code_scrollbar = Scrollbar(
            output_frame,
            orient="horizontal",
            command=morse_code_output_text.xview
        )
        morse_code_scrollbar.grid(
            column=0,
            row=1,
            sticky="EW"
        )
        morse_code_output_text.config(
            xscrollcommand=morse_code_scrollbar.set
        )

        return morse_code_output_text

    def __config_play_button(self):
        play_button = Button(
            text="Play",
            command=self.__toggle_play_stop,
            font=self.__BUTTON_FONT,
            width=10
        )
        play_button.grid(
            column=0,
            row=4
        )

        return play_button
