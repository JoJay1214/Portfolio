"""
Tic Tac Toe
file:   tic_tac_toe_app.py
author: Joshua Jacobs
date:   7/3/2022
brief:  Main TKinter GUI for Tic Tac Toe app

"""

# EXTERNAL LIBRARY IMPORTS
import tkinter as tk

# PROJECT IMPORTS
from source.ui.frames.title_frame import TitleFrame
from source.ui.frames.button_board_frame import ButtonBoardFrame
from source.ui.frames.game_text_frame import GameTextFrame

from source.tic_tac_toe import TicTacToe


class TicTacToeApplication(tk.Frame):
    """
    Main TKinter GUI for Tic Tac Toe app
    """

    """
    CONSTANTS
    """

    __RESET_TIME = 3000  # time before the game resets after a round

    """
    CONSTRUCTOR
    """

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        """
        Constructor for the Tic Tac Toe app
        :param parent: The parent window
        :param args: Argument list
        :param kwargs: Keyword Argument list
        """

        # INIT/CONFIG TK FRAME
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # PUBLIC VARIABLES
        self.parent = parent  # the parent window

        # PRIVATE VARIABLES
        self.__title = None                    # the app's title
        self.__button_board = None             # the clickable buttons where game markers are placed
        self.__game_text = None                # displays player turn and game result

        self.__tic_tac_toe_game = TicTacToe()  # the tic-tac-toe game program

        # CONFIG SELF
        self.__create_widgets()
        self.__config_widgets()
        self.__place_widgets()

    """
    PRIVATE METHODS
    """

    def __create_widgets(self):

        # TITLE
        self.__title = TitleFrame(
            self,
        )

        # BUTTON BOARD
        self.__button_board = ButtonBoardFrame(
            self,
        )

        # GAME TEXT
        self.__game_text = GameTextFrame(
            self,
        )

    def __config_widgets(self):

        # BUTTON BOARD
        self.__button_board.set_button_board_commands(cmd=self.__click_game_space)

        # GAME TEXT
        self.__game_text.set_game_text(f"{self.__tic_tac_toe_game.get_current_player_marker()}'s Turn")

    def __place_widgets(self):

        # TITLE
        self.__title.grid(
            column=0,
            row=0,
            sticky="NESW",
        )

        # BUTTON BOARD
        self.__button_board.grid(
            column=0,
            row=1,
        )

        # GAME TEXT
        self.__game_text.grid(
            column=0,
            row=2,
            sticky="NESW",
        )

    def __update_button_board(self):
        """
        Updates the buttons' text in the UI to reflect the game's board
        """

        board = self.__tic_tac_toe_game.get_board()  # game's current board

        # update each buttons' text corresponding to each space on the game's board
        for row in range(3):
            for col in range(3):
                self.__button_board.__button_board[row][col].config(
                    text=board[row][col],
                )

    def __click_game_space(self, row, col):
        """
        Method bound to each button on the button board. Takes in the 2D index and begins the game flow.
        This is what gives the UI interactivity with the game
        :param row: 2D index corresponding to the row of the button
        :param col: 2D index corresponding to the column of the button
        """

        if self.__tic_tac_toe_game.is_playing():
            self.__fill_space_on_board(row, col)

    def __fill_space_on_board(self, row, col):
        """
        Attempts to fill a space on the game's board
        :param row: 2D index corresponding to the row of the space on the board
        :param col:  2D index corresponding to the column of the space on the board
        """

        # if a space is open, fill it with the current player's marker
        if self.__tic_tac_toe_game.place_marker(self.__tic_tac_toe_game.get_current_player_marker(), row, col):
            self.__update_button_board()  # update board after move
            self.__check_board()          # check for game's end

    def __check_board(self):
        """
        Check the board for any sort of game-ending condition, like a win or draw
        """

        # if the current player has won, end the game and update game text
        if self.__tic_tac_toe_game.check_for_winner(self.__tic_tac_toe_game.get_current_player_marker()):
            self.__end_game(f"{self.__tic_tac_toe_game.get_current_player_marker()}'s Win!")

        # if a player has not yet won...
        else:
            # if the board is filled and there's no winner, the game ends in a Draw
            if self.__tic_tac_toe_game.is_board_filled():
                self.__end_game("DRAW!")

            # game has not yet ended, switch players and continue
            else:
                self.__tic_tac_toe_game.change_player()
                self.__game_text.set_game_text(f"{self.__tic_tac_toe_game.get_current_player_marker()}'s Turn")

    def __end_game(self, end_txt: str):
        """
        Display the end-game text and begin timer for game reset
        :param end_txt: The end-game text to be displayed
        """

        self.__game_text.set_game_text(end_txt)
        self.parent.after(self.__RESET_TIME, self.__reset_game)

    def __reset_game(self):
        """
        Reset the game, reset the board, and reset the game text
        """

        self.__tic_tac_toe_game.reset_game()
        self.__update_button_board()
        self.__game_text.set_game_text(f"{self.__tic_tac_toe_game.get_current_player_marker()}'s Turn")
