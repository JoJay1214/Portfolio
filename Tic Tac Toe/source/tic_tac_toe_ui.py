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
    __WINDOW_BG_COLOR = "#CCCCCC"
    __FRAME_BG_COLOR = "#000000"

    __TITLE_FONT = ("Arial", 64, "bold")
    __BUTTON_FONT = ("Arial", 40, "bold")
    __GAME_TEXT_FONT = ("Arial", 40, "bold")

    __BUTTON_PAD = 5

    def __init__(self, game: TicTacToe):
        self.__game = game
        self.__game.assign_markers()

        self.__window = self.__config_window()
        self.__button_board = self.__config_button_board()
        self.__game_text = self.__config_game_text()

        self.__window.mainloop()

    def __update_button_board(self):
        board = self.__game.get_board()

        for row in range(3):
            for col in range(3):
                self.__button_board[row][col].config(
                    text=board[row][col],
                )

    def __fill_space_on_board(self, space: Button):
        space.config(
            text=f"{self.__game.get_current_player_marker()}",
            state="disabled",
        )

    def __config_window(self) -> Tk:
        window = Tk()
        window.title("Tic Tac Toe")
        window.config(
            bg=self.__WINDOW_BG_COLOR,
        )

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
                    command=lambda btn_arg=button: self.__fill_space_on_board(btn_arg),
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
