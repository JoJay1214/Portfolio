"""
Text to Morse Code App
file:   app_settings.py
author: Joshua Jacobs
date:   6/23/2022
brief:  Contains the constants used to control TKinter options in the app--such as background color and
        padding size.

"""

"""
MAIN APP
"""
MS_TIL_TRANSLATE = 200     # time to wait between translation updates
MC_TIME_INTERVAL_MS = 100  # time interval for morse code audio output

FRAME_HIGHLIGHT_THICKNESS = 1
FRAME_HIGHLIGHT_COLOR = "#000000"

"""
WINDOW
"""

# color
WINDOW_BG_COLOR = "#BBBBBB"

# padding
WINDOW_PADX = 50
WINDOW_PADY = 20

"""
TITLE FRAME
"""
TITLE_FONT = ("Arial", 36, "bold")
TITLE_MC_FONT = ("Arial", 18, "bold")

"""
INPUT TEXTBOX FRAME
"""
ENTRY_FONT = ("Arial", 16)

INPUT_TEXT_HEIGHT = 5
INPUT_STARTING_TEXT = "Text to Morse Code"

"""
OUTPUT TEXTBOX FRAME
"""
OUTPUT_TEXT_HEIGHT = 1
OUTPUT_TEXT_BG_COLOR = "#000000"
OUTPUT_TEXT_FG_COLOR = "#FFFFFF"

MORSE_CODE_FONT = ("Arial", 16, "bold")

"""
PLAY BUTTON FRAME
"""
BUTTON_FONT = ("Arial", 18, "bold")
