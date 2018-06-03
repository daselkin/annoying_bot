from params import EMOJI_TYPEFACE, EMOJI_FONTSIZE, MAX_EMOJI_LENGTH, EMOJI_CHANCE
import random

from PIL import ImageDraw, ImageFont

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
ALIGNS = ['left', 'right', 'center']
COLORS_RGB = [(0,0,0), (255, 255, 255), (255, 51, 51)]
COLORS_BW = [0, 255]

def emoji_str():
    return u''.join(random.choice(CHARS) for i in range(random.randint(1,MAX_EMOJI_LENGTH)))

def align():
    return random.choice(ALIGNS)

def color(rgb=True):
    return random.choice(COLORS_RGB if rgb else COLORS_BW)
    

def text_location(img, x_ratio, y_ratio):
    width, height = img.size
    return (
        random.randint(int(width*x_ratio[0]), int(width*x_ratio[1])),
        random.randint(int(height*y_ratio[0]), int(height*y_ratio[1]))
        )


def add_emojis_to_image(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(EMOJI_TYPEFACE, EMOJI_FONTSIZE)

    for x_range in [(0, 0.5), (0.5, 1)]:
        if random.random() <= EMOJI_CHANCE:
            location = text_location(img, x_range, (0.5, 1))
            try:
                draw.text(location, emoji_str(), color(), font=font, align=align())
            except:
                draw.text(location, emoji_str(), color(rgb=False), font=font, align=align())
