"""
Text to Morse Code
file:   morse_code_ui.py
author: Joshua Jacobs
date:   4/17/2022
brief:  TKinter based User Interface to connect a CharToMorseCodeTranslator to.

"""
from source.char_to_morse_code import CharToMorseCodeTranslator, DIT, DAH
from tkinter import Tk, Label, Text, Scrollbar, Frame, Button, WORD, END, NONE
from winsound import PlaySound, SND_FILENAME


class MorseCodeUI:
    """
    Interface used to give interaction between the User and the
    Morse Code program.
    """

    """
    CONSTANTS
    """
    # Program Control
    __MS_TIL_TRANSLATE = 200  # time to wait between translation updates
    __MC_TIME_INTERVAL_MS = 100  # time interval for morse code audio output

    # Fonts
    __MORSE_CODE_FONT = ("Arial", 16, "bold")
    __BUTTON_FONT = ("Arial", 18, "bold")

    # UI Widget Settings

    __PLAY_BUTTON_WIDTH = 10

    """
    CONSTRUCTOR
    """

    def __init__(self, translator: CharToMorseCodeTranslator):
        # Translator
        self.__translator = translator  # text to morse code translator
        self.__timer = None  # timer to start/stop morse code audio output

        # Configure UI
        self.__morse_code_output_textbox = self.__config_text_output()  # morse code text output Text obj
        self.__play_button = self.__config_play_button()  # morse code play button Button obj

        # Main Loop

        # translate text in input textbox after a specific amount of time
        self.__window.after(self.__MS_TIL_TRANSLATE, self.__translate_text_in_box)

    """
    PRIVATE METHODS
    """

    def __translate_text_in_box(self):
        """
        Translate the text in the input textbox and output it into the output textbox
        """

        # get input text
        translated_text = self.__translator.translate(self.__input_textbox.get("1.0", END))

        self.__morse_code_output_textbox.config(state="normal")
        self.__morse_code_output_textbox.delete("1.0", END)  # delete old text in output box
        self.__morse_code_output_textbox.insert("1.0", translated_text)  # insert new text into output box
        self.__morse_code_output_textbox.config(state="disabled")

        self.__window.after(self.__MS_TIL_TRANSLATE, self.__translate_text_in_box)  # run translate after wait time

    def __toggle_play_stop(self):
        """
        Play or Stop the Morse Code audio output
        """

        if self.__timer:  # if playing, stop
            self.__reset_on_player_stop()

        else:  # if not playing, start
            # disable text box
            self.__input_textbox.config(state="disabled")

            self.__play_button.config(text="Stop")
            self.__play_morse_code(0)  # start playing the Morse Code audio

    def __reset_on_player_stop(self):
        """
        Reset interface to original state
        """

        # cancel current timer
        self.__window.after_cancel(self.__timer)
        self.__timer = None

        # enable text box
        self.__input_textbox.config(state="normal")

        self.__play_button.config(text="Play")

    def __play_morse_code(self, interval: int):
        morse_code_text = self.__morse_code_output_textbox.get("1.0", END)  # get outputted Morse Code text

        # if there's morse code left to be played, keep playing
        if interval < len(morse_code_text):
            if morse_code_text[interval] == DIT:  # play Dit sound
                PlaySound("sounds/dit.wav", SND_FILENAME)

            elif morse_code_text[interval] == DAH:  # play Dah sound
                PlaySound("sounds/dah.wav", SND_FILENAME)

            # after morse code time interval has passed, play next character
            # with the delay, spaces will come out as pauses between Dits/Dahs
            self.__timer = self.__window.after(self.__MC_TIME_INTERVAL_MS, self.__play_morse_code, interval + 1)

        else:  # stop playing and reset interface
            self.__reset_on_player_stop()

    """
    APP UI CONFIG
    """

    def __config_text_output(self) -> Text:
        """
        Create and configure the Text box for morse code output
        :return: The created Text box
        """

        # Frame to hold Entry and Scrollbar
        output_frame = Frame()
        output_frame.grid(
            column=0,
            row=3,
            pady=self.__OUTPUT_FRAME_PADY,
        )



        return morse_code_output_text

    def __config_play_button(self) -> Button:
        """
        Create and configure Button to click to play morse code audio
        :return: The created Button
        """

        play_button = Button(
            command=self.__toggle_play_stop,
            font=self.__BUTTON_FONT,
            text="Play",
            width=self.__PLAY_BUTTON_WIDTH,
        )
        play_button.grid(
            column=0,
            row=4
        )

        return play_button
