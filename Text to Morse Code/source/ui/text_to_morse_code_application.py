"""
Text to Morse Code App
file:   text_to_morse_code_application.py
author: Joshua Jacobs
date:   6/23/2022
brief:  Main TKinter GUI for Text to Morse Code App.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk
from winsound import PlaySound, SND_FILENAME

# PROJECT IMPORTS
from source.ui.frames.title_frame import TitleFrame
from source.ui.frames.input_textbox_frame import InputTextboxFrame
from source.ui.frames.output_textbox_frame import OutputTextboxFrame
from source.ui.frames.play_button_frame import PlayButtonFrame

from source.char_to_morse_code import CharToMorseCodeTranslator, DIT, DAH

import source.app_settings as sett


class TextToMorseCodeApplication(tk.Frame):
    """
    Main TKinter GUI for Text to Morse Code App
    """

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        Constructor for the Text to Morse Code app
        :param parent: The parent container
        :param args: Argument list
        :param kwargs: Keyword argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__title_frame = None           # holds the app title section
        self.__input_textbox_frame = None   # holds the input entry textbox section
        self.__output_textbox_frame = None  # holds the output textbox section
        self.__play_button_frame = None     # holds the play button section

        self.__timer = None                 # timer to start/stop morse code audio output

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

        self.parent.after(sett.MS_TIL_TRANSLATE, self.__translate_text_in_box)

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__title_frame = TitleFrame(
            self,
            highlightthickness=sett.FRAME_HIGHLIGHT_THICKNESS,
            highlightbackground=sett.FRAME_HIGHLIGHT_COLOR,
        )

        # INPUT TEXTBOX
        self.__input_textbox_frame = InputTextboxFrame(
            self,
            highlightthickness=sett.FRAME_HIGHLIGHT_THICKNESS,
            highlightbackground=sett.FRAME_HIGHLIGHT_COLOR,
        )

        # OUTPUT TEXTBOX
        self.__output_textbox_frame = OutputTextboxFrame(
            self,
            highlightthickness=sett.FRAME_HIGHLIGHT_THICKNESS,
            highlightbackground=sett.FRAME_HIGHLIGHT_COLOR,
        )

        # PLAY BUTTON
        self.__play_button_frame = PlayButtonFrame(
            self,
            highlightthickness=sett.FRAME_HIGHLIGHT_THICKNESS,
            highlightbackground=sett.FRAME_HIGHLIGHT_COLOR,
        )

    def __config_commands(self):

        # PLAY BUTTON
        self.__play_button_frame.set_play_button_command(
            cmd=self.__toggle_play_stop,
        )

    def __place_widgets(self):

        # TITLE
        self.__title_frame.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # INPUT TEXTBOX
        self.__input_textbox_frame.grid(
            column=0,
            row=1,
            sticky="EW",
        )

        # OUTPUT TEXTBOX
        self.__output_textbox_frame.grid(
            column=0,
            row=2,
            sticky="EW",
        )

        # PLAY BUTTON
        self.__play_button_frame.grid(
            column=0,
            row=3,
            sticky="NESW",
        )

    def __translate_text_in_box(self):
        """
        Translate the text in the input textbox and output it into the output textbox
        """

        # get input text
        translated_text = CharToMorseCodeTranslator.translate(self.__input_textbox_frame.get_input_text())

        # set output text
        self.__output_textbox_frame.set_output_text(translated_text)

        self.parent.after(sett.MS_TIL_TRANSLATE, self.__translate_text_in_box)  # run translate after wait time

    def __toggle_play_stop(self):
        """
        Play or Stop the Morse Code audio output
        """

        if self.__timer:  # if playing, stop
            self.__reset_on_player_stop()

        else:  # if not playing, start
            # disable text box
            self.__input_textbox_frame.disable_input_textbox()

            self.__play_button_frame.set_play_button_text(text="Stop")
            self.__play_morse_code(0)  # start playing the Morse Code audio

    def __reset_on_player_stop(self):
        """
        Reset interface to original state
        """

        # cancel current timer
        self.parent.after_cancel(self.__timer)
        self.__timer = None

        # enable text box
        self.__input_textbox_frame.enable_input_textbox()

        self.__play_button_frame.set_play_button_text(text="Play")

    def __play_morse_code(self, interval: int):
        """
        Play a morse code sound given the morse code output and the current interval.
        Ready the program for the next sound to be played and reset the player if there 
        are no more sounds to be played.
        :param interval: The current morse code sound to be played.
        """
        
        morse_code_text = self.__output_textbox_frame.get_output_text()  # get outputted Morse Code text

        # if there's morse code left to be played, keep playing
        if interval < len(morse_code_text):
            if morse_code_text[interval] == DIT:  # play Dit sound
                PlaySound("sounds/dit.wav", SND_FILENAME)

            elif morse_code_text[interval] == DAH:  # play Dah sound
                PlaySound("sounds/dah.wav", SND_FILENAME)

            # after morse code time interval has passed, play next character
            # with the delay, spaces will come out as pauses between Dits/Dahs
            self.__timer = self.parent.after(sett.MC_TIME_INTERVAL_MS, self.__play_morse_code, interval + 1)

        else:  # stop playing and reset interface
            self.__reset_on_player_stop()
