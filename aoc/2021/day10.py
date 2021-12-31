from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
import itertools
import sys

import attr
# a: 22:03
# b: 33:15

puzzle = Puzzle(year=2021, day=10)

penalties = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

bonus = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4 
}

openings = ('(', '[', '{', '<')
closings = (')', ']', '}', '>')

corresponding = dict()
corresponding2 = dict()


for i in range(len(openings)):
    corresponding[closings[i]] = openings[i]
    corresponding2[openings[i]] = closings[i]


res = 0
# with open('ex10.txt') as infile:
#     lines = infile.readlines()

scores = list()

for l in lines:
    chain = list()
    incomplete = True
    for c in l:
        if len(chain) == 0:
            if c in closings:
                res += penalties[c]
                incomplete = False
                break
            else:
                chain.append(c)
        else:
            if c in openings:
                chain.append(c)
            elif c in closings:
                if chain[-1] == corresponding[c]:
                    chain.pop()
                else:
                    res += penalties[c]
                    incomplete = False
                    break
    
    if incomplete:
        adding = list()
        while len(chain) > 0:
            adding.append(corresponding2[chain.pop()]) 
        
        score = 0
        for c in adding:
            score *= 5
            score += bonus[c]

        scores.append(score)
    

print(scores)
scores = sorted(scores)
print(scores)
res2 = scores[len(scores) // 2]

print("part a: {}".format(res))
#puzzle.answer_a = res

print("part b: {}".format(res2))
puzzle.answer_b = res2