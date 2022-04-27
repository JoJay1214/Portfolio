"""
Tic Tac Toe
main.py
Joshua Jacobs
4/26/2022
"""
from source.tic_tac_toe import TicTacToe
from source.tic_tac_toe_ui import TicTacToeUI


def main():
    """
    Tic Tac Toe demo
    """
    tic_tac_toe = TicTacToe()
    TicTacToeUI(tic_tac_toe)


if __name__ == "__main__":
    main()
