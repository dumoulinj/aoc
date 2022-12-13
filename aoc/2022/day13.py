from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict, deque
import os
import copy
import json
# a: 
# b:  

day = 13

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()

p1 = []
p2 = []
p = []

for l in lines:
    if l.strip() == '':
        p1.append(p[0])
        p2.append(p[1])
        p = []
    else:
        p.append(json.loads(l.strip()))

p1.append(p[0])
p2.append(p[1])

right_order = list()

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        # print('    - Compare {} vs {}'.format(left, right))
        if left > right:
            # print('        - Right side is smaller, bad order')
            return False
        elif left < right:
            # print('        - Left side is smaller, right order')
            return True
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) > 0:
            return True
        elif len(left) > 0 and len(right) == 0:
            return False
        elif len(left) == 0 and len(right) == 0:
            return None
        else:
            res = compare(left[0], right[0])
            if res is None:
                return  compare(left[1:], right[1:])
            else:
                return res
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    return True


for i in range(len(p1)):
    # print('== Pair {} =='.format(i))
    _p1 = p1[i]
    _p2 = p2[i]
    # print('- Compare {} vs {}'.format(_p1, _p2))

    if compare(_p1, _p2):
        right_order.append(i+1)
    

res_a = sum(right_order)
print("part a: {}".format(res_a))

ordered_packets = list()
all_packets = p1 + p2
all_packets.append([[2]])
all_packets.append([[6]])
ordered_packets.append(all_packets.pop(0))

for p in all_packets:
    i = 0
    while i < len(ordered_packets)and not compare(p, ordered_packets[i]):
        i += 1
    
    ordered_packets.insert(i, p)

res_b = (ordered_packets.index([[2]]) + 1) * (ordered_packets.index([[6]]) + 1)
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b