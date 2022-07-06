"""
Tic Tac Toe
file:   tic_tac_toe.py
author: Joshua Jacobs
date:   3/10/2022
brief:  Tic Tac Toe implementation and logic that runs the game.

"""
import random  # shuffle


class TicTacToe:
    """
    Tic Tac Toe class that acts as and controls the Tic Tac Toe game.
    """

    """
    CONSTRUCTOR
    """

    def __init__(self):
        # game board with empty spaces
        self.__board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.__markers = ['X', 'O']  # X and O to signify players
        self.__current_player = 0    # current player's turn, first or second
        self.__is_playing = True     # is the game still in the middle of being played?

        # randomize which player goes first
        random.shuffle(self.__markers)

    """
    PUBLIC METHODS
    """

    def is_playing(self):
        """
        Get whether the game is still being played or has ended
        :return: The current status of the game
        """
        return self.__is_playing

    def get_board(self) -> list:
        """
        Get the game board in its current state
        :return: The game's board in a 3x3 list
        """
        return self.__board

    def get_current_player_marker(self) -> str:
        """
        Get the marker of the current player
        :return: The current player's marker
        """
        return self.__markers[self.__current_player]

    def place_marker(self, player: str, row: int, col: int) -> bool:
        """
        Place a player's marker in a given space if that space is empty
        :param player: Player marker to be placed
        :param row: Row on the board to place marker
        :param col: Column on the board to place marker
        :return: bool True if the marker was placed, False otherwise
        """
        if self.__board[row][col] == " ":
            self.__board[row][col] = player
            return True
        else:
            return False

    def change_player(self):
        """
        Swap the current player with the other player
        """
        self.__current_player = not self.__current_player

    def check_for_winner(self, player: str) -> bool:
        """
        Checks the possible winning scenarios on the board to see if a player has won.
        Ends the game if a player has won
        :param player: The player marker to be checked against the board
        :return: bool True if a player has won, False otherwise
        """
        # if any of the winning triples contain the same marker, that player wins
        if \
                player == self.__board[0][0] == self.__board[0][1] == self.__board[0][2] or \
                player == self.__board[1][0] == self.__board[1][1] == self.__board[1][2] or \
                player == self.__board[2][0] == self.__board[2][1] == self.__board[2][2] or \
                player == self.__board[0][0] == self.__board[1][0] == self.__board[2][0] or \
                player == self.__board[0][1] == self.__board[1][1] == self.__board[2][1] or \
                player == self.__board[0][2] == self.__board[1][2] == self.__board[2][2] or \
                player == self.__board[0][0] == self.__board[1][1] == self.__board[2][2] or \
                player == self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            self.__is_playing = False  # a player has won, end the game
            return True
        else:
            # no one has one, keep playing
            return False

    def is_board_filled(self) -> bool:
        """
        Checks if the game board has any spaces left open. Ends the game if all spaces are filled

        :return: Returns bool False if there is at least one space left open, True otherwise
        """
        # if any space on the board is empty, board is not filled completely
        for row in self.__board:
            if ' ' in row:
                return False

        self.__is_playing = False  # board is full, end the game

        return True

    def reset_game(self):
        """
        Resets game board to blank, player turn to Player 1, and game status to active
        Shuffles the player markers
        """

        # reset board to blank
        self.__board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.__current_player = 0  # reset current player turn to Player 1
        self.__is_playing = True   # reset game playing status to in-progress

        # randomize which player goes first
        random.shuffle(self.__markers)
