from text import reverse_hebrew, annoying_text
from image import get_image, resize_and_caption

import time

if __name__ == '__main__':
    filename = 'output/{}.jpg'.format(int(time.time()))

    get_image(filename)
    resize_and_caption(filename, reverse_hebrew(annoying_text(time.localtime())), filename)

    
