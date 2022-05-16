"""
Image Watermarking App
file:   watermark.py
author: Joshua Jacobs
date:   3/11/2022
brief:  Used to place a watermark on a given image file.

"""
import PIL
from PIL import Image, ImageFont, ImageDraw, ImageTk


class Watermark:
    """
    Used to place a watermark on a given image file
    """

    def __init__(self):
        self.__img = None
        self.__path = None

    def load_image(self, path):
        """
        Open an image and store it for use
        :param path: The location of the image
        """

        try:
            self.__img = Image.open(path)
            self.__path = path
        except FileNotFoundError:
            print("Error! File Not Found")
            self.__img = None
        except PIL.UnidentifiedImageError:
            print("Error! Unidentified Image (Possibly not an image file)")
            self.__img = None

    def get_image(self):
        """
        Get the currently loaded image
        :return: The currently loaded image
        """
        return self.__img

    def resize_image(self, image: Image, max_x: int, max_y: int):
        """
        Resize an Image to fit a canvas of specified dimensions
        :param image: The image to resize
        :param max_x: The maximum possible width of the resized image
        :param max_y: The maximum possible height of the resized image
        :return: The resized image
        """

        if image.height >= image.width:
            resized_img = image.resize(
                (int(image.width * (max_y / image.height)), int(image.height * (max_y / image.height))),
                Image.ANTIALIAS
            )
        else:
            resized_img = image.resize(
                (int(image.width * (max_x / image.width)), int(image.height * (max_x / image.width))),
                Image.ANTIALIAS
            )

        return resized_img

    def watermark_image(self, image: Image, watermark: str) -> Image:
        watermarked_image = image.copy()

        draw = ImageDraw.Draw(watermarked_image)
        font = ImageFont.truetype("arial.ttf", 50)

        draw.text((0, 0), watermark, (255, 255, 255), font=font)

        return watermarked_image

    def save_image(self, image: Image):
        """
        Opens an image and copies it, then applies a watermark to the copy and saves it
        :param filepath: Image to copy and watermark
        :param watermark: Watermark to be applied to image copy
        """

        # save watermarked image
        new_file_name = self.__path.split("/")[-1].split(".")[0]  # get file name without path or extension
        image.save(f"watermarked-{new_file_name}.png", "PNG")
