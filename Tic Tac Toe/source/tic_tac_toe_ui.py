"""
Tic Tac Toe
file:   tic_tac_toe_ui.py
author: Joshua Jacobs
date:   4/26/2022
brief:  TKinter GUI to give interaction between the
        user and the Tic Tac Toe program.
"""
from tkinter import Tk, Label, Button, Frame
from source.tic_tac_toe import TicTacToe


class TicTacToeUI:
    """
    TKinter GUI to give interaction between the user and the Tic Tac Toe program.
    """

    """
    CONSTANTS
    """

    # Program Control
    __RESET_TIME = 3000  # time before the game resets after a round

    # Widget Settings
    __WIN_START_POS = (350, 50)
    __WINDOW_PAD = 20

    __BUTTON_PAD = 5

    # Color
    __FRAME_BG_COLOR = "#000000"

    # Font
    __TITLE_FONT = ("Arial", 64, "bold")
    __BUTTON_FONT = ("Arial", 40, "bold")
    __GAME_TEXT_FONT = ("Arial", 40, "bold")

    """
    CONSTRUCTOR
    """

    def __init__(self, game: TicTacToe):
        """
        Tic Tac Toe UI Constructor
        :param game: The Tic Tac Toe object that controls the game behind the UI
        """
        self.__game = game  # the Tic Tac Toe game program

        self.__window = self.__config_window()              # the window that holds the UI
        self.__button_board = self.__config_button_board()  # the clickable buttons where game markers are placed
        self.__game_text = self.__config_game_text()        # text showing player turn and end game result

        self.__window.mainloop()

    """
    PRIVATE METHODS
    """

    def __update_button_board(self):
        """
        Updates the buttons' text in the UI to reflect the game's board
        """
        board = self.__game.get_board()  # game's current board

        # update each buttons' text corresponding to each space on the game's board
        for row in range(3):
            for col in range(3):
                self.__button_board[row][col].config(
                    text=board[row][col],
                )

    def __click_game_space(self, row, col):
        """
        Method bound to each button on the button board. Takes in the 2D index and begins the game flow.
        This is what gives the UI interactivity with the game
        :param row: 2D index corresponding to the row of the button
        :param col: 2D index corresponding to the column of the button
        """
        if self.__game.is_playing():
            self.__fill_space_on_board(row, col)

    def __fill_space_on_board(self, row, col):
        """
        Attempts to fill a space on the game's board
        :param row: 2D index corresponding to the row of the space on the board
        :param col:  2D index corresponding to the column of the space on the board
        """

        # if a space is open, fill it with the current player's marker
        if self.__game.place_marker(self.__game.get_current_player_marker(), row, col):
            self.__update_button_board()  # update board after move
            self.__check_board()          # check for game's end

    def __check_board(self):
        """
        Check the board for any sort of game-ending condition, like a win or draw
        """

        # if the current player has won, end the game and update game text
        if self.__game.check_for_winner(self.__game.get_current_player_marker()):
            self.__end_game(f"{self.__game.get_current_player_marker()}'s Win!")

        # if a player has not yet won...
        else:
            # if the board is filled and there's no winner, the game ends in a Draw
            if self.__game.is_board_filled():
                self.__end_game("DRAW!")

            # game has not yet ended, switch players and continue
            else:
                self.__game.change_player()
                self.__game_text.config(
                    text=f"{self.__game.get_current_player_marker()}'s Turn",
                )

    def __end_game(self, end_txt: str):
        """
        Display the end-game text and begin timer for game reset
        :param end_txt: The end-game text to be displayed
        """
        self.__game_text.config(
            text=end_txt,
        )
        self.__window.after(self.__RESET_TIME, self.__reset_game)

    def __reset_game(self):
        """
        Reset the game, reset the board, and reset the game text
        """
        self.__game.reset_game()
        self.__update_button_board()
        self.__game_text.config(
            text=f"{self.__game.get_current_player_marker()}'s Turn",
        )

    """
    UI Configuration
    """
    def __config_window(self) -> Tk:
        """
        Create and configure the window and the title label
        :return: The created TK window object
        """

        # window
        window = Tk()
        window.title("Tic Tac Toe")
        window.config(
            padx=self.__WINDOW_PAD,
            pady=self.__WINDOW_PAD,
        )
        window.geometry(f"+{self.__WIN_START_POS[0]}+{self.__WIN_START_POS[1]}")

        # title
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
        """
        Create and configure the 3x3 board of buttons and the frame that holds them
        :return: The 3x3 list of created TK buttons
        """

        # and empty list of lists for the board buttons
        board = [
            [],
            [],
            []
        ]

        # button board frame
        frame = Frame(
            bg=self.__FRAME_BG_COLOR,
        )
        frame.grid(
            column=0,
            row=1,
        )

        # create each button and append them properly to the list of lists
        for row in range(3):
            for col in range(3):

                button = Button(
                    frame,
                    text=" ",
                    font=self.__BUTTON_FONT,
                    height=1,
                    width=3,
                )
                # bind method to button, passing its 2D row/column indexes
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
        """
        Create and configure the game text label
        :return: The created TK Label
        """
        label = Label(
            text=f"{self.__game.get_current_player_marker()}'s Turn",
            font=self.__GAME_TEXT_FONT,
        )
        label.grid(
            column=0,
            row=2,
        )

        return label
