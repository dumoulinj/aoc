from aocd.models import Puzzle
from aocd import lines
import sys

import attr
# a:  7:58
# b: 19:00

puzzle = Puzzle(year=2021, day=7)

l = lines[0]
#l = "16,1,2,0,4,2,7,1,2,14"
pos = [int(x) for x in l.split(',')]

m = sys.maxsize

fuel = m
_i = -1 
for i in pos:
    count = 0
    for j in pos:
        count += abs(i-j)
    
    fuel = min(fuel, count)

res = fuel
print("part a: {}".format(res))
puzzle.answer_a = res

fuel = m
_i = -1 
for i in range(max(pos)):
    count = 0
    for j in pos:
        k = abs(i-j)
        if k > 0:
            for _k in range(1, k+1):
                count += _k
    
    fuel = min(fuel, count)

res = fuel
print("part b: {}".format(res))
puzzle.answer_b = res