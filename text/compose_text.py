# -*- coding: utf-8 -*-
import codecs
import random

from read_dictionaries import WDAY, HOUR, NOUNS, ADJECTIVES, CONNECTORS, BLESSINGS, ENDINGS
from linebreak import split_line
from params import MAX_ADJECTIVES, MAX_NOUNS, BLESSING_CHANCE

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
    
    return split_line(
        u'{time}{linebreak0}{epiteph}{linebreak1}{of}{goodstuff}{linebreak2}{blessing}{ending}'.format(
            time=time_txt,
            linebreak0=u' ' if num_epitephs > 0 else u'',
            epiteph=conjunct(random.sample(ADJECTIVES, num_epitephs)),
            linebreak1=', ' if num_epitephs > 0 else u' ',
            of=random.choice(CONNECTORS) if num_goodstuff > 0 else u'',
            goodstuff=conjunct(random.sample(NOUNS, num_goodstuff)),
            linebreak2=', ' if (num_goodstuff > 0 and has_blessing) else u' ',
            blessing=random.choice(BLESSINGS) if has_blessing else u'',
            ending=random.choice(ENDINGS)
            )
        )



