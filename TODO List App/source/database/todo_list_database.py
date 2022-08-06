"""
TODO List App
file:   todo_list_database.py
author: Joshua Jacobs
date:   7/31/2022
brief:  Handles the management of a SQL Database that store the to-do list information

"""

# EXTERNAL LIBRARY IMPORTS
import sqlite3


class TODOListDatabase:
    """
    Handles the management of a SQL Database that store the to-do list information
    """

    """
    CONSTANTS
    """

    __TABLE_NAME = "items"

    __SQL_CREATE_TODOLIST_TABLE = f"""
        CREATE TABLE IF NOT EXISTS {__TABLE_NAME} (
            id integer PRIMARY KEY,
            title text NOT NULL,
            description text NOT NULL,
            deadline text NOT NULL
        );
    """

    __SQL_INSERT = f"""
        INSERT INTO {__TABLE_NAME}(
            title,
            description,
            deadline
        )
        VALUES(?,?,?)
    """

    """
    CONSTRUCTOR
    """

    def __init__(self):

        # PRIVATE VARIABLES
        self.__connection = None

    """
    DESTRUCTOR
    """

    def __del__(self):

        self.close_connection()

    """
    PUBLIC METHODS
    """

    def create_connection(self, fp: str):
        """
        Create a connection to a SQLite database
        :param fp: The filepath to the database
        """

        try:
            self.__connection = sqlite3.connect(fp)
            self.__create_table(self.__SQL_CREATE_TODOLIST_TABLE)
        except sqlite3.Error as e:
            print(e)

    def create_item(self, item):
        """
        Create a new item in the to-do list
        :param item: The item to add to the list
        """

        cursor = self.__connection.cursor()
        cursor.execute(self.__SQL_INSERT, item)
        self.__connection.commit()

    def get_all_items(self) -> list:
        """
        Get all the items in the to-do list from the database
        :return: The list of to-do items
        """

        cursor = self.__connection.cursor()
        cursor.execute(f"SELECT * FROM {self.__TABLE_NAME}")

        return cursor.fetchall()

    def delete_item_by_title(self, title: str):
        """
        Delete an item from the database given its Title
        :param title: The string of text to match with the row to delete
        """

        sql = f"DELETE FROM {self.__TABLE_NAME} WHERE title=?"
        cursor = self.__connection.cursor()
        cursor.execute(sql, (title,))
        self.__connection.commit()

    def close_connection(self):
        """
        If there is an open database connection, close it
        """

        if self.__connection:
            self.__connection.close()

    """
    PRIVATE METHODS
    """

    def __create_table(self, create_table_sql: str):
        """
        Create a table from the create_table_sql statement
        :param create_table_sql: The table to create in the database
        """

        try:
            cursor = self.__connection.cursor()
            cursor.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
