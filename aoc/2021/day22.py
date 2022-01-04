from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy

# a: 14:05
# b: 

puzzle = Puzzle(year=2021, day=22)

# with open('ex22.txt') as infile:
#    lines = infile.readlines()

# cubes = dict()
# for l in lines:
#     p1, p2 = l.strip().split(' ')
#     on_off = p1 == "on"
    
#     rx, ry, rz = p2.split(',')
#     x1, x2 = rx.split('..')
#     y1, y2 = ry.split('..')
#     z1, z2 = rz.split('..')

#     x1 = int(x1[2:])
#     x2 = int(x2)
#     y1 = int(y1[2:])
#     y2 = int(y2)
#     z1 = int(z1[2:])
#     z2 = int(z2)


#     limit = 50
#     for x in range(max(x1, -1*limit), min(x2, limit) + 1):
#         for y in range(max(y1, -1*limit), min(y2, limit) + 1):
#             for z in range(max(z1, -1*limit), min(z2, limit) + 1):
#                 cubes[(x, y, z)] = on_off

# res = sum(cubes.values())

# print("part a: {}".format(res))
# puzzle.answer_a = res

def do_intersect(a, b):
    ax1, ax2 = a[0]
    ay1, ay2 = a[1]
    az1, az2 = a[2]

    bx1, bx2 = b[0]
    by1, by2 = b[1]
    bz1, bz2 = b[2]

    if bx2 < ax1 or bx1 > ax2:
        return False
    if by2 < ay1 or by1 > ay2:
        return False
    if bz2 < az1 or bz1 > az2:
        return False
    
    return True

def get_intersect_range(a, b):
    ax1, ax2 = a[0]
    ay1, ay2 = a[1]
    az1, az2 = a[2]

    bx1, bx2 = b[0]
    by1, by2 = b[1]
    bz1, bz2 = b[2]
    
    ix1 = max(ax1, bx1)
    ix2 = min(ax2, bx2)

    iy1 = max(ay1, by1)
    iy2 = min(ay2, by2)

    iz1 = max(az1, bz1)
    iz2 = min(az2, bz2)

    return ((ix1, ix2), (iy1, iy2), (iz1, iz2))

def get_nb_points_in_range(a):
    ax1, ax2 = a[0]
    ay1, ay2 = a[1]
    az1, az2 = a[2]
    return (ax2-ax1+1) * (ay2-ay1+1) * (az2-az1+1)

cubes_on = list()
cubes_off = list()

for i, l in enumerate(lines):
    p1, p2 = l.strip().split(' ')
    on_off = p1 == "on"
    
    rx, ry, rz = p2.split(',')
    x1, x2 = rx.split('..')
    y1, y2 = ry.split('..')
    z1, z2 = rz.split('..')

    x1 = int(x1[2:])
    x2 = int(x2)
    y1 = int(y1[2:])
    y2 = int(y2)
    z1 = int(z1[2:])
    z2 = int(z2)

    a = ((x1, x2), (y1, y2), (z1, z2))

    new_cubes_on = list()
    new_cubes_off = list()

    if on_off:
        new_cubes_on.append(a)

    for b in cubes_on:
        if do_intersect(a, b):
            intersect_range = get_intersect_range(a, b)
            new_cubes_off.append(intersect_range)

    for b in cubes_off:
        if do_intersect(a, b):
            intersect_range = get_intersect_range(a, b)
            new_cubes_on.append(intersect_range)
    
    for c in new_cubes_on:
        cubes_on.append(c)

    for c in new_cubes_off:
        cubes_off.append(c)


res = 0
for c in cubes_on:
    res += get_nb_points_in_range(c)

for c in cubes_off:
    res -= get_nb_points_in_range(c)

print("part b: {}".format(res))
puzzle.answer_b = res