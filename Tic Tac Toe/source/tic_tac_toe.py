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

    def get_board(self) -> list:
        return self.__board

    def get_current_player_marker(self) -> str:
        return self.__players[self.__current_player]

    def play(self):
        self.assign_markers()

        self.show_board()

        while self.__is_playing:
            for player in self.__players:
                self.place_marker(player)

                if self.check_for_winner(player) or self.is_board_filled():
                    break

    # def reset_board(self):
    #     for row in self.__board:
    #         row[0] = ' '
    #         row[1] = ' '
    #         row[2] = ' '

    def show_board(self):
        print(
            f" {self.__board[0][0]} | {self.__board[0][1]} | {self.__board[0][2]} \n"
            f"-----------\n"
            f" {self.__board[1][0]} | {self.__board[1][1]} | {self.__board[1][2]} \n"
            f"-----------\n"
            f" {self.__board[2][0]} | {self.__board[2][1]} | {self.__board[2][2]} \n"
        )

    def is_board_filled(self):
        for row in self.__board:
            if ' ' in row:
                return False

        print("DRAW!")
        self.__is_playing = False

        return True

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
            print(f"{player}'s Win!")
            self.__is_playing = False
            return True
        else:
            return False

    def assign_markers(self):
        self.__players = self.__markers
        random.shuffle(self.__players)

    def place_marker(self, player):
        space_dict = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2],
        }

        print(f"{player}'s Turn")
        space = space_dict[int(input("Select a space to fill: "))]

        while not self.__board[int(space[0])][space[1]] == ' ':
            space = space_dict[int(input("Select a space to fill: "))]

        self.__board[int(space[0])][space[1]] = player
        print()
        self.show_board()

    def is_playing(self):
        return self.__is_playing
