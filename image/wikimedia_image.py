import requests
from bs4 import BeautifulSoup

WIKILINK = 'https://commons.wikimedia.org/wiki/Special:Random/Image'

MAX_ATTEMPTS = 10

def is_jpg(r):
    return r.url[-4:].lower() == '.jpg'


def get_wikimedia_jpg_url():
    attempt = 0
    while (attempt < MAX_ATTEMPTS) or MAX_ATTEMPTS == -1:
        r = requests.get(WIKILINK)
        if is_jpg(r):
            s = BeautifulSoup(r.text, 'lxml')
            return s.find(class_='fullImageLink').img.attrs['src']
        else:
            attempt += 1
    raise IOError("Can't find a suitable image")


