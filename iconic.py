import random

from PIL import Image, ImageDraw

def _square(image, x, y, block, pad, colour):
    x = x * block + pad
    y = y * block + pad

    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x + block, y + block), fill=colour)

def identicon(seed):
    if len(seed) != 15:
            print("Seed needs to be 15 characters!")
            raise TypeError
    
    width, pad = 256, 0.1 # icon's width and blank border

    p = int(width * pad)
    b = (width - 2 * p) // 5
    w = b * 5 + 2 * p

    lum = 40 + int(seed[0], 16)
    hue = int(seed[-6:], 16) / 0xffffff * 360
    hsl = f"hsl({int(hue)}, 80%, {lum}%)"

    image  = Image.new("RGB", (w, w), "#F0F0F0")
    colour = hsl

    for i, v in enumerate(seed):
        yes = ord(v) % 2 != 0

        if yes and i < 10:
            _square(image, i // 5, i % 5, b, p, colour)        # first column
            _square(image, 4 - i // 5, i % 5, b, p, colour)    # last column
        elif yes:
            _square(image, i // 5, i - 10, b, p, colour)       # middle column

    return image

identicon("arcadeisthebest").show()
