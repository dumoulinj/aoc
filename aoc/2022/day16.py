
import random
import sys
from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import Counter, defaultdict, deque
import os
import copy
import json
# a: 
# b:  

day = 16

puzzle = Puzzle(year=2022, day=day)

exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
with open(exfile) as infile:
    lines = infile.readlines()

# 30 minutes before the volcano erupts
# flow rate if it were opened (in pressure per minute)
valves = dict()
DP = dict()

for l in lines:
    _l = l.strip().split()
    v_id = _l[1]
    fr = int(_l[4][5:-1])
    to_valves = []
    for v in _l[9:]:
        to_valves.append(v[:2])
    
    valves[v_id] = {
        "fr": fr,
        "to": to_valves
    }

print(valves)

def released_pressure(t, fr):
    return t * fr


start = "AA"
t_open = 1
t_follow = 1
t_max = 30

best_score = 0

vid = start
crt_score = 0
open_valves = set()

Q = deque()
Q.append((vid, open_valves, crt_score, 0))

path = vid

ordered_fr = []
for v in valves.keys():
    ordered_fr.append(valves[v]["fr"])
ordered_fr = sorted(ordered_fr, reverse=True)
best_possible_score = dict()
for t in range(1, t_max + 1, 1):
    best_possible_score[t] = sum([released_pressure(t_max-i, fr) for i, fr in enumerate(ordered_fr[:t_max-t])]) // 1.5 

while Q:
    vid, open_valves, crt_score, t = Q.popleft()

    if crt_score > best_score:
        best_score = crt_score
        print("New best score ", best_score)

    if t >= t_max:
        continue

    if t > 0 and best_score - crt_score > best_possible_score[t]:
        continue


    rt = t_max - t
    v = valves[vid]

    if vid not in open_valves and v["fr"] > 0:
        _open_valves = open_valves.copy()
        _open_valves.add(vid)
        Q.append((vid, _open_valves, crt_score + released_pressure(rt-1, v["fr"]), t+1))

    next_candidates = [c for c in v["to"]]
    for ncid in next_candidates:
        Q.append((ncid, open_valves, crt_score, t+1))
    

res_a = 0
print("part a: {}".format(res_a))

res_b = 0
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b