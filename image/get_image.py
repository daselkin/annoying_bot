from wikimedia_image import get_wikimedia_jpg_url

import requests
import shutil


def save_image(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)


def get_image(path):
    save_image(get_wikimedia_jpg_url(), path)
    
