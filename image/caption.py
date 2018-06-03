from PIL import Image, ImageFont, ImageDraw

from params import TYPEFACE, FONT_SIZE, TEXT_ALIGN, IMAGE_SIZE

def resize(img):
    ratio = (IMAGE_SIZE/float(img.size[0]))
    height = int((float(img.size[1])*float(ratio)))
    img = img.resize((IMAGE_SIZE,max(IMAGE_SIZE,height)), Image.ANTIALIAS)
    #img = img.resize((IMAGE_SIZE,IMAGE_SIZE), Image.ANTIALIAS)
    return img


def caption(img, text, color):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(TYPEFACE, FONT_SIZE)
    draw.text((0, 0),text, color, font=font, align=TEXT_ALIGN)
