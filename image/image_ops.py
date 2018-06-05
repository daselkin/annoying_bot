from PIL import Image

from caption import resize, caption
from complement_color import best_complement_color
from emojis import add_emojis_to_image

def resize_and_caption(input_path, text, output_path):
    "Open"
    img = Image.open(input_path)
    img = img.convert(mode='RGB')

    color = best_complement_color(img.getcolors(img.size[0] * img.size[1]/2))
    
    "Resize"
    img = resize(img)
    
    "Draw text"
    caption(img, text, color)
    add_emojis_to_image(img)
    
    img.save(output_path)
