from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict

# a: 
# b:  

day = 8

puzzle = Puzzle(year=2022, day=day)

# with open('day8.ex') as infile:
#     lines = infile.readlines()

m = defaultdict(int)

for i, l in enumerate(lines):
    for j, c in enumerate(l.strip()):
        m[i, j] = int(c)

h = i+1
w = j+1

acc = w * 2 + (h - 2) * 2

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for i in range(1, h-1):
    for j in range(1, w-1):
        for d in dirs:
            e = 1 
            v = True
            while True:
                if (i + e*d[0], j + e*d[1]) in m:
                    if m[(i + e*d[0], j + e*d[1])] >= m[(i, j)]:
                        v = False
                        break
                    else:
                        pass
                else:
                    break
                e += 1

            if v:
                acc += 1
                break

res_a = acc


res_b = 0
for i in range(0, h):
    for j in range(0, w):
        sc = 1
        for d in dirs:
            e = 1 
            acc = 0
            while True:
                if (i + e*d[0], j + e*d[1]) in m:
                    acc += 1
                    if m[(i + e*d[0], j + e*d[1])] >= m[(i, j)]:
                        break
                else:
                    break
                e += 1

            sc *= acc
        
        res_b = max(res_b, sc)



print("part a: {}".format(res_a))
print("part b: {}".format(res_b))

#puzzle.answer_a = res_a
# puzzle.answer_b = res_b