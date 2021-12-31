from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
import itertools
import sys

import attr
# a: 9:20
# b: 47:30

puzzle = Puzzle(year=2021, day=9)

# with open('ex9.txt') as infile:
#     lines = infile.readlines()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

hm = list()

for l in lines:
    _l = list()
    for c in l:
        try:
            _l.append(int(c))
        except:
            None
    hm.append(_l)

res = 0
low_points = list()
max_r = len(hm)
max_c = len(hm[0])
for i in range(max_r):
    for j in range(max_c):
        low = True
        for d in dirs:
            try:
                if hm[i][j] >= hm[i+d[0]][j+d[1]]:
                    low = False
                    break
            except:
                None
        if low:
            low_points.append((i, j))
            res += hm[i][j] + 1

print("part a: {}".format(res))
puzzle.answer_a = res

basins_sizes = list()

visited = set()

def rec_search(r, c):
    if (r, c) in visited:
        return 0

    if r < 0 or r > max_r or c < 0 or c > max_c:
        return 0

    try:
        visited.add((r, c))
        if hm[r][c] == 9:
            return 0
        else:
            return 1 + rec_search(r, c-1) + rec_search(r, c+1) + rec_search(r-1, c) + rec_search(r+1, c)
    except:
        return 0

for lp in low_points:
    row = lp[0]
    col = lp[1]
    basins_sizes.append(rec_search(row, col))

basins_sizes.sort()
res = basins_sizes[-1] * basins_sizes[-2] * basins_sizes[-3]

print("part b: {}".format(res))
puzzle.answer_b = res