
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

def released_pressure(t, fr):
    return t * fr


t_max = 30
best_score = 0
start = "AA"

# while True:
#     vid = start
#     open_valves = set()
#     score = 0

#     for t in range(1, t_max+1, 1):
#         if valves[vid]["fr"] > 0 and vid not in open_valves:
#             if bool(random.getrandbits(1)):
#                 score += released_pressure(t_max-t-1, valves[vid]["fr"]) 
#                 open_valves.add(vid)
#                 continue
#         candidates = [v for v in valves[vid]["to"] if v not in open_valves]
#         candidates = []
#         if candidates:
#             vid = random.choice(candidates)
#         else:
#             vid = random.choice([v for v in valves[vid]["to"]])
    
#     if score > best_score:
#         best_score = score
#         print("New best score ", best_score)

# open_valves = set()
# Q = deque()
# Q.append((start, open_valves, 0, 0))

# ordered_fr = []
# for v in valves.keys():
#     ordered_fr.append(valves[v]["fr"])
# ordered_fr = sorted(ordered_fr, reverse=True)
# best_possible_score = dict()
# for t in range(1, t_max + 1, 1):
#     best_possible_score[t] = sum([released_pressure(t_max-i, fr) for i, fr in enumerate(ordered_fr[:t_max-t])]) // 1.5 

# DP = set()
# while Q:
#     vid, open_valves, crt_score, t = Q.pop()

#     if crt_score > best_score:
#         best_score = crt_score
#         print("New best score ", best_score)

#     dpk = (vid, tuple(sorted(open_valves)), t)

#     if dpk in DP:
#         continue

#     rt = t_max - t

#     if rt == -1:
#         continue

#     v = valves[vid]

#     if vid not in open_valves and v["fr"] > 0:
#         # _open_valves = open_valves.copy()
#         _open_valves = set(open_valves)
#         _open_valves.add(vid)
#         Q.append((vid, _open_valves, crt_score + released_pressure(rt-1, v["fr"]), t+1))

#     next_candidates = [c for c in v["to"]]
#     for ncid in next_candidates:
#         Q.append((ncid, open_valves, crt_score, t+1))
    
#     DP.add(dpk)
# DP = defaultdict(int)

# def dfs(vid, open_valves, crt_score, t):
#     if t > t_max:
#         return crt_score

#     dpk = (vid, tuple(sorted(open_valves)), t)

#     if dpk in DP:
#         return DP[dpk] 

#     rt = t_max - t
#     v = valves[vid]

#     res = crt_score
#     if vid not in open_valves and v["fr"] > 0:
#         _open_valves = open_valves.copy()
#         _open_valves.add(vid)
#         res = max(res, dfs(vid, _open_valves, crt_score + released_pressure(rt-1, v["fr"]), t+1))

#     next_candidates = [c for c in v["to"]]
#     for ncid in next_candidates:
#         res = max(res, dfs(ncid, open_valves, crt_score, t+1))
    
#     DP[dpk] = res
#     return res

## Part 1 working
# DP = defaultdict(int)
# def dfs(vid, open_valves, t):
#     if t == 0:
#         return 0

#     dpk = (vid, tuple(sorted(open_valves)), t)

#     if dpk in DP:
#         return DP[dpk] 

#     v = valves[vid]

#     res = 0
#     if vid not in open_valves and v["fr"] > 0:
#         _open_valves = open_valves.copy()
#         _open_valves.add(vid)
#         res = max(res, sum([valves[x]["fr"] for x in open_valves]) + dfs(vid, _open_valves, t-1))

#     for ncid in [c for c in v["to"]]:
#         res = max(res, sum([valves[x]["fr"] for x in open_valves]) + dfs(ncid, open_valves, t-1))
    
#     DP[dpk] = res
#     return res

# res_a = dfs(start, set(), 30)
# print("part a: {}".format(res_a))


DP = defaultdict(int)
def dfs(vid1, vid2, open_valves, t):
    if t == 0:
        return 0

    dpk = (vid1, vid2, tuple(sorted(open_valves)), t)

    if dpk in DP:
        return DP[dpk] 

    v1 = valves[vid1]
    v2 = valves[vid2]

    res = 0
    _open_valves = open_valves.copy()
    new_open = False
    if vid1 not in _open_valves and v1["fr"] > 0:
        _open_valves.add(vid1)
        new_open = True

    if vid2 not in _open_valves and v2["fr"] > 0:
        _open_valves.add(vid2)
        new_open = True
        
    if new_open:
        res = max(res, sum([valves[x]["fr"] for x in open_valves]) + dfs(vid1, vid2, _open_valves, t-1))

    for ncid1 in [c for c in v1["to"]]:
        for ncid2 in [c for c in v2["to"]]:
            res = max(res, sum([valves[x]["fr"] for x in open_valves]) + dfs(ncid1, ncid2, open_valves, t-1))

    DP[dpk] = res
    return res
res_b = dfs(start, start, set(), 26)
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b