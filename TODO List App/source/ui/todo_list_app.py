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
from source.ui.frames.user_error_feedback_frame import UserErrorFeedbackFrame
from source.ui.frames.add_edit_remove_frame import AddEditRemoveFrame

from source.database.todo_list_database import TODOListDatabase


class TODOListApp(tk.Frame):
    """
    An application built using TKinter that acts as a to-do list viewer/manager
    """

    """
    CONSTANTS
    """

    __DB_FILEPATH = "db/TODOListDatabase.db"  # filepath to the database file

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
        self.grid_rowconfigure(3, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent container

        # PRIVATE VARIABLES
        self.__list_header = None                       # heads the list of to-do items
        self.__list_frame = None                        # displays the list of to-do items
        self.__user_error_feedback_frame = None         # displays error text for the user when necessary
        self.__add_edit_remove = None                   # buttons for adding, editing, and removing list items

        self.__todo_list_database = TODOListDatabase()  # manages the to-do list database

        self.__selected_list_item = None                # current selected item in the list

        # CONFIG SELF
        self.__create_widgets()
        self.__config_commands()
        self.__place_widgets()

        # LOAD DATABASE
        self.__todo_list_database.create_connection(self.__DB_FILEPATH)
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

        # ERROR FEEDBACK
        self.__user_error_feedback_frame = UserErrorFeedbackFrame(
            self,
        )

        # ADD AND REMOVE
        self.__add_edit_remove = AddEditRemoveFrame(
            self,
        )

    def __config_commands(self):

        # ADD
        self.__add_edit_remove.set_add_btn_cmd(self.__add_list_input_item)

        # EDIT
        self.__add_edit_remove.set_edit_btn_cmd(self.__edit_list_item)

        # REMOVE
        self.__add_edit_remove.set_remove_btn_cmd(self.__delete_list_item)

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

        # USER ERROR
        self.__user_error_feedback_frame.grid(
            column=0,
            row=2,
            sticky="EW",
        )

        # ADD AND REMOVE
        self.__add_edit_remove.grid(
            column=0,
            row=3,
            sticky="E",
        )

    def __load_items(self, items: list):

        # load the list of items into the list frame ui
        for item in items:
            list_item = self.__list_frame.create_new_list_item(
                title=item[1],
                description=item[2],
                deadline=item[3]
            )
            list_item.bind_on_click_command(cmd=self.__select_list_item)

    def __add_list_input_item(self):

        # if there is not already a 3-col input widget
        # create a new one, add it to the list, and scroll to it
        if not self.__list_frame.input_item_is_active():
            self.__deselect_list_item()

            self.__add_edit_remove.set_add_btn_state(state="disabled")
            self.__add_edit_remove.set_edit_btn_state(state="disabled")

            self.__list_frame.create_new_input_item(cmd=self.__add_list_item)

            self.parent.update_idletasks()
            self.__list_frame.scroll_to_list_end()

    def __add_list_item(self, _=None):

        # get input item texts
        input_item = self.__list_frame.get_inputted_text()

        # if title has text and title is not already in the database
        if input_item[0] and self.__todo_list_database.create_item(input_item):

            # add item to UI and database, then reset ui to original state
            list_item = self.__list_frame.create_new_list_item(
                title=input_item[0],
                description=input_item[1],
                deadline=input_item[2]
            )
            list_item.bind_on_click_command(cmd=self.__select_list_item)

            self.parent.update_idletasks()
            self.__list_frame.scroll_to_list_end()

            self.__reset_ui()

        elif not input_item[0]:

            # flash user error text explaining title needs to be input to be submitted
            self.__user_error_feedback_frame.set_error_text(text="*A Title is required to submit a new item")

        else:

            # flash user error text explaining title key already exists in the database
            self.__user_error_feedback_frame.set_error_text(text="*An item with that Title already exists")

    def __select_list_item(self, event):

        if not self.__list_frame.input_item_is_active():

            # deselect the old list item, if there is one
            self.__deselect_list_item()

            event_widget = event.widget

            # accommodate for whether the frame or the label was clicked from the List Item
            if event_widget.winfo_class() == "Frame":
                caller = event_widget
            else:
                caller = event_widget.master

            # select and highlight the newly clicked list item
            caller.select_list_item()
            self.__selected_list_item = caller

    def __deselect_list_item(self, _=None):

        if self.__selected_list_item:

            # if there's a selected list item, deselect it
            self.__selected_list_item.deselect_list_item()
            self.__selected_list_item = None

    def __edit_list_item(self):

        if self.__selected_list_item:

            # if there's a selected list item, edit it
            self.__add_edit_remove.set_add_btn_state(state="disabled")
            self.__add_edit_remove.set_edit_btn_state(state="disabled")

            self.__list_frame.edit_list_item(item=self.__selected_list_item, cmd=self.__update_edited_item)

    def __update_edited_item(self, _=None):

        input_item = self.__list_frame.get_inputted_text()
        old_item_data = self.__selected_list_item.get_list_item_text()

        # if a title is filled in and the title does not already exist in the database
        if input_item[0] and self.__todo_list_database.update_item(old_item=old_item_data, new_item=input_item):

            # update the item in the database and ui
            self.__selected_list_item.set_list_item_text(
                title=input_item[0],
                description=input_item[1],
                deadline=input_item[2]
            )

            self.__reset_ui()

        elif not input_item[0]:

            # flash user error text explaining title needs to be input to be submitted
            self.__user_error_feedback_frame.set_error_text(text="*A Title is required to submit a new item")

        else:

            # flash user error text explaining title key already exists in the database
            self.__user_error_feedback_frame.set_error_text(text="*An item with that Title already exists")

    def __delete_list_item(self):

        if self.__list_frame.input_item_is_active():

            # simply reset ui back to normal and remove 3-col input item
            self.__reset_ui()

        else:

            # there is no input item, currently
            # check for a selected item in the list
            if self.__selected_list_item:

                # get the title of the selected item
                item_title = self.__selected_list_item.get_list_item_text()[0]

                # delete the item by title in the database and clear the list for refilling
                self.__todo_list_database.delete_item_by_title(item_title)
                self.__list_frame.clear_list()
                self.__selected_list_item = None

                # repopulate the list in the ui with the remaining items in the database
                list_items = self.__todo_list_database.get_all_items()
                self.__load_items(list_items)

    def __reset_ui(self):

        # reset ui widgets back to their original states
        self.__user_error_feedback_frame.clear_error_text()
        self.__add_edit_remove.set_add_btn_state(state="normal")
        self.__add_edit_remove.set_edit_btn_state(state="normal")
        self.__list_frame.destroy_current_input_item()
