"""
Image Watermarking App
file:   watermark.py
author: Joshua Jacobs
date:   3/11/2022
brief:  Can be used to open an image file, watermark it, resize it, and save it.

"""

# EXTERNAL LIBRARY IMPORTS
import PIL
from PIL import Image, ImageFont, ImageDraw


class Watermark:
    """
    Can be used to open an image file, watermark it, resize it, and save it
    """

    """
    CONSTANTS
    """
    __FONT = "arial.ttf"
    __DEFAULT_FONT_SIZE = 50
    __DEFAULT_FONT_COLOR = (255, 255, 255, 255)
    __DEFAULT_TEXT_POS = (0, 0)

    """
    METHODS
    """

    @staticmethod
    def get_image(path) -> Image:
        """
        Attempt to open and get an image file
        :param path: The location of the image
        :return: The Image, if it was opened properly, else None
        """

        try:
            return Image.open(path)
        except FileNotFoundError:
            print("Error! File Not Found")
        except PIL.UnidentifiedImageError:
            print("Error! Unidentified Image (Possibly not an image file)")

        return None

    @staticmethod
    def watermark_image(
            image: Image, watermark: str,
            font_size: __DEFAULT_FONT_SIZE, color: __DEFAULT_FONT_COLOR, pos: __DEFAULT_TEXT_POS
    ) -> Image:
        """
        Get a copy of an image with a watermark on it
        :param image: The image to watermark
        :param watermark: The text to watermark the image
        :param font_size: The size of the watermark text font
        :param color: The color of the watermark font
        :param pos: The XY position of the watermark text
        :return: The watermarked image
        """

        # create blank image for alpha text
        alpha_txt = Image.new('RGBA', image.size, (255, 255, 255, 0))

        # setup tools needed to draw text on image
        font = ImageFont.truetype(Watermark.__FONT, font_size)
        draw = ImageDraw.Draw(alpha_txt)

        # draw text on blank image, then composite that onto copy of image to watermark
        draw.text(pos, watermark, color, font=font)
        watermarked_image = Image.alpha_composite(image.copy().convert('RGBA'), alpha_txt)

        return watermarked_image

    @staticmethod
    def resize_image(image: Image, max_x: int, max_y: int) -> Image:
        """
        Resize an Image to fit a canvas of specified dimensions, preserving the image's aspect ratio
        :param image: The image to resize
        :param max_x: The maximum possible width of the resized image
        :param max_y: The maximum possible height of the resized image
        :return: The resized image
        """

        if image.height >= image.width:
            # resize by height
            resized_img = image.resize(
                (int(image.width * (max_y / image.height)), int(image.height * (max_y / image.height))),
                Image.ANTIALIAS
            )

        else:
            # resize by width
            resized_img = image.resize(
                (int(image.width * (max_x / image.width)), int(image.height * (max_x / image.width))),
                Image.ANTIALIAS
            )

        return resized_img

    @staticmethod
    def save_image(image: Image, path: str):
        """
        Save an image to a specific file path
        :param image: Image to save
        :param path: The file path to be saved on
        """

        image.save(f"{path}.png", "PNG")
