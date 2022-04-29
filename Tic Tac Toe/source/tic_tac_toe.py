"""
Tic Tac Toe
tic_tac_toe.py
Joshua Jacobs
3/10/2022
"""
import random  # shuffle


class TicTacToe:
    """
    Tic Tac Toe
    """

    def __init__(self):
        self.__board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.__markers = ['X', 'O']
        self.__players = []
        self.__current_player = 0
        self.__is_playing = True

        self.__assign_markers()

    def is_playing(self):
        return self.__is_playing

    def get_board(self) -> list:
        return self.__board

    def is_board_filled(self):
        for row in self.__board:
            if ' ' in row:
                return False

        self.__is_playing = False

        return True

    def reset_game(self):
        self.__board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.__assign_markers()
        self.__current_player = 0
        self.__is_playing = True

    def get_current_player_marker(self) -> str:
        return self.__players[self.__current_player]

    def __assign_markers(self):
        self.__players = self.__markers
        random.shuffle(self.__players)

    def place_marker(self, player, row, col) -> bool:
        if self.__board[row][col] == " ":
            self.__board[row][col] = player
            return True
        else:
            return False

    def change_player(self):
        self.__current_player = not self.__current_player

    def check_for_winner(self, player):
        if \
                player == self.__board[0][0] == self.__board[0][1] == self.__board[0][2] or \
                player == self.__board[1][0] == self.__board[1][1] == self.__board[1][2] or \
                player == self.__board[2][0] == self.__board[2][1] == self.__board[2][2] or \
                player == self.__board[0][0] == self.__board[1][0] == self.__board[2][0] or \
                player == self.__board[0][1] == self.__board[1][1] == self.__board[2][1] or \
                player == self.__board[0][2] == self.__board[1][2] == self.__board[2][2] or \
                player == self.__board[0][0] == self.__board[1][1] == self.__board[2][2] or \
                player == self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            self.__is_playing = False
            return True
        else:
            return False
