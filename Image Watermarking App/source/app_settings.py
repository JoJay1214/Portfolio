"""
Image Watermarking App
file:   app_settings.py
author: Joshua Jacobs
date:   6/7/2022
brief:  Contains the constants used to control TKinter options in the app--such as background color and
        padding size.

"""

"""
MAIN APPLICATION
"""

# Color
PRIMARY_APP_COLOR = "#CCCCCC"  # primary background color of the app

# File Dialog Settings
OPEN_FILETYPES = [
    ("All Files", "*.*"),
]
SAVE_FILETYPES = [
    ("PNG Files", "*.png"),
]

# TK Window Settings
WIN_START_POS = (0, 0)  # starting position of the app window
WIN_PAD_X = 20
WIN_PAD_Y = 10

"""
WATERMARK SETTINGS
"""
TROUGH_COLOR = "#AAAAAA"

"""
IMAGE CANVASES
"""
CANVAS_WIDTH = 540  # width of the canvases the images sit on
CANVAS_HEIGHT = 304  # height of the canvases the images sit on

CANVAS_BG_COLOR = "#000000"  # canvas background color

CANVAS_PAD_Y = 5  # top and bottom canvas padding
