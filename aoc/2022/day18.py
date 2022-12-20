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

day = 18

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()


dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

cubes = set() 
connected = []

nb_not_connected = len(lines) * 6

minx = sys.maxsize
maxx = 0

miny = sys.maxsize
maxy = 0

minz = sys.maxsize
maxz = 0

for i, l in enumerate(lines):
    _l = l.strip().split(',')
    cube = tuple([int(v) for v in _l])

    minx = min(minx, cube[0])
    miny = min(miny, cube[1])
    minz = min(minz, cube[2])

    maxx = max(maxx, cube[0])
    maxy = max(maxy, cube[1])
    maxz = max(maxz, cube[2])

    for d in dirs:
        if (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2]) in cubes:
            nb_not_connected -= 2

    cubes.add(cube)


res_a = nb_not_connected
print("part a: {}".format(res_a))

print(minx, miny, minz)
print(maxx, maxy, maxz)

res_b = 0
visited = set()

Q = deque()
Q.append((minx-1, miny-1, minz-1))
Q.append((maxx+1, maxy+1, maxz+1))

ans = 0
while Q:
    c = Q.popleft()
    
    if not(minx-1 <= c[0] <= maxx+1 and miny-1 <= c[1] <= maxy+1 and minz-1 <= c[2] <= maxz+1):
        continue

    if c in visited:
        continue

    if c in cubes:
        ans += 1
        continue

    visited.add(c)

    for d in dirs:
        xx = c[0] + d[0]
        yy = c[1] + d[1]
        zz = c[2] + d[2]

        cc = (xx, yy, zz)

        Q.append(cc)

res_b = ans

print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b