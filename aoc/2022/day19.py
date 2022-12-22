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

day = 19

puzzle = Puzzle(year=2022, day=day)

exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
with open(exfile) as infile:
    lines = infile.readlines()

blueprints = list()
costs = list()

bp = 
cost = 

for l in lines:
    if l.strip() == '':
        # next bp
    elif l.startswith("Blueprint"):

    else:
    
# pack with one ore collecting robot to start

res_a = 0
print("part a: {}".format(res_a))

res_b = 0
print("part a: {}".format(res_b))