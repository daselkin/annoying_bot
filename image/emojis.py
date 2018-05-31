from params import EMOJI_TYPEFACE, EMOJI_FONTSIZE, MAX_EMOJI_LENGTH, EMOJI_CHANCE
import random

from PIL import ImageDraw, ImageFont

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
ALIGNS = ['left', 'right', 'center']
COLORS = [(0,0,0), (255, 255, 255), (255, 51, 51)]

def emoji_str():
    return u''.join(random.choice(CHARS) for i in range(random.randint(1,MAX_EMOJI_LENGTH)))

def align():
    return random.choice(ALIGNS)

def color():
    return random.choice(COLORS)
    

def text_location(img, x_ratio, y_ratio):
    width, height = img.size
    return (
        random.randint(int(width*x_ratio[0]), int(width*x_ratio[1])),
        random.randint(int(height*y_ratio[0]), int(height*y_ratio[1]))
        )


def add_emojis_to_image(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(EMOJI_TYPEFACE, EMOJI_FONTSIZE)

    if random.random() <= EMOJI_CHANCE:
        draw.text(text_location(img, (0, 0.5), (0.5, 1)), emoji_str(), color(), font=font, align=align())

    if random.random() <= EMOJI_CHANCE:
        draw.text(text_location(img, (0.5, 1), (0.5, 1)), emoji_str(), color(), font=font, align=align())
