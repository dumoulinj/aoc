from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
import string

puzzle = Puzzle(year=2022, day=3)

def get_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38
        
res_a = 0
res_b = 0

sacs = []
for l in lines:
    rs = [x for x in l]
    sacs.append([rs[:len(rs)//2], rs[len(rs)//2:]])

for s in sacs:
    for c in s[0]:
        if c in s[1]:
            p = get_priority(c)
            res_a += p
            break

sacs = lines
for i in range(0, len(sacs), 3):
    for c in sacs[i]:
        if c in sacs[i+1] and c in sacs[i+2]:
            p = get_priority(c)
            res_b += p
            break

print("part a: {}".format(res_a))
print("part b: {}".format(res_b))
# puzzle.answer_a = res_a
# puzzle.answer_b = res_b