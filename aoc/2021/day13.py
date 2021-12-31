from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
import itertools
import sys

import attr
# a: 33:39
# b: 52:00

puzzle = Puzzle(year=2021, day=13)

#with open('ex13.txt') as infile:
#    lines = infile.readlines()

max_x = 0
max_y = 0

paper = dict()
partA = False
for line in lines:
    if ',' in line:
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        paper[(y, x)] = True
    elif 'fold' in line:
        fold_instruction = line.replace('fold along ', '').strip().split('=')
        d = fold_instruction[0]
        s = int(fold_instruction[1])

        to_add = list()
        to_remove = list()

        for k in paper.keys():
            r = k[0]
            c = k[1]
            if d == 'x' and c > s:
                # Fold left
                to_add.append([r, s-(c-s)])
                max_x = s
            elif d == 'y' and k[0] > s:
                # Fold up
                to_add.append([s-(r-s), c])
                max_y = s
        
        for ta in to_add:
            paper[(ta[0], ta[1])] = True
        
        if not partA:
            res = len([x for x in paper.keys() if x[0] <= max_y and x[1] <= max_x])
            print("part a: {}".format(res))
            partA = True

for r in range(max_y+1):
    for c in range(max_x+1):
        if (r, c) in paper:
            print('#', end='')
        else:
            print(' ', end='')
    print()