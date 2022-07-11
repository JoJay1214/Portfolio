from tkinter import Tk, Label, Button, Entry, END
from typing_speed_test import TypingSpeedTest, TEST_LEN_SEC


class TypingSpeedTestUI:
    def __init__(self, tst: TypingSpeedTest):
        self.__timer = None

    def __start_test(self):
        self.__tst.restart_game()
        self.__get_new_word()
        self.__typing_entry.focus()
        self.__count_down(TEST_LEN_SEC)
        self.__start_button.config(text="Cancel Test", command=self.__cancel_test)

    def __cancel_test(self):
        self.__word_label.config(text="word")
        self.__score_label.config(text="0/0")
        self.__time_label.config(text="00")
        self.__window.after_cancel(self.__timer)
        self.__timer = None
        self.__start_button.config(text="Start Typing", command=self.__start_test)

    def __input_typed_entry(self, event=None):
        if self.__timer:
            self.__tst.store_typed_word(self.__typing_entry.get())
            self.__score_label.config(text=self.__tst.get_score_str())
            self.__get_new_word()

    def __get_new_word(self):
        self.__word_label.config(text=self.__tst.get_word())
        self.__typing_entry.delete(0, END)

    def __count_down(self, count):
        self.__time_label.config(text=f"{count:02}")
        if count > 0:
            self.__timer = self.__window.after(1000, self.__count_down, count - 1)
        else:
            self.__window.after_cancel(self.__timer)
            self.__timer = None
            self.__start_button.config(text="Start Typing", command=self.__start_test)
