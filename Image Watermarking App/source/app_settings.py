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

# Background
PRIMARY_APP_COLOR = "#CCCCCC"  # primary color of the app
SEC_BG_COLOR = "#DDDDDD"       # section background color
SUBSEC_BG_COLOR = "#EEEEEE"    # subsection background color

# Border Highlight
SEC_HL_THICKNESS = 1         # sub/section border highlight thickness
SEC_HL_COLOR = "#666666"     # section border highlight color
SUBSEC_HL_COLOR = "#999999"  # subsection border highlight color

# File Dialog Settings
OPEN_FILETYPES = [         # file types shown when browsing to open a file
    ("All Files", "*.*"),
]
SAVE_FILETYPES = [         # file types shown when browsing to save a file
    ("PNG Files", "*.png"),
]

# Font
SEC_TITLE_FONT = ("Arial", 16)    # section title font and font size
SEC_CONTENT_FONT = ("Arial", 12)  # section content font and font size

# Section Padding
SEC_OUTER_PAD = (15, 10)      # section outer x & y padding
SEC_CONTENT_OUTER_PAD_X = 40  # section content outer padding x

SEC_TITLE_PAD_X = (10, 0)     # section title padding x
SEC_TITLE_PAD_Y = (10, 10)    # section title padding y

SEC_ENTRY_PAD_X = (10, 20)    # section entry padding x
SEC_SCALE_PAD_LEFT = 10       # section scale left padding

"""
WINDOW
"""

# TK Window Settings
WIN_START_POS = (0, 0)  # starting position of the app window
WIN_PAD_X = 20          # window padding x
WIN_PAD_Y = 10          # window padding y

"""
FILE MANAGE SECTION
"""

BROWSE_BTN_WIDTH = 15  # width of the browse button
SAVE_BUTTON_PAD_Y = (10, 0)  # save button padding y

"""
IMAGE CANVASES SECTION
"""

CANVAS_WIDTH = 540           # width of the canvases the images sit on
CANVAS_HEIGHT = 304          # height of the canvases the images sit on

CANVAS_BG_COLOR = "#000000"  # canvas background color

CANVAS_PAD_Y = 5             # top and bottom canvas padding

"""
TEXT WATERMARK SECTION
"""

TROUGH_COLOR = "#CCCCCC"         # watermark settings subsections' scale trough color

UPDATE_WATERMARK_BTN_WIDTH = 15  # update watermark button width

"""
WATERMARK FONT SETTINGS SECTION
"""

FONT_SIZE_MIN = 1             # minimum value of font size scale
FONT_SIZE_MAX = 200           # maximum value of font size scale
FONT_SIZE_SCALE_DEFAULT = 50  # default settings for the font size scale

ALPHA_MIN = 0                 # minimum value of font alpha scale
ALPHA_MAX = 255               # maximum value of font alpha scale
ALPHA_SCALE_DEFAULT = 255     # default settings for the font alpha scale
