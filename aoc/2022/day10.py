from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict
import os

# a: 
# b:  

day = 10

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

res_a = 0
res_b = 0

signal_strengths = []
# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
cycles_to_look_for = [20, 60, 100, 140, 180, 220]

X = 1
cycle = 1
nb_cycle = {
    'addx': 2,
    'noop': 1
}

H = 6
W = 40
CRT = [['.' for _ in range(W)] for _ in range(H)]

def draw(x, c):
    c -= 1
    x -= 1
    if c == 40:
        row = c // (W)
        col = c % (W)
        # print(x, c, row, col)
        # input()
    if x <= c % W <= x + 2:
        row = c // W
        col = c % W
        CRT[row][col] = '#'
    #     print(x, c, row, col)
    # else:
    #     print("no", x, c)


for l in lines:
    if l.startswith('addx'):
        op, v = l.strip().split(' ')
        v = int(v)
        for i in range(nb_cycle[op]):
            draw(X, cycle)
            # part a
            if i+1 == nb_cycle[op]:
                X += v
            if cycle in cycles_to_look_for:
                signal_strengths.append(cycle * X)
            
            # part b
            cycle += 1
    else:
        # noop
        # part a
        if cycle in cycles_to_look_for:
            signal_strengths.append(cycle * X)
        
        # part b
        draw(X, cycle)
        cycle += 1

# sum of signal strenghts
res_a = sum(signal_strengths)


print("part a: {}".format(res_a))
# print("part b: {}".format(res_b))

for r in CRT:
    for c in r:
        print(c, end='')
    print()
# puzzle.answer_a = res_a
# puzzle.answer_b = res_b