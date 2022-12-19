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

exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
with open(exfile) as infile:
    lines = infile.readlines()


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

# def dfs(c):
#     if c in cubes:
#         return 1

#     visited.add(c)

#     ans = 0
#     for d in dirs:
#         xx = c[0] + d[0]
#         yy = c[1] + d[1]
#         zz = c[2] + d[2]

#         cc = (xx, yy, zz)

#         if cc not in visited and minx-1 <= xx <= maxx+1 and miny-1 <= yy <= maxy+1 and minz-1 <= zz <= maxz+1:
#             ans += dfs(cc)

#     return ans

# res_b = dfs((minx-1, miny-1, minz-1))

Q = deque()
Q.append((minx-1, miny-1, minz-1))

ans = 0
while Q:
    c = Q.pop()
    visited.add(c)

    if c in cubes:
        ans += 1
        continue

    for d in dirs:
        xx = c[0] + d[0]
        yy = c[1] + d[1]
        zz = c[2] + d[2]

        cc = (xx, yy, zz)

        if cc not in visited and minx-1 <= xx <= maxx+1 and miny-1 <= yy <= maxy+1 and minz-1 <= zz <= maxz+1:
            Q.append(cc)

res_b = ans

# for c in cubes:
#     for d in dirs:
#         i = 1
#         while True:
#             xx = c[0] + i * d[0]
#             yy = c[1] + i * d[1]
#             zz = c[2] + i * d[2]

#             if minx <= xx <= maxx and miny <= yy <= maxy and minz <= zz <= maxz:
#                 if (xx, yy, zz) in cubes:
#                     break
#             else:
#                 res_b += 1
#                 break

#             i += 1



print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b