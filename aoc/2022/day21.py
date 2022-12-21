
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

day = 21

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

monkeys = dict()

for l in lines:
    _id, job = l.split(':')

    job = job.lstrip().split()

    if len(job) == 1:
        job = int(job[0])
    else:
        a = job[0]
        op = job[1]
        b = job[2]
        job = (a, op, b)

    monkeys[_id] = job
    
def yel(_id):
    m = monkeys[_id]
    if isinstance(m, int):
        return m 
    else:
        if m[1] == '+':
            return yel(m[0]) + yel(m[2])
        elif m[1] == '-':
            return yel(m[0]) - yel(m[2])
        elif m[1] == '*':
            return yel(m[0]) * yel(m[2])
        elif m[1] == '/':
            return yel(m[0]) // yel(m[2])

res_a = yel("root")
print("part a: {}".format(res_a))


def yel2(_id):
    m = monkeys[_id]
    if _id == 'humn':
        return 'x'

    if isinstance(m, int):
        return m

    a = yel2(m[0])
    b = yel2(m[2])

    if m[1] == '+':
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return '(' + str(a) + '+' + str(b) + ')'
    if m[1] == '-':
        if isinstance(a, int) and isinstance(b, int):
            return a - b
        else:
            return '(' + str(a) + '-' + str(b) + ')'
    if m[1] == '*':
        if isinstance(a, int) and isinstance(b, int):
            return a * b
        else:
            return '(' + str(a) + '*' + str(b) + ')'
    if m[1] == '/':
        if isinstance(a, int) and isinstance(b, int):
            return a // b
        else:
            return '(' + str(a) + '/' + str(b) + ')'

from sympy.parsing.sympy_parser import parse_expr
from sympy import simplify, solve, Eq, symbols

a, _, b = monkeys["root"]

x = symbols('x')
res_b = solve(simplify(parse_expr(yel2(a))) - yel2(b))[0]
print("part b: {}".format(res_b))
# puzzle.answer_a = res_a
# puzzle.answer_b = res_b