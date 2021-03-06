import random
import os

TYPEFACE = 'fonts/{}'.format(random.choice(os.listdir('fonts')))
FONT_SIZE = 30
TEXT_ALIGN = 'center'
IMAGE_SIZE = 320


EMOJI_TYPEFACE = 'emoji_fonts/{}'.format(random.choice(os.listdir('emoji_fonts')))
EMOJI_FONTSIZE = random.randint(45, 78)
MAX_EMOJI_LENGTH = 3
EMOJI_CHANCE = 0.75
