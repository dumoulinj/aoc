from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys

import attr
# a: 24:08
# b: 56:00

puzzle = Puzzle(year=2021, day=14)

#with open('ex14.txt') as infile:
#    lines = infile.readlines()

template = lines[0].strip()
first_letter = template[0]
last_letter = template[-1]

rules = dict()

for line in lines[2:]:
    a, b = line.strip().split(' -> ')
    rules[a] = b

# nb_steps = 10

# for i in range(nb_steps):
    # new_template = template
    # x = 0
    # for j in range(len(template)-1):
    #     p = template[j:j+2]
    #     if p in rules:
    #         x += 1
    #         new_template = new_template[:j+x] + rules[p] + new_template[j+x:]
    # template = new_template


# c = Counter(template)
# mc = c.most_common()
# m = mc[0]
# l = mc[-1]
#res = m[1] - l[1]

#print("part a: {}".format(res))
#puzzle.answer_a = res

nb_steps = 40

tuples = defaultdict(int)

for j in range(len(template)-1):
    tuples[template[j:j+2]] += 1


for i in range(nb_steps):
    new_tuples = deepcopy(tuples)
    for t in tuples.keys():
        if t in rules:
            nb = tuples[t]
            new_tuples[t] -= nb
            a = t[0] + rules[t]
            b = rules[t] + t[1]
            new_tuples[a] += nb
            new_tuples[b] += nb
            
    tuples = deepcopy(new_tuples)

letters = defaultdict(int)
for t, v in tuples.items():
    letters[t[0]] += v
    letters[t[1]] += v

for l, v in letters.items():
    if l == first_letter or l == last_letter:
        letters[l] = v // 2 + 1
    else:
        letters[l] = v // 2


vals = list(letters.values())
vals.sort()
_min = vals[0]
_max = vals[-1]

res = _max-_min


print("part b: {}".format(res))
puzzle.answer_b = res