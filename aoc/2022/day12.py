

from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict, deque
import os
import copy
# a: 
# b:  

day = 12

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()


m = defaultdict(int)
maxr = len(lines)
maxc = len(lines[0].strip())
start = [] 
end = None
for r, l in enumerate(lines):
    for c, v in enumerate(l):
        if v == 'S':
            start.append((r, c))
            _v = ord('a')
        elif v == 'E':
            end = (r, c)
            _v = ord('z')
        else:
            if v == 'a':
                start.append((r, c))
            _v = ord(v)
        
        m[(r, c)] = _v

def bfs(part):
    q = deque()
    q.append((start[0], 0))
    if part == 2:
        for s in start[1:]:
            q.append((s, 0))
    
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = set() 
    while q:
        pos, depth = q.popleft()

        if pos == end:
            return depth

        if pos in visited:
            continue

        visited.add(pos)

        r = pos[0]
        c = pos[1]

        for d in dirs:
            rr = r + d[0]
            cc = c + d[1]

            if 0 <= rr < maxr and 0 <= cc < maxc and m[(rr, cc)] <= m[(r, c)] + 1:
                q.append(((rr, cc), depth + 1))

res_a = bfs(1)
print("part a: {}".format(res_a))

res_b = bfs(2)
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b