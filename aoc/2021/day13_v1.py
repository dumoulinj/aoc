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

paper = list()

dots = list()
folds = list()

def do_fold(d, val, paper):
    temp_paper = [row[:] for row in paper]
    _max_y = len(paper)
    _max_x = len(paper[0])

    if d == 'x':
        # fold left
        for _y in range(_max_y):
            for _x in range(val+1, _max_x):
                if temp_paper[_y][_x] == 1:
                    temp_paper[_y][val-(_x-val)] = 1
                    temp_paper[_y][_x] = 0
        _max_x = val
    else:
        # fold up
        for _y in range(val+1, _max_y):
            for _x in range(_max_x):
                if temp_paper[_y][_x] == 1:
                    temp_paper[val-(_y-val)][_x] = 1
                    temp_paper[_y][_x] = 0
        _max_y = val
    
    paper = list()
    for _y in range(_max_y):
        paper.append(temp_paper[_y][:_max_x])
    
    return paper

def print_paper(paper):
    for r in paper:
        for c in r:
            if c == 1:
                print(c, end='')
            else:
                print(' ', end='')
        print()

max_x = 0
max_y = 0

for line in lines:
    if ',' in line:
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        dots.append((y, x))
    elif 'fold' in line:
        fold = line.replace('fold along ', '').strip().split('=')
        folds.append((fold[0], int(fold[1])))


max_x += 1
max_y += 1

for _y in range(max_y):
    row = list()
    for _x in range(max_x):
        row.append(0)
    paper.append(row)

for dot in dots:
    paper[dot[0]][dot[1]] = 1

for i, f in enumerate(folds):
    paper = do_fold(f[0], f[1], paper)
    if i == 0:
        res = sum([sum(l) for l in paper])

        print("part a: {}".format(res))
        puzzle.answer_a = res

print_paper(paper)