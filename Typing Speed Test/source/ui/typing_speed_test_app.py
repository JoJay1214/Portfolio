"""
Typing Speed Test
file:   typing_speed_test_app.py
author: Joshua Jacobs
date:   7/5/2022
brief:  Main TKinter GUI for the Typing Speed Test app.

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.frames.title_frame import TitleFrame
from source.ui.frames.start_button_frame import StartButtonFrame
from source.ui.frames.score_display_frame import ScoreDisplayFrame
from source.ui.frames.time_display_frame import TimeDisplayFrame
from source.ui.frames.typing_test_frame import TypingTestFrame

from source.typing_speed_test import TypingSpeedTest


class TypingSpeedTestApp(tk.Frame):
    """
    Main TKinter GUI for the Typing Speed Test app
    """

    """
    CONSTANTS
    """

    TEST_LEN_SEC = 60  # test length in seconds

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        Constructor for the Frame that holds the Typing Speed Test app
        :param parent: The parent window
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent window

        # PRIVATE VARIABLES
        self.__title_frame = None                     # the app's title
        self.__start_button_frame = None              # start button to start/stop the test
        self.__score_display_frame = None             # displays the current score in the typing test
        self.__time_display_frame = None              # displays the current time left in the typing test
        self.__typing_test_frame = None               # displays current word and has entry for user interaction

        self.__typing_speed_test = TypingSpeedTest()  # the current typing speed test
        self.__timer = None                           # timer to reduce time in Time Display

        # CONFIG SELF
        self.__create_widgets()
        self.__config_widget_commands()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__title_frame = TitleFrame(
            self,
        )

        # START BUTTON
        self.__start_button_frame = StartButtonFrame(
            self,
        )

        # SCORE DISPLAY
        self.__score_display_frame = ScoreDisplayFrame(
            self,
        )

        # TIME DISPLAY
        self.__time_display_frame = TimeDisplayFrame(
            self,
        )

        # TYPING TEST
        self.__typing_test_frame = TypingTestFrame(
            self,
        )

    def __config_widget_commands(self):

        # START BUTTON
        self.__start_button_frame.set_start_button(btn_txt="Start Typing", btn_cmd=self.__start_test)

        # TYPING TEST
        self.__typing_test_frame.bind_text_entry(event="<Return>", handler=self.__input_typed_entry)

    def __place_widgets(self):

        # TITLE
        self.__title_frame.grid(
            column=0,
            row=0,
            columnspan=2,
            sticky="NESW",
        )

        # START BUTTON
        self.__start_button_frame.grid(
            column=0,
            row=1,
            columnspan=2,
            sticky="NESW",
        )

        # SCORE DISPLAY
        self.__score_display_frame.grid(
            column=0,
            row=2,
            sticky="NESW",
        )

        # TIME DISPLAY
        self.__time_display_frame.grid(
            column=1,
            row=2,
            sticky="NESW",
        )

        # TYPING TEST
        self.__typing_test_frame.grid(
            column=0,
            row=3,
            columnspan=2,
            sticky="NESW",
        )

    def __start_test(self):
        self.__typing_speed_test.restart_game()

        self.__get_new_word()
        self.__count_down(self.TEST_LEN_SEC)

        self.__start_button_frame.set_start_button(btn_txt="Cancel Test", btn_cmd=self.__cancel_test)
        self.__score_display_frame.set_score_label("0/0")
        self.__typing_test_frame.set_text_entry_state("normal")
        self.__typing_test_frame.focus_text_entry()

    def __cancel_test(self):
        self.__reset_ui()

    def __reset_ui(self):
        self.parent.after_cancel(self.__timer)
        self.__timer = None

        self.__start_button_frame.set_start_button(btn_txt="Start Typing", btn_cmd=self.__start_test)
        self.__time_display_frame.set_time_label("00")
        self.__typing_test_frame.set_word_label("word")
        self.__typing_test_frame.delete_text_entry()
        self.__typing_test_frame.set_text_entry_state("disabled")

    def __input_typed_entry(self, _=None):
        if self.__timer:
            self.__typing_speed_test.store_typed_word(self.__typing_test_frame.get_text_entry())
            self.__score_display_frame.set_score_label(self.__typing_speed_test.get_score_str())
            self.__get_new_word()

    def __get_new_word(self):
        self.__typing_test_frame.set_word_label(self.__typing_speed_test.get_word())
        self.__typing_test_frame.delete_text_entry()

    def __count_down(self, count: int):
        self.__time_display_frame.set_time_label(f"{count:02}")
        if count > 0:
            self.__timer = self.parent.after(1000, self.__count_down, count - 1)
        else:
            self.__reset_ui()
