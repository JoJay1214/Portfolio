from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Watermark():
    def watermark_image(self, filepath, watermark):
        image = Image.open(filepath)
        watermarked_image = image.copy()

        draw = ImageDraw.Draw(watermarked_image)
        font = ImageFont.truetype("arial.ttf", 50)

        # add Watermark
        draw.text((0, 0), watermark, (255, 255, 255), font=font)

        new_file_name = filepath.split("/")[-1].split(".")[0]
        watermarked_image.save(f"watermarked-{new_file_name}.png", "PNG")
