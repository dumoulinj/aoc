from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines

puzzle = Puzzle(year=2022, day=1)

res_a = 0
elves = []
c = 0
for v in lines:
    if v=="":
        res_a = max(res_a, c)
        elves.append(c)
        c = 0
    else:
        c += int(v)

print("part a: {}".format(res_a))
# puzzle.answer_a = res_a

elves.sort(reverse=True)
res_b = elves[0] + elves[1] + elves[2]
print("part b: {}".format(res_b))
# puzzle.answer_b = res_b