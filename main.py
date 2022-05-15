from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, filedialog
from os import environ


window = Tk()
window.withdraw()


filename = filedialog.askopenfilename(title="select an image: ")
print(filename)


def add_watermark(image, text):
    opened_image = Image.open(image)

    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font1 = environ['FONT']
    font_size = int(image_width // 8)
    font = ImageFont.truetype(font1, font_size)
    x, y = int(image_width // 6), int(image_height // 6)

    draw.text((x, y), text, font=font, fill="#123", stroke_width=0, stroke_fill="#222", anchor="ms")

    opened_image.show()

add_watermark(filename, "Howdy!")

