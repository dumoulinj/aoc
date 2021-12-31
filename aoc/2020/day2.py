from aocd.models import Puzzle
from aocd import lines

puzzle = Puzzle(year=2020, day=2)

nb_valid_a = 0
nb_valid_b = 0

for line in lines:
    line_split = line.split(' ')
    lh = line_split[0].split('-')
    l = (int)(lh[0])
    h = (int)(lh[1])
    
    c = line_split[1][:-1]

    password = line_split[2]

    _count_a = password.count(c)

    if _count_a >= l and _count_a <= h:
        nb_valid_a += 1
    
    if password[l-1] == c:
        if password[h-1] != c:
            nb_valid_b += 1
    elif password[h-1] == c:
        nb_valid_b += 1

    
print("part a: {}".format(nb_valid_a))
print("part b: {}".format(nb_valid_b))