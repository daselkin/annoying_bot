def reverse_hebrew(txt):
    return u'\n'.join(
        map(lambda x: x[::-1], txt.split('\n'))
        )
