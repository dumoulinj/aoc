from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines

# a: 
# b:  

puzzle = Puzzle(year=2022, day=6)

def get_pos(l, n):
    c = 0
    t = []
    for i in range(len(l)):
        t.append(l[i])
        if i > n-1:
            ok = True 
            for x in t:
                if t.count(x) > 1:
                    ok = False 
            if ok:
                return i + 1

        if len(t) > n-1:
            del t[0]

res_a = get_pos(lines[0], 4)
print("part a: {}".format(res_a))
#puzzle.answer_a = res_a


res_b = get_pos(lines[0], 14)
print("part b: {}".format(res_b))
# puzzle.answer_b = res_b