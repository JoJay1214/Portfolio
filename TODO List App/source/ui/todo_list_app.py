"""
TODO List App
file:   todo_list_app.py
author: Joshua Jacobs
date:   7/21/2022
brief:  An application built using TKinter that acts as a to-do list viewer/manager

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.frames.list_header_frame import ListHeaderFrame
from source.ui.frames.list_frame import ListFrame
from source.ui.frames.add_and_remove_frame import AddAndRemoveFrame

from source.database.todo_list_database import TODOListDatabase


class TODOListApp(tk.Frame):
    """
    An application built using TKinter that acts as a to-do list viewer/manager
    """

    """
    CONSTANTS
    """

    __DB_FILEPATH = "db/TODOListDatabase.db"

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        An application built using TKinter that acts as a to-do list viewer/manager
        :param parent: The parent container
        :param args: Argument List
        :param kwargs: Keyword Argument List
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__list_header = None
        self.__list_frame = None
        self.__add_and_remove = None

        self.__todo_list_database = TODOListDatabase()
        self.__todo_list_database.create_connection(self.__DB_FILEPATH)

        self.__selected_list_item = None

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

        # LOAD DATABASE
        list_items = self.__todo_list_database.get_all_items()
        self.__load_items(list_items)

    def __create_widgets(self):

        # HEADER
        self.__list_header = ListHeaderFrame(
            self,
        )

        # LIST
        self.__list_frame = ListFrame(
            self,
        )

        # ADD AND REMOVE
        self.__add_and_remove = AddAndRemoveFrame(
            self,
        )

    def __config_commands(self):

        # ADD
        self.__add_and_remove.set_add_btn_cmd(self.__add_list_input_item)

        # REMOVE
        self.__add_and_remove.set_remove_btn_cmd(self.__delete_list_item)

    def __place_widgets(self):

        # HEADER
        self.__list_header.grid(
            column=0,
            row=0,
            sticky="EW",
        )

        # LIST
        self.__list_frame.grid(
            column=0,
            row=1,
            sticky="NESW",
        )

        # ADD AND REMOVE
        self.__add_and_remove.grid(
            column=0,
            row=2,
            sticky="ES",
        )

    def __add_list_input_item(self):

        if not self.__list_frame.input_item_is_active():
            self.__list_frame.create_new_input_item(cmd=self.__add_list_item)
            self.parent.update_idletasks()
            self.__list_frame.scroll_to_list_end()

    def __add_list_item(self, _=None):

        # get item
        input_item = self.__list_frame.get_inputted_text()

        # add item to UI and database
        list_item = self.__list_frame.create_new_list_item(
            title=input_item[0],
            description=input_item[1],
            deadline=input_item[2]
        )
        list_item.bind_on_click_command(cmd=self.__select_list_item)

        self.__todo_list_database.create_item(input_item)

    def __load_items(self, items: list):

        for item in items:
            list_item = self.__list_frame.create_new_list_item(
                title=item[1],
                description=item[2],
                deadline=item[3]
            )
            list_item.bind_on_click_command(cmd=self.__select_list_item)

    def __select_list_item(self, event):

        if self.__selected_list_item:
            self.__selected_list_item.deselect_list_item()

        event_widget = event.widget

        if event_widget.winfo_class() == "Frame":
            caller = event_widget
        else:
            caller = event_widget.master

        caller.select_list_item()
        self.__selected_list_item = caller

    def __delete_list_item(self):

        if self.__selected_list_item:
            item_title = self.__selected_list_item.get_list_item_text()[0]

            self.__todo_list_database.delete_item_by_title(item_title)
            self.__list_frame.clear_list()
            self.__selected_list_item = None

            list_items = self.__todo_list_database.get_all_items()
            self.__load_items(list_items)
