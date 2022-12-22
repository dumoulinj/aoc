import sys
from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict, deque
import os
import copy
import json
# a: 
# b:  

day = 22

puzzle = Puzzle(year=2022, day=day)

exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
with open(exfile) as infile:
    lines = infile.readlines()

def draw(pos):
    global maxx, maxy, pixels, m

    for y in range(1, maxy+1, 1):
        for x in range(1, maxx+1, 1):
            if (y, x) == pos:
                pixel = 'o'
            else:
                pixel = pixels[m[(y, x)]] if (y, x) in m else pixels[0] 
            print(pixel, end='')
        print()


pixels = ['|', '.', '#']

m = defaultdict(int)

y = 1
for y, l in enumerate(lines[:-2], 1):
    for x, c in enumerate(l, 1):
        if c in ['.', '#']:
            m[(y, x)] = pixels.index(c)

miny = 1
minx = 1

maxy = max([k[0] for k in m.keys()])
maxx = max([k[1] for k in m.keys()])

steps = list()
p = lines[-1].strip()
v = ''
for c in p:
    if c in ['L', 'R']:
        steps.append(int(v))
        v = ''
        steps.append(c)
    else:
        v += c

if v != '':
    steps.append(int(v))


# draw()
# print(steps)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
facing = 0

pos = (1, min([k[1] for k in m if k[0] == 1]))
draw(pos)
res_a = 0
print("part a: {}".format(res_a))

res_b = 0
print("part a: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b