from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys
import json

import attr
# a:
# b: 

puzzle = Puzzle(year=2021, day=18)

#with open('ex17.txt') as infile:
#    lines = infile.readlines()

@attr.s
class Pair(object):
    left = attr.ib()
    right = attr.ib()
    parent = attr.ib()
    val:int = attr.ib()


def add(a, b):
    # Addition
    # [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]] 
    l = list()
    l.append(a)
    l.append(b)
    return l

def enum_list(l, depth, d):
    # def _enum_list(l,level=1):
    #     for e in l:
    #         if isinstance(e,list):
    #             yield from _enum_list(e,level+1)
    #         else:
    #            yield e,level
    # yield from _enum_list(l)
    found = False
    after = list()
    left = 0
    right = 0
    left_list = list()
    right_list = list()
    left_found = False
    right_found = False
    for _l in l:
        if not found:
            if depth == 4 and isinstance(_l, list):
                found = True
                left = _l[0]
                right = _l[1]

                reverse_left = d[3]
                reverse_left.reverse()
                for _x in reverse_left:
                    print(_x)
            else:
                d[depth].append(_l)
                if isinstance(_l, list):
                    enum_list(_l, depth+1, d)
        else:
            if isinstance(_l, int) and not right_found:
                right += _l
                right_found = True
            else:
                right_list.append(_l)

        
    return add(left_list, right_list)


def explode(l):
    d = defaultdict(list)
    enum_list(l, 1, d)
    print(d)


def split(n):
    return [n//2, (n//2) + 1]

def test_add():
    _a = "[1,2]"
    _b = "[[3,4],5]"

    a = json.loads(_a)
    b = json.loads(_b)

    assert add(a, b) == [[1,2],[[3,4],5]]

def create_pairs(l):
    for _l in l:
        print(_l)

def test_explode():
    l = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    # explode(l)
    create_pairs(l)

test_add()
test_explode()


# Reduction
# To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:
#  - If any pair is nested inside four pairs, the leftmost such pair explodes.
#  - If any regular number is 10 or greater, the leftmost such regular number splits.

# if nested 4 times
# -> leftmost explodes
    # explosion:
    # L + first number on the left (if any)
    # R + first number on the right (if any)
    # then the exploding pair = 0

# if not exploded
    # if number >= 10
    # -> leftmost splits

# res = 0
# print("part a: {}".format(res))
# #puzzle.answer_a = res

# res = 0
# print("part b: {}".format(res))
# #puzzle.answer_b = res