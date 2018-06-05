from itertools import *
from math import sqrt

GRADIENT = [15, 128, 240]

def best_complement_color(pixels):
    if type(pixels[0][1]) == int:
        colors = GRADIENT
        distance = lambda x,y: abs(x-y)
    else:
        colors = list(product(*[GRADIENT for i in range(len(pixels[0][1]))]))
        distance = lambda x,y: sqrt(sum( map(lambda (v, u): (v-u)**2, zip(x, y) ) ))

    color_deltas = {c: 0 for c in colors}
    for (amt, col) in pixels:
        for complement in colors:
            color_deltas[complement] += amt * distance(col, complement)

    
    return max(color_deltas.items(), key=lambda (k,v): v)[0]
