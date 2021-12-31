from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys
import math
from enum import Enum

import attr
# a:
# b:

puzzle = Puzzle(year=2021, day=23)

# with open('ex23.txt') as infile:
#    lines = infile.readlines()


class CellType(Enum):
    HALL = 1
    RA = 2
    RB = 3
    RC = 4
    RD = 5


@attr.s
class Cell(object):
    cell_type = attr.ib()
    occupied = attr.ib(init=True, default=False)
    left = attr.ib(init=False, default=None)
    right = attr.ib(init=False, default=None)
    up = attr.ib(init=False, default=None)
    down = attr.ib(init=False, default=None)

class AmphipodType(Enum):
    A = 1
    B = 2
    C = 3
    D = 4

@attr.s
class Amphipod(object):
    amphipod_type = attr.ib()
    cell = attr.ib()
    found_place = attr.ib(init=True, default=False)

@attr.s
class Hotel(object):
    amphipods = attr.ib()

    def init(self):
        ra1 = Cell(CellType.RA, occupied=True)
        ra2 = Cell(CellType.RA, occupied=True)
        ra1.down = ra2
        ra2.up = ra1

        rb1 = Cell(CellType.RB, occupied=True)
        rb2 = Cell(CellType.RB, occupied=True)
        rb1.down = rb2
        rb2.up = rb1

        rc1 = Cell(CellType.RC, occupied=True)
        rc2 = Cell(CellType.RC, occupied=True)
        rc1.down = rc2
        rc2.up = rc1

        rd1 = Cell(CellType.RD, occupied=True)
        rd2 = Cell(CellType.RD, occupied=True)
        rd1.down = rd2
        rd2.up = rd1

        hallway = list()
        for _ in range(11):
            c = Cell(CellType.HALL)
            hallway.append(c)
        
        for i in range(11):
            if i > 0:
                hallway[i].left = hallway[i-1]
            if i < 10:
                hallway[i].right = hallway[i+1]
        
        hallway[2].down = ra1
        ra1.up = hallway[2]

        hallway[4].down = rb1
        rb1.up = hallway[4]

        hallway[6].down = rc1
        rc1.up = hallway[6]

        hallway[8].down = rd1
        rd1.up = hallway[8]

        self.amphipods = [
            Amphipod(AmphipodType.A, ra1),
            Amphipod(AmphipodType.A, ra2, True),
            Amphipod(AmphipodType.B, rb1),
            Amphipod(AmphipodType.B, rb2),
            Amphipod(AmphipodType.C, rc1),
            Amphipod(AmphipodType.C, rc2, True),
            Amphipod(AmphipodType.D, rd1),
            Amphipod(AmphipodType.D, rd2)
        ]



ENERGY = {
    AmphipodType.A: 1,
    AmphipodType.B: 10,
    AmphipodType.C: 100,
    AmphipodType.D: 1000
}

hotel = Hotel()
hotel.init()

res = 0
print("part a: {}".format(res))
#puzzle.answer_a = res 

print("part b: {}".format(res))
#puzzle.answer_b = res 