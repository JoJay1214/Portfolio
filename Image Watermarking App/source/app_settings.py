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

# Background Color
PRIMARY_APP_COLOR = "#CCCCCC"    # primary background color of the app
SECTION_BG_COLOR = "#DDDDDD"     # section background color
SUBSECTION_BG_COLOR = "#EEEEEE"  # subsection background color

# Border Highlight Color
SECTION_HIGH_THICKNESS = 1
SECTION_HIGH_BG_COLOR = "#666666"
SUBSECTION_HIGH_BG_COLOR = "#777777"

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

# Section Padding
SEC_TITLE_PAD_X = (10, 0)
SEC_TITLE_PAD_Y = (10, 0)

"""
WATERMARK SETTINGS
"""
TROUGH_COLOR = "#CCCCCC"

"""
IMAGE CANVASES
"""
CANVAS_WIDTH = 540  # width of the canvases the images sit on
CANVAS_HEIGHT = 304  # height of the canvases the images sit on

CANVAS_BG_COLOR = "#000000"  # canvas background color

CANVAS_PAD_Y = 5  # top and bottom canvas padding
