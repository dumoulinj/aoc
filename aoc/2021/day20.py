from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys

import attr
# a: 
# b: 

puzzle = Puzzle(year=2021, day=20)

with open('ex20.txt') as infile:
   lines = infile.readlines()


algo = lines[0].strip()
#assert algo == "#..##..#.#.#.###.#..##.####..##..##.##.#.###.......##..#..#.#.#.#..#...##....#.#.##.###....###.#.##.##..##.#...##.##...#...##......##.#...#.......##.#.#..####.##..#.#.#.....##.....#....#.#.#.##..##..##.##.....###...#.#..###.#######.#.....###....#......#.###.#...#.#####.#.#.###..#...##.##.#..#...######.###.#.##...####..####.###...####........##...##.##.####...##.#.#...##.#####.#....#.....##..#......###..###.#.#..###..#.####......#.....#.#.#.###..#.#..#..#...##..##..#.##....#....#.##..###..#....##.##..#.###.."

DX = [-1, 0, 1]

def convert(pixels):
    bn = ""
    for p in pixels:
        if p == '.':
            bn += '0'
        else:
            bn += '1'
    return int(bn, 2)

def get_output_pixel(pixels):
    n = convert(pixels)
    return algo[n]

def print_picture(p):
    min_r = min([r for r, c in p.keys()])
    max_r = max([r for r, c in p.keys()])

    min_c = min([c for r, c in p.keys()])
    max_c = max([c for r, c in p.keys()])

    for r in range(min_r, max_r +1):
        for c in range(min_c, max_c +1):
            if (r,c) in p:
                print(p[(r, c)], end='')
            else:
                print('.', end='')
        print()

assert convert("...#...#.") == 34
#assert get_output_pixel("...#...#.") == "#"


picture = dict()
lines = [l.strip() for l in lines[2:]]

# def add_ext(p, n):
#     min_r = min([r for r, c in p.keys()])
#     max_r = max([r for r, c in p.keys()])

#     min_c = min([c for r, c in p.keys()])
#     max_c = max([c for r, c in p.keys()])
#     for r in range(min_r-n, max_r+n+1):
#         for c in range(min_c-n, max_c+n+1):
#             if min_r <= r < max_r+1 and min_c <= c < max_c+1:
#                 pass
#             else:
#                 p[(r, c)] = '.'

for r in range(len(lines)):
    for c in range(len(lines[0])):
        picture[(r, c)] = lines[r][c]

# add_ext(picture, 2)

new_picture = None
nb_steps = 50
for n in range(nb_steps):
    print(n)
    new_picture = dict()

    min_r = min([r for r, c in picture.keys()])
    max_r = max([r for r, c in picture.keys()])

    min_c = min([c for r, c in picture.keys()])
    max_c = max([c for r, c in picture.keys()])

    for r in range(min_r-2, max_r+3):
        for c in range(min_c-2, max_c+3):
            pixels = ""
            for dr in DX:
                for dc in DX:
                    rr = r+dr
                    cc = c + dc
                    if (rr, cc) in picture:
                        prr = picture[(rr, cc)]
                    else:
                        if n % 2 == 0:
                            prr = '.'
                        else:
                            prr = '#'

                    pixels += prr
            new_pixel = get_output_pixel(pixels)
            new_picture[(r, c)] = new_pixel
        
    picture = deepcopy(new_picture)
    # print_picture(picture)
    # print()

res = "".join(picture.values()).count('#')

print("part a: {}".format(res))
#puzzle.answer_a = res

print("part b: {}".format(res))
puzzle.answer_b = res