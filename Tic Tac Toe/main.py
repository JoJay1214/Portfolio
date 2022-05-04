"""
Tic Tac Toe
file:   main.py
author: Joshua Jacobs
date:   4/26/2022
brief:  The classic Tic Tac Toe game presented in a GUI that was built using
        TKinter. The game is built for two players to switch off taking their
        turns; and resets after a round is decided.

"""
from source.tic_tac_toe import TicTacToe
from source.tic_tac_toe_ui import TicTacToeUI


def main():
    """
    Configures and runs the Tic Tac Toe app
    """
    tic_tac_toe = TicTacToe()
    TicTacToeUI(tic_tac_toe)


if __name__ == "__main__":
    main()
