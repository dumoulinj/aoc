from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys

import attr
# a: 50:10
# b: 1:08:29

puzzle = Puzzle(year=2021, day=17)

#with open('ex17.txt') as infile:
#    lines = infile.readlines()


# target area: x=150..171, y=-129..-70
minx = 150
maxx = 171

maxy = -70
miny = -129

# minx = 20
# maxx = 30

# maxy = -5
# miny = -10


h = miny

solutions = set()

for _vy in range(-1000, 8256):
    for _vx in range(-10*maxx, 10*maxx):
        vx = _vx
        vy = _vy
        px = 0
        py = 0


        _h = py
        while True:
            px += vx

            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1

            py += vy
            _h = max(_h, py)
            vy -= 1

            #print(px, py)

            if minx <= px <= maxx and maxy >= py >= miny:
                h = max(h, _h)
                # if h == _h:
                #     print("New solution:")
                #     print(vx, vy, h)
                solutions.add((_vx, _vy))
                break
            elif px > maxx or py < miny:
                break
        print(len(solutions))
        

res = h 
print("part a: {}".format(res))
puzzle.answer_a = res

res = len(solutions)
print("part b: {}".format(res))
puzzle.answer_b = res