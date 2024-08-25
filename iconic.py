import random

from PIL import Image, ImageDraw

def identicon():
    width, pad = 256, 0.2 # icon's width and blank border

    p = int(width * pad)
    b = (width - 2 * p) // 5
    w = b * 5 + 2 * p

    seed = "blah blah" # needs to be random or provided?

    lum = 40 + int(seed[0], 16)
    hue = int(seed[-6:], 16) / 0xffffff * 360
    hsl = f"hsl({int(hue)}, 80%, {lum}%)"

    image  = Image.new("RGB", (w, w), "#F0F0F0")
    colour = hsl

    # algorithmcally plot dots on the image like github user icons

    return image

identicon().show()
