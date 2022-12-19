
from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict, deque
import os
import copy
import json
# a: 
# b:  

day = 17

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

pattern = lines[0].strip()
max_pattern = len(pattern)

LEFT_WALL = 0
RIGHT_WALL = 8
max_r = 0
# starts
#   - L + 2
#   - max_h + 3 

nb_rocks = 0

tower = defaultdict(int)

SHAPES = ['-', '+', 'j', 'l', 'o']
NB_SHAPES = len(SHAPES)

HEIGHTS = {
    '-': 1,
    '+': 3,
    'j': 3,
    'l': 4,
    'o': 2
}

WIDTHS = {
    '-': 4,
    '+': 3,
    'j': 3,
    'l': 1,
    'o': 2
}

PIXELS = {
    '-': [(0, 0), (0, 1), (0, 2), (0, 3)],
    '+': [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    'j': [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    'l': [(0, 0), (1, 0), (2, 0), (3, 0)],
    'o': [(0, 0), (0, 1), (1, 0), (1, 1)] 
}

CHECK_LEFT = {
    '-': [0],
    '+': [0, 1, 4],
    'j': [0, 3, 4],
    'l': [0, 1, 2, 3],
    'o': [0, 2] 
}

CHECK_RIGHT = {
    '-': [3],
    '+': [0, 3, 4],
    'j': [2, 3, 4],
    'l': [0, 1, 2, 3],
    'o': [1, 3] 
}

CHECK_DOWN = {
    '-': [0, 1, 2, 3],
    '+': [0, 1, 3],
    'j': [0, 1, 2],
    'l': [0],
    'o': [0, 1] 
}

CHECK = {
    '<': CHECK_LEFT,
    '>': CHECK_RIGHT,
    'v': CHECK_DOWN
}

MOVES = {
    '<': (0, -1),
    '>': (0, 1),
    'v': (-1, 0)
}

APPEARS = (3, 2)

def draw(crt_shape_coords):
    for r in range(max_r + 9, -1, -1):
        for c in range(9):
            pixel = '.'
            if c == 0 or c == 8:
                pixel = '+' if r == 0 else '|'
            elif r == 0:
                pixel = '-'
            else:
                if (r, c) in crt_shape_coords:
                    pixel = '@'
                elif tower[(r, c)] == 1:
                    pixel = '#'

            print(pixel, end='')
        print()

def move(rock, m):
    new_rock = [(r[0]+MOVES[m][0], r[1]+MOVES[m][1]) for r in rock]

    for r in new_rock:
        if tower[r] == 1 or r[1] in [LEFT_WALL , RIGHT_WALL] or r[0] == 0:
            return False

    return new_rock

to_draw = False
# to_draw = True

shape_idx = 0
next_move = 0

def cycle(list):
    # list to store shortest cycles
    shortest = [] 
    # return single integer and non-repeating lists
    if len(list) <= 1: return list
    if len(set(list)) == len(list): return list
    # loop through the list expanding and comparing 
    # groups of elements until a sequence is seen 
    for x in range(len(list)):
        if list[0:x] == list[x:2*x]:
            shortest = list[0:x] 
    return shortest 

DP = []

goal = 2022
goal = 1000000000000
while True:
    # if nb_rocks == 2022:
    if nb_rocks == goal:
        break
    
    if nb_rocks % 1e6 == 0:
        print(nb_rocks, '{}%'.format(nb_rocks / goal * 100))
    
    rock_id = SHAPES[shape_idx]
    rock = []

    r = max_r + APPEARS[0] + 1
    c = APPEARS[1] + 1

    for p in PIXELS[rock_id]:
        rock.append((r+p[0], c+p[1]))

    if to_draw:
        draw(rock)
        input()

    go_down = False
    while True:
        if go_down:
            # Go down
            if to_draw:
                print('v')
            new_rock = move(rock, 'v')

            if new_rock == False:
                for rp in rock:
                    tower[rp] = 1
                
                nb_rocks += 1

                max_new_r = max([rp[0] for rp in rock])
                min_new_r = min([rp[0] for rp in rock])
                # max_r = max(max_r, max_new_r)
                
                # DP.append(max_r)
                if max_new_r > max_r:
                    diff = max_new_r - max_r
                    DP.append(diff)
                    repeating_sequence = cycle(DP[1:])
                    if len(repeating_sequence) != 0 and len(repeating_sequence) != len(DP) - 1:
                        print("Repeating sequence!")
                        print(repeating_sequence)

                    max_r = max_new_r

                # Check if new line
                # for _r in (min_new_r, max_new_r + 1, 1):
                _r = max_r
                if all([tower[(_r, c)] == 1 for c in range(LEFT_WALL+1, RIGHT_WALL, 1)]):
                    print("Nouvelle ligne!")
                    print(_r, nb_rocks)
                    nb = goal // nb_rocks
                    idx = goal - nb


                # Check if pattern
                if max_r % 2 == 0:
                    pattern_found = True
                    for i in range(1, (max_r // 2) + 1, 1):
                        _t = [tower[i, j] == tower[(max_r//2 + i, j)] for j in range(LEFT_WALL+1, RIGHT_WALL, 1)]
                        if not all(_t):
                            pattern_found = False
                            # break
                    
                    if pattern_found:
                        print("Pattern found!")
                        print(nb_rocks)

                shape_idx = (shape_idx + 1) % NB_SHAPES
                break
            else:
                rock = new_rock

            go_down = False
        else:
            if to_draw:
                print(pattern[next_move])
            new_rock = move(rock, pattern[next_move])
            next_move = (next_move + 1) % max_pattern

            if new_rock:
                rock = new_rock

            go_down = True

        if to_draw:
            draw(rock)
            input()


res_a = max_r
print("part a: {}".format(res_a))

res_b = 0
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b