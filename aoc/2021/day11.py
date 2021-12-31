from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
import itertools
import sys

import attr
# a: 44:25
# b: 49:00

puzzle = Puzzle(year=2021, day=11)

res = 0
#with open('ex11.txt') as infile:
#    lines = infile.readlines()

levels = list()

for l in lines:
    _l = list()
    for c in l:
        try:
            _l.append(int(c))
        except:
            None
    levels.append(_l)

max_r = len(levels)
max_c = len(levels[0])


nb_steps = 100

directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1)]

nb_flashes = 0

flashed = set()

nboctopuses = max_r * max_c

def flash(r, c):
    if (r, c) not in flashed:
        if levels[r][c] > 9:
            flashed.add((r, c))
            for d in directions:
                nr = r+d[0]
                nc = c+d[1]
                if 0<= nr < max_r and 0<=nc < max_c and (nr, nc) not in flashed:
                    levels[nr][nc] += 1
                    flash(nr, nc)

s = 1
while True:
    for r in range(max_r):
        for c in range(max_c):
            levels[r][c] += 1

    for r in range(max_r):
        for c in range(max_c):
            if levels[r][c] > 9:
                flash(r, c)

    for f in flashed:
        levels[f[0]][f[1]] = 0      

    _nb_flashes = len(flashed)

    if _nb_flashes == nboctopuses:
        break

    if s <= nb_steps:
        nb_flashes += _nb_flashes

    flashed = set()

    s += 1

res = nb_flashes
print("part a: {}".format(res))
puzzle.answer_a = res

res = s
print("part b: {}".format(res))
puzzle.answer_b = res