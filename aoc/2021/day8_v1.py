from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
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
unique_numbers = (1, 7, 4, 8)
not_unique = (0, 1, 5, 6, 8, 9)
lines = ["acedgfb cdfeb gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
#with open('ex8.txt') as infile:
#    lines = infile.readlines()

count = 0

outputs = list()

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
    nup = list()
    digits_sets = dict()
    for _p in p:
        c = len(_p)
        k = ''.join(sorted(_p))
        if c in unique:
            ctable[k] = nbs[c]
            ctable_2[nbs[c]] = k
        else:
            nup.append(k)
        
        if c not in digits_sets:
            digits_sets[c] = set(k)
        else:
            digits_sets[c] = digits_sets[c].union(set(k))

    ct = dict()
    # a -> diff entre 7 et 1
    _a = (digits_sets[counts[7]] - digits_sets[counts[1]]).pop()
    ct[_a] = 'a'

    # e
    s1 = digits_sets[counts[7]].union(digits_sets[counts[4]])
    s2 = digits_sets[counts[6]]

    _e = (s2 - s1).pop()
    ct[_e] = 'e'

    # g
    s1 = digits_sets[counts[7]].union(digits_sets[counts[4]])
    s2 = digits_sets[counts[8]]
    s2.remove(_e)

    _g = (s2-s1).pop()
    ct[_g] = 'g'

    # b
    s1 = digits_sets[counts[1]]
    s2 = digits_sets[counts[0]]
    s2.remove(_e)
    s2.remove(_g)
    s2.remove(_a)
    _b = (s2 - s1).pop()
    ct[_b] = 'b'

    # d
    s1 = digits_sets[counts[1]]
    s2 = digits_sets[counts[4]]
    s2.remove(_b)
    _d = (s2-s1).pop()
    ct[_d] = 'd'

    # f
    
    

    # f -> diff entre 1 et (2 - a) --> c 
    #   -> 1, 7
    # temp = ctable_2[2].replace(_a)
    # ct[set(ctable_2[1]) - set(ctable_2[1])] = 'f'

    print(ct)
    # e -> diff entre (9-c) et (0-c) et (6-c)

    # d -> dans 4 et 


    rctable = {
        "acedgfb": 8, 
        "cdfeb": 5, 
        "gcdfa": 2, 
        "fbcad": 3, 
        "dab": 7, 
        "cefabd": 9, 
        "cdfgeb": 6, 
        "eafb": 4, 
        "cagedb": 0, 
        "ab": 1 
    }

    ctable = dict()
    for k, v in rctable.items():
        _k = ''.join(sorted(k))
        ctable[_k] = v


    for o in outputs:
        d = ""
        for _o in o:
            __o = ''.join(sorted(_o))
            d += str(ctable[__o])
        res += int(d)


print("part a: {}".format(count))
#puzzle.answer_a = res

print("part b: {}".format(res))
# puzzle.answer_b = res