from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines

# a: 5:00
# b: 9:00

puzzle = Puzzle(year=2022, day=4)

        
res_a = 0
res_b = 0

for l in lines:
    a, b = l.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    if (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2):
        res_a += 1
    
    if (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2) or (a1 <= b1 <= a2) or (a1 <= b2 <= a2) or(b1 <= a1 <= b2) or (b1 <= a2 <= b2):
        res_b += 1

print("part a: {}".format(res_a))
print("part b: {}".format(res_b))
puzzle.answer_a = res_a
puzzle.answer_b = res_b