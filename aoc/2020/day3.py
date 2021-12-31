from aocd.models import Puzzle
from aocd import lines

puzzle = Puzzle(year=2020, day=3)

def traverse(right, down):
    nb_tree = 0
    row = 0
    col = 0

    map_size = len(lines[0])

    while row < len(lines):
        if lines[row][col] == '#':
            nb_tree += 1
        row += down
        col = (col + right) % map_size

    return nb_tree
    
print("part a: {}".format(traverse(3, 1)))

slopes = [(1, 1), (3, 1), (5,1), (7,1), (1,2)]

res_b = 1

for slope in slopes:
    res_b *= traverse(slope[0], slope[1])

print("part b: {}".format(res_b))