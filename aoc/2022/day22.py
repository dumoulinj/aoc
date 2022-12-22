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

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

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


pixels = [' ', '.', '#']

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

def run(pos, facing):
    global steps, m, dirs, pixels

    for step in steps:
        if step == 'L':
            facing -= 1
            if facing == -1:
                facing = 3
        elif step == 'R':
            facing = (facing + 1) % 4
        else:
            for i in range(step):
                new_pos = (pos[0] + dirs[facing][0], pos[1] + dirs[facing][1])
                if new_pos not in m:
                    if facing == 0:
                        # Right
                        new_pos = (new_pos[0], min([k[1] for k in m.keys() if k[0] == new_pos[0]]))
                    elif facing == 1:
                        # Down 
                        new_pos = (min([k[0] for k in m.keys() if k[1] == new_pos[1]]), new_pos[1])
                    elif facing == 2:
                        # Left 
                        new_pos = (new_pos[0], max([k[1] for k in m.keys() if k[0] == new_pos[0]]))
                    elif facing == 3:
                        # Up 
                        new_pos = (max([k[0] for k in m.keys() if k[1] == new_pos[1]]), new_pos[1])
                    
                if m[new_pos] == pixels.index('#'):
                    break
                else:
                    pos = new_pos
                
                # draw(pos)
                # input()
    
    return 1000 * pos[0] + 4 * pos[1] + facing

facing = 0
pos = (1, min([k[1] for k in m if k[0] == 1]))

res_a = run(pos, facing)
print("part a: {}".format(res_a))

def run2(pos, facing):
    global steps, m, dirs, pixels

    for step in steps:
        if step == 'L':
            facing -= 1
            if facing == -1:
                facing = 3
        elif step == 'R':
            facing = (facing + 1) % 4
        else:
            for i in range(step):
                new_pos = (pos[0] + dirs[facing][0], pos[1] + dirs[facing][1])
                if new_pos not in m:
                    if facing == 0:
                        # Right

                        # C1 -> I6 (2)
                        # I1 -> C6 (2)

                        # I6 -> C1 (2)
                        # C6 -> I1 (2)

                        # C4 -> C6 (1)
                        # I4 -> A6 (1)
                        new_pos = (new_pos[0], min([k[1] for k in m.keys() if k[0] == new_pos[0]]))
                    elif facing == 1:
                        # Down 

                        # G2 -> I5 (3)
                        # I2 -> G5 (3)

                        # G3 -> G5 (0)
                        # I3 -> A5 (0)

                        # G5 -> I2 (3)
                        # I5 -> G2 (3)

                        # G6 -> G2 (0)
                        # I6 -> A2 (0)

                        new_pos = (min([k[0] for k in m.keys() if k[1] == new_pos[1]]), new_pos[1])
                    elif facing == 2:
                        # Left 

                        # A1 -> A3 (1)
                        # G1 -> C3 (1)

                        # A2 -> I6 (3)
                        # G2 -> G6 (3)

                        # A5 -> I3 (3)
                        # G5 -> G3 (3)

                        new_pos = (new_pos[0], max([k[1] for k in m.keys() if k[0] == new_pos[0]]))
                    elif facing == 3:
                        # Up 

                        # A1 -> C2 (1)
                        # C1 -> A2 (1)

                        # C2 -> A1 (1)
                        # A2 -> C1 (1)

                        # A3 -> A1 (0)
                        # C3 -> G1 (0)

                        # A6 -> I4 (2)
                        # C6 -> c4 (2)
                        new_pos = (max([k[0] for k in m.keys() if k[1] == new_pos[1]]), new_pos[1])
                    
                if m[new_pos] == pixels.index('#'):
                    break
                else:
                    pos = new_pos
                
                # draw(pos)
                # input()
    
    return 1000 * pos[0] + 4 * pos[1] + facing

res_b = run2(pos, facing)
print("part a: {}".format(res_b))

puzzle.answer_a = res_a
# puzzle.answer_b = res_b