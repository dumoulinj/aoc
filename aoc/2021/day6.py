from aocd.models import Puzzle
from aocd import lines

import attr
# a: 11:43
# b: 20:00

puzzle = Puzzle(year=2021, day=6)

#lines = "3,4,3,1,2"
lantern_fishes = [int(x) for x in lines[0].split(',')]

def sim(days):
    fishes = lantern_fishes
    for i in range(days):
        nlf = list()
        for lf in fishes:
            lf = lf - 1
            if lf == -1:
                nlf.append(8)
                nlf.append(6)
            else:
                nlf.append(lf)
        fishes = nlf
    
    return len(fishes)

res = sim(80)
print("part a: {}".format(res))
puzzle.answer_a = res

def sim2(nb_days):
    days = [0 for i in range(9)]

    for lf in lantern_fishes:
        days[lf] += 1
    
    for i in range(nb_days):
        nb_0 = days[0]
        for d in range(1, 9):
            days[d-1] = days[d]
            days[d] = 0

        days[6] += nb_0
        days[8] += nb_0
    
    return sum(days)


# lines = "3,4,3,1,2"
# lantern_fishes = [int(x) for x in lines.split(',')]
lantern_fishes = [int(x) for x in lines[0].split(',')]

res = sim2(256)
print("part b: {}".format(res))
puzzle.answer_b = res