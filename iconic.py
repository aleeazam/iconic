import random

from PIL import Image, ImageDraw

def square(image, x, y, block, pad, colour):
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

    # algorithmcally plot dots on the image like github user icons
    # random for now
    for i in range(3):
            square(image, i, 0, b, p, colour)

    return image

identicon("arcadeisthebest").show()
