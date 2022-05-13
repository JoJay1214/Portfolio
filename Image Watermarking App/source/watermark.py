"""
Image Watermarking App
file:   watermark.py
author: Joshua Jacobs
date:   3/11/2022
brief:  Used to place a watermark on a given image file.

"""
from PIL import Image, ImageFont, ImageDraw


class Watermark:
    """
    Used to place a watermark on a given image file
    """

    @staticmethod
    def watermark_image(filepath: str, watermark: str):
        """
        Opens an image and copies it, then applies a watermark to the copy and saves it
        :param filepath: Image to copy and watermark
        :param watermark: Watermark to be applied to image copy
        """

        # open image and make a copy
        watermarked_image = Image.open(filepath).copy()

        # setup copied image for drawing
        draw = ImageDraw.Draw(watermarked_image)
        font = ImageFont.truetype("arial.ttf", 50)

        # add Watermark
        draw.text((0, 0), watermark, (255, 255, 255), font=font)

        # save watermarked image
        new_file_name = filepath.split("/")[-1].split(".")[0]  # get file name without path or extension
        watermarked_image.save(f"watermarked-{new_file_name}.png", "PNG")
