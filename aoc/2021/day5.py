from aocd.models import Puzzle
from aocd import lines

import attr
# a: 28min42s
# b: 1h02min55s

@attr.s
class Vent_line(object):
    x1: int = attr.ib()
    x2: int = attr.ib()
    y1: int = attr.ib()
    y2: int = attr.ib()

puzzle = Puzzle(year=2021, day=5)
vent_lines = list()
field = list()

max_x = 0
max_y = 0

#lines = ("0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2")

for line in lines:
    a, b = line.split(' -> ')
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    max_x = max(max_x, x1)
    max_x = max(max_x, x2)
    max_y = max(max_y, y1)
    max_y = max(max_y, y2)
    vent_line = Vent_line(x1, x2, y1, y2)
    vent_lines.append(vent_line)

for i in range(max_y+1):
    row = list()
    for j in range(max_x+1):
        row.append(0)
    field.append(row)

for v in vent_lines:
    if v.x1 == v.x2:
        y_sign = 1 if v.y1 < v.y2 else -1

        for y in range(v.y1, v.y2 + y_sign, y_sign):
            field[y][v.x1] += 1
    if v.y1 == v.y2:
        x_sign = 1 if v.x1 < v.x2 else -1

        for x in range(v.x1, v.x2 + x_sign, x_sign):
            field[v.y1][x] += 1

res = 0
for i in range(max_y+1):
    for j in range(max_x+1):
        if field[i][j] > 1:
            res += 1

print("part a: {}".format(res))
puzzle.answer_a = res

# part 2
field = list()
for i in range(max_y+1):
    row = list()
    for j in range(max_x+1):
        row.append(0)
    field.append(row)

for v in vent_lines:
    if v.x1 == v.x2:
        y_sign = 1 if v.y1 < v.y2 else -1

        for y in range(v.y1, v.y2 + y_sign, y_sign):
            field[y][v.x1] += 1
    if v.y1 == v.y2:
        x_sign = 1 if v.x1 < v.x2 else -1

        for x in range(v.x1, v.x2 + x_sign, x_sign):
            field[v.y1][x] += 1
        
    # diagonal
    x_diff = v.x1 - v.x2
    y_diff = v.y1 - v.y2
    if abs(x_diff) == abs(y_diff):
        # print(v)
        x_sign = 1 if x_diff < 0 else -1
        y_sign = 1 if y_diff < 0 else -1

        for i in range(abs(x_diff)+1):
            _x = v.x1+(i*x_sign)
            _y = v.y1+(i*y_sign)
            # print("i: {}, _x: {}, _y: {}".format(i, _x, _y))
            field[_y][v.x1+(i*x_sign)] += 1

#print(field)

res = 0
for i in range(max_y+1):
    for j in range(max_x+1):
        #print(field[i][j])
        if field[i][j] > 1:
            res += 1

print("part b: {}".format(res))
puzzle.answer_b = res