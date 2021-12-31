from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
import itertools
import sys

import attr
# a: 21min
# b: 

puzzle = Puzzle(year=2021, day=8)


clock_d = {
    "abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9
}
clock_a = [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"
]

nbs = [(), (), (1), (7), (4), (2, 3, 5), (0, 6, 9), (8)]
counts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

unique = (2, 3, 4, 7)
not_unique = (5, 6)

unique_numbers = (1, 7, 4, 8)
not_unique_numbers = (0, 2, 3, 5, 6, 9)

#lines = ["acedgfb cdfeb gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
#with open('ex8.txt') as infile:
#    lines = infile.readlines()

count = 0

outputs = list()

def get_nb_sim(a, b):
    _a = set(a)
    _b = set(b)

    return len(_a & _b)

def get_nb_sims(values):
    nb_sims = list()
    for i in range(9):
        t = list()
        for j in range(9):
            t.append(get_nb_sim(values[i], values[j]))
        nb_sims.append(t)
    
    return nb_sims

REF_NB_SIMS = get_nb_sims(clock_a)

def verify(s1):
    for i in range(9):
        for j in range(9):
            if s1[i][j] != REF_NB_SIMS[i][j]:
                return False
    return True

def get_output(o):
    d = ""
    for _o in o:
        __o = ''.join(sorted(_o))
        d += str(ctable[__o])
    return int(d)

def find_ctable(p_235, p_069):
    for p_a in p_235:
        _2 = p_a[0]
        _3 = p_a[1]
        _5 = p_a[2]

        ctable[_2] = 2
        ctable[_3] = 3
        ctable[_5] = 5

        ctable_2[2] = _2
        ctable_2[3] = _3
        ctable_2[5] = _5

        for p_b in p_069:
            _0 = p_b[0]
            _6 = p_b[1]
            _9 = p_b[2]
            ctable[_0] = 0
            ctable[_6] = 6
            ctable[_9] = 9

            ctable_2[0] = _0
            ctable_2[6] = _6
            ctable_2[9] = _9

            _nb_sims = get_nb_sims(ctable_2)

            if verify(_nb_sims):
                return True
    
    return False

res = 0
for l in lines:
    p, o = l.split(' | ')
    p = p.split()
    o = o.split()
    outputs.append(o)
    for _o in o:
        c = len(_o)
        if c in unique:
            count += 1

    ctable = dict()
    ctable_2 = dict()
    digits_sets = dict()

    _235 = list()
    _069 = list()
    for _p in p:
        c = len(_p)
        k = ''.join(sorted(_p))
        if c in unique:
            ctable[k] = nbs[c]
            ctable_2[nbs[c]] = k
        else:
            if c == 5:
                _235.append(k)
            else:
                _069.append(k)
    
    p_235 = list(itertools.permutations(_235))
    p_069 = list(itertools.permutations(_069))

    if find_ctable(p_235, p_069):
        res += get_output(o)
    else:
        print("We have a problem")
    

        
print("part a: {}".format(count))
puzzle.answer_a = res

print("part b: {}".format(res))
puzzle.answer_b = res