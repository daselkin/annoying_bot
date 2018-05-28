from PIL import Image

from caption import resize, caption
from complement_color import best_complement_color

def resize_and_caption(input_path, text, output_path):
    "Open"
    img = Image.open(input_path)
    "Resize"
    resize(img)

    color = best_complement_color(img.getcolors(img.size[0] * img.size[1]/2))
    
    "Draw text"
    caption(img, text, color)
    img.save(output_path)
