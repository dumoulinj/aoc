from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
import itertools
import sys

import attr
# a: 56min00s
# b: 1h08min10s

puzzle = Puzzle(year=2021, day=12)

res = 0
# with open('ex12.txt') as infile:
#     lines = infile.readlines()

links = dict()

START_END = ("start", "end")

for l in lines:
    a, b = l.strip().split('-')
    if a not in links:
        links[a] = list()
    
    if b not in links:
        links[b] = list()
    
    links[a].append(b)    
    links[b].append(a)

# def visit(c, path):
#     for nc in links[c]:
#         _path =  [x for x in path]
#         if nc not in links[_path[-1]]:
#             continue
#         if nc == "end":
#             solutions.add(''.join(_path))
#         elif nc != "start":
#             if nc.islower():
#                 if nc not in _path:
#                     _path.append(nc)
#                     visit1(nc, _path)
#             else:
#                 _path.append(nc)
#                 visit1(nc, _path)

def visit(c, path, sc):
    for nc in links[c]:
        _path =  [x for x in path]
        if nc not in links[_path[-1]]:
            continue
        if nc == "end":
            solutions.add(''.join(_path))
        elif nc != "start":
            if nc.islower():
                if sc:
                    if nc not in _path:
                        _path.append(nc)
                        visit(nc, _path, True)
                else:
                    if nc in _path:
                        nsc = True
                    else:
                        nsc = False

                    _path.append(nc)
                    visit(nc, _path, nsc)

            else:
                _path.append(nc)
                visit(nc, _path, sc)

solutions = set()
for c in links["start"]:
    p = list()
    p.append(c)
    visit(c, p, True)

res = len(solutions)
print("part a: {}".format(res))
# puzzle.answer_a = res

solutions = set()
for c in links["start"]:
    p = list()
    p.append(c)
    visit(c, p, False)

res = len(solutions)
print("part b: {}".format(res))
puzzle.answer_b = res