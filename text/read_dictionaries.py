# -*- coding: utf-8 -*-
import codecs

def read_from_file(fname):
    return codecs.open(fname, 'r', 'utf8').read().replace(u'\r', u'').split('\n')


WDAY_FILE = 'dictionaries/weekdays.txt'
HOUR_FILE = 'dictionaries/daytimes.txt'

NOUNS_FILE = 'dictionaries/good_nouns.txt'
ADJECTIVES_FILE = 'dictionaries/good_adjectives.txt'
CONNECTORS_FILE = 'dictionaries/connectors.txt'
BLESSINGS_FILE = 'dictionaries/blessings.txt'


WDAY = dict(zip(range(7), read_from_file(WDAY_FILE)))
HOUR = dict(zip(range(24), read_from_file(HOUR_FILE)))
NOUNS, ADJECTIVES, CONNECTORS, BLESSINGS = map(read_from_file, [NOUNS_FILE, ADJECTIVES_FILE, CONNECTORS_FILE, BLESSINGS_FILE])
    
