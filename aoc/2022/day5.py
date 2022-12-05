from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines

# a: 13:20
# b: 20:10 

puzzle = Puzzle(year=2022, day=5)

res_a = '' 
res_b = ''

# crates = [
#         ['N', 'R', 'G', 'P'],
#         ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
#         ['M', 'S', 'V'],
#         ['L', 'S', 'R', 'C', 'Z', 'P'],
#         ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
#         ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
#         ['H', 'D', 'G', 'W', 'P'],
#         ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
#         ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
#     ]
crates = [[] for x in range(9)]
for l in lines[:8]:
    for i in range(9):
        try:
            t = l[i*4+1]
            if t != ' ':
                crates[i].insert(0, t)
        except:
            pass
import copy
crates_b = copy.deepcopy(crates) 


for l in lines[10:]:
    _l = l.split(' ')
    n = int(_l[1])
    s = int(_l[3]) - 1
    e = int(_l[5]) - 1
    for i in range(n):
        crates[e].append(crates[s].pop())
for c in crates:
    res_a += c[-1]
print("part a: {}".format(res_a))
puzzle.answer_a = res_a

for l in lines[10:]:
    _l = l.split(' ')
    n = int(_l[1])
    s = int(_l[3]) - 1
    e = int(_l[5]) - 1

    t = []

    for i in range(n):
        t.append(crates_b[s].pop())
    
    while t:
        crates_b[e].append(t.pop())
    

for c in crates_b:
    res_b += c[-1]

print("part b: {}".format(res_b))
puzzle.answer_b = res_b