# -*- coding: utf-8 -*-
import codecs
import random

from read_dictionaries import WDAY, HOUR, NOUNS, ADJECTIVES, CONNECTORS, BLESSINGS


MAX_ADJECTIVES = 3
MAX_NOUNS = 3

BLESSING_CHANCE = 4

def conjunct(lst):
    if len(lst) == 0:
        return u''
    elif len(lst) == 1:
        return lst[0]
    else:
        return u', '.join(lst[:-1]) + u' ו' + lst[-1]
    

def annoying_text(tm):
    time_txt = random.choice([
        u'יום {}'.format(WDAY[(tm.tm_wday+1)%7]),
        HOUR[tm.tm_hour]
        ])
    
    num_epitephs = random.randint(0, MAX_ADJECTIVES)
    num_goodstuff = random.randint( (0 if num_epitephs > 0 else 1), MAX_NOUNS)
    has_blessing = random.randint(1, BLESSING_CHANCE) == 1
    
    return u'{time}{linebreak0}{epiteph}{linebreak1}{of}{goodstuff}{linebreak2}{blessing}'.format(
        time=time_txt,
        linebreak0=u' ' if num_epitephs > 0 else u'',
        epiteph=conjunct(random.sample(ADJECTIVES, num_epitephs)),
        linebreak1='\n' if num_epitephs > 0 else u' ',
        of=random.choice(CONNECTORS) if num_goodstuff > 0 else u'',
        goodstuff=conjunct(random.sample(NOUNS, num_goodstuff)),
        linebreak2='\n' if num_goodstuff > 0 else u' ',
        blessing=random.choice(BLESSINGS) if has_blessing else u''
        )



