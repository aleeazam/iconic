import random

from PIL import Image, ImageDraw
from hashlib import md5, sha1

md5 = lambda x: md5(x.encode()).hexdigest()

def _square(image, x, y, block, pad, colour):
    x = x * block + pad
    y = y * block + pad

    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x + block, y + block), fill=colour)

def identicon(seed, width=512, pad=0.1, hasher=md5):
    if pad < 0:
        raise ValueError("pad >= 0.0")
    
    seed = hasher(seed)[-15:]

    p = int(width * pad)
    b = (width - 2 * p) // 5
    w = b * 5 + 2 * p

    lum = 40 + int(seed[0], 16)
    hue = int(seed[-6:], 16) / 0xffffff * 360
    hsl = f"hsl({int(hue)}, 80%, {lum}%)"

    image  = Image.new("RGB", (w, w), "#F0F0F0")
    colour = hsl

    filled = []

    for i, v in enumerate(seed):
        yes = ord(v) % 2 != 0
        filled.append(yes)

        if yes and i < 10:
            _square(image, i // 5, i % 5, b, p, colour)        # 1
            _square(image, 4 - i // 5, i % 5, b, p, colour)    # 3
        elif yes:
            _square(image, i // 5, i - 10, b, p, colour)       # 2

    if all(filled) or not any(filled):
        return identicon(seed, block, pad, hasher) # ignore boring icons
                                                   # blotted square or empty ones
        
    return image

if __name__ == "__main__":
    try:
        import argparse
    except:
        exit("pip install argparse")

    parser = argparse.ArgumentParser()
    parser.add_argument("seed", nargs="?", help="Seed used to generate the identicon.")
    parser.add_argument("-i", "--invert", help="Invert identicon colours.", action="store_true")
    parser.add_argument("-s", "--save", help="Confirm save identicon.", action="store_true")
    parser.add_argument("-v", "--view", help="View identicon.", action="store_true")

    args = parser.parse_args()

    if args.seed == None:
        args.seed = input("Enter seed: ").strip()

    image = identicon(args.seed, invert=args.invert)

    if args.view:
        image.show()

    if args.save or input("save (y/N): ") == "y":
        image.save(f"{args.seed}.png")
