"""
Tic Tac Toe
tic_tac_toe_ui.py
Joshua Jacobs
4/26/2022
"""
from tkinter import Tk, Label, Button, Frame
from source.tic_tac_toe import TicTacToe


class TicTacToeUI:
    """
    CONSTANTS
    """
    __RESET_TIME = 3000

    __FRAME_BG_COLOR = "#000000"

    __TITLE_FONT = ("Arial", 64, "bold")
    __BUTTON_FONT = ("Arial", 40, "bold")
    __GAME_TEXT_FONT = ("Arial", 40, "bold")

    __WINDOW_PAD = 20
    __BUTTON_PAD = 5

    __WIN_START_POS = (350, 50)

    """
    CONSTRUCTOR
    """
    def __init__(self, game: TicTacToe):
        self.__game = game

        self.__window = self.__config_window()
        self.__button_board = self.__config_button_board()
        self.__game_text = self.__config_game_text()

        self.__window.mainloop()

    """
    PRIVATE METHODS
    """
    def __update_button_board(self):
        board = self.__game.get_board()

        for row in range(3):
            for col in range(3):
                self.__button_board[row][col].config(
                    text=board[row][col],
                )

    def __click_game_space(self, row, col):
        if self.__game.is_playing():
            self.__fill_space_on_board(row, col)

    def __fill_space_on_board(self, row, col):
        if self.__game.place_marker(self.__game.get_current_player_marker(), row, col):
            self.__update_button_board()
            self.__check_board()

    def __check_board(self):
        if self.__game.check_for_winner(self.__game.get_current_player_marker()):
            self.__end_game(f"{self.__game.get_current_player_marker()}'s Win!")
        else:
            if self.__game.is_board_filled():
                self.__end_game("DRAW!")
            else:
                self.__game.change_player()
                self.__game_text.config(
                    text=f"{self.__game.get_current_player_marker()}'s Turn",
                )

    def __end_game(self, end_txt: str):
        self.__game_text.config(
            text=end_txt,
        )
        self.__window.after(self.__RESET_TIME, self.__reset_game)

    def __reset_game(self):
        self.__game.reset_game()
        self.__update_button_board()
        self.__game_text.config(
            text=f"{self.__game.get_current_player_marker()}'s Turn",
        )

    """
    UI Configuration
    """
    def __config_window(self) -> Tk:
        window = Tk()
        window.title("Tic Tac Toe")
        window.config(
            padx=self.__WINDOW_PAD,
            pady=self.__WINDOW_PAD,
        )
        window.geometry(f"+{self.__WIN_START_POS[0]}+{self.__WIN_START_POS[1]}")

        title_label = Label(
            text="Tic Tac Toe",
            font=self.__TITLE_FONT,
        )
        title_label.grid(
            column=0,
            row=0,
        )

        return window

    def __config_button_board(self) -> list:
        board = [
            [],
            [],
            []
        ]

        frame = Frame(
            bg=self.__FRAME_BG_COLOR,
        )
        frame.grid(
            column=0,
            row=1,
        )

        for row in range(3):
            for col in range(3):
                button = Button(
                    frame,
                    text=" ",
                    font=self.__BUTTON_FONT,
                    height=1,
                    width=3,
                )
                button.config(
                    command=lambda r=row, c=col: self.__click_game_space(r, c),
                )
                button.grid(
                    column=col,
                    row=row,
                    padx=self.__BUTTON_PAD,
                    pady=self.__BUTTON_PAD,
                )
                board[row].append(button)

        return board

    def __config_game_text(self) -> Label:
        label = Label(
            text=f"{self.__game.get_current_player_marker()}'s Turn",
            font=self.__GAME_TEXT_FONT,
        )
        label.grid(
            column=0,
            row=2,
        )

        return label
