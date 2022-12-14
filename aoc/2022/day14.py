import sys
from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import Counter, defaultdict, deque
import os
import copy
import json
# a: 
# b:  

day = 14

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

cave = defaultdict(int)

maxx, maxy = 0, 0
minx, miny = sys.maxsize, 0 

for l in lines:
    rocks = l.strip().split(' -> ')

    for i in range(len(rocks) - 2 + 1):
        r1 = rocks[i]
        r2 = rocks[i+1]
        x1, y1 = r1.split(',')
        x2, y2 = r2.split(',')

        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        signx = 0
        signy = 0
        if x1 == x2:
            y12 = y2 - y1
            signy = (y12>0) - (y12<0)
            d = (1*signy, 0)
        elif y1 == y2:
            x12 = x2 - x1
            signx = (x12>0) - (x12<0)
            d = (0, 1*signx)
        else:
            assert False

        # print(x1, y1, x2, y2, signx, signy)

        while True:
            minx = min(minx, x1)
            maxx = max(maxx, x1)
            maxy = max(maxy, y1)
            cave[(x1, y1)] = 1
            if x1 == x2 and y1 == y2:
                break
            x1 += d[1]
            y1 += d[0]

def draw(cave):
    for i in range(miny, maxy + 1):
        for j in range(minx, maxx + 1):
            pixel = ['.', '#', 'o']
            print(pixel[cave[(j, i)]], end='')
        print()

start = (500, 0)

def run(cave):
    move = True
    while move:
        x, y = start
        move = False
        while y < maxy:
            if cave[(x, y+1)] == 0:
                y += 1
            else:
                if cave[(x-1), (y+1)] == 0:
                    x -= 1
                    y += 1
                elif cave[(x+1), (y+1)] == 0:
                    x += 1
                    y += 1
                else:
                    if (x, y) == start:
                        break
                    else:
                        cave[(x, y)] = 2
                        move = True
                        break
    return cave

endcave = run(cave.copy())
# draw(endcave)
res_a = Counter(endcave.values())[2]
print("part a: {}".format(res_a))

# Prep for part b
inf = 1000
for i in range(inf):
    cave[(minx - i, maxy + 2)] = 1
    cave[(minx + i, maxy + 2)] = 1
    cave[(maxx + i, maxy + 2)] = 1
    cave[(maxx - i, maxy + 2)] = 1

minx -= inf
maxx += inf
maxy += 2

endcave = run(cave.copy())
# draw(endcave)
res_b = Counter(endcave.values())[2] + 1
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b