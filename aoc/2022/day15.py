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

day = 15

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

def draw():
    for y in range(-2, 28, 1):
        for x in range(-2, 26, 1):
            c = '.'
            if (x, y) in sensors:
                c = 'S'
            elif (x, y) in beacons:
                c = 'B'
            elif (x, y) in no_beacons:
                c = '#'
            elif (x, y) in candidates:
                c = 'C'
            print(c, end='')
        print()

sensors = dict()
beacons = set()
no_beacons = set()

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


y = 2000000
# y = 10

minxy = 0
maxxy = 4000000
# maxxy = 20 
candidates = defaultdict(int)

for l in lines:
    _l = l.split(' ')
    sx = int(_l[2].split('=')[1][:-1])
    sy = int(_l[3].split('=')[1][:-1])

    bx = int(_l[8].split('=')[1][:-1])
    by = int(_l[9].split('=')[1])

    dist = get_dist((sx, sy), (bx, by)) 

    sensors[(sx, sy)] = dist
    beacons.add((bx, by))

    for xx in range(sx-dist, sx+dist+1, 1):
        # for yy in range(sy-dist, sy+dist+1, 1):
        #     if get_dist((xx, yy), (sx, sy)) <= dist:
        #         if (xx, yy) != (bx, by):
        #             no_beacons.add((xx, yy))
        yy = y
        if get_dist((xx, yy), (sx, sy)) <= dist:
            if (xx, yy) != (bx, by):
                no_beacons.add((xx, yy))

    # draw()
    # input()
res_a = len([x for x in no_beacons if x[1] == y])
print("part a: {}".format(res_a))

def is_in_another_sensor_zone(candidate, sensor):
    for sk, sv in sensors.items():
        if sk != sensor and get_dist(candidate, sk) <= sv:
            return False
    return True

nbs = 0
nb_sensors = len(sensors)

for sk, sv in sensors.items():
    nbs += 1
    # print(nbs, nb_sensors)
    sx = sk[0]
    sy = sk[1]
    dist = sv

    in_zone = False
    for i in range(0, dist+2):
        for xx, yy in [(sx+dist-i+1, sy-i), (sx+dist-i+1, sy+i), (sx-dist+i-1, sy-i), (sx-dist+i-1, sy+i)]:
            if 0 <= xx <= maxxy and 0 <= yy <= maxxy:
                if is_in_another_sensor_zone((xx, yy), sk):
                    candidates[(xx, yy)] += 1

# print(candidates)

# res_b = [ck for ck, cv in candidates.items() if cv == nb_sensors_in_zone and 0 <= ck[0] < maxxy and 0 <= ck[1] <= maxxy][0]
res_b = max(candidates.keys(), key=(lambda key: candidates[key]))
res_b = res_b[0] * maxxy + res_b[1]

print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b