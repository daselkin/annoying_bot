from params import MAX_CHARS_PER_LINE

def split_line(l):
    tokens = l.split(' ')
    lines = [[]]
    for token in tokens:
        if sum(map(len, lines[-1])) + len(token) < MAX_CHARS_PER_LINE:
            lines[-1].append(token)
        else:
            lines.append([token])
    return u'\n'.join(map(lambda x: u' '.join(x), lines))
