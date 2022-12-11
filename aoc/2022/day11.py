
from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict
from attrs import define, Factory
import os
import copy
# a: 
# b:  

day = 11

puzzle = Puzzle(year=2022, day=day)

# exfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day{}.ex'.format(day))
# with open(exfile) as infile:
#     lines = infile.readlines()


@define
class Monkey:
    op: str = '' 
    op_val: int = 0
    test: int = 0
    true: int = 0
    false: int = 0
    items: list[int] = Factory(list)
    nb_inspection: int = 0


mi = 0
monkeys = []
monkey = None
pgdc = 1
for l in lines:
    l = l.lstrip().strip()
    if l.startswith('Monkey'):
        monkey = Monkey()
    elif l == '':
        monkeys.append(monkey)
        mi += 1
    elif l.startswith('Starting'):
        l = l.replace(',', '')
        _l = l.split()
        items = [int(x) for x in _l[2:]]
        monkey.items = items
    elif l.startswith('Operation'):
        _l = l.split()
        op = _l[4]
        if _l[5] == 'old':
            op_val = -1
        else:
            op_val = int(_l[5])
        monkey.op = op
        monkey.op_val = op_val
    elif l.startswith('Test'):
        monkey.test = int(l.split()[-1])
        pgdc *= monkey.test
    elif l.startswith('If true'):
        monkey.true = int(l.split()[-1])
    elif l.startswith('If false'):
        monkey.false = int(l.split()[-1])

monkeys.append(monkey)

def run(part, monkeys):
    if part == 1:
        max_round = 20
    else:
        max_round = 10000

    for r in range(max_round):
        # print('Round {}'.format(r))
        for m in monkeys:
            #for si in m.items:
            while len(m.items) > 0:
                si = m.items.pop(0)
                m.nb_inspection += 1
                if m.op == '*':
                    if m.op_val == -1:
                        si *= si
                    else:
                        si *= m.op_val
                else:
                    si += m.op_val
                
                if part == 1:
                    si = si // 3

                idx = None
                if si % m.test == 0:
                    idx = m.true
                else:
                    idx = m.false

                si = si % pgdc
                monkeys[idx].items.append(si)
                # print('Append {} to monkey {}'.format(si, idx))
        
        # for m in monkeys:
        #     m.items = [x%m.test for x in m.items]
        # print('Round {}'.format(r))
        # for m in monkeys:
        #     print(m.nb_inspection)
    
    monkeys.sort(key=lambda x: x.nb_inspection, reverse=True)
    return monkeys[0].nb_inspection * monkeys[1].nb_inspection

res_a = run(1, copy.deepcopy(monkeys))
print("part a: {}".format(res_a))

res_b = run(2, copy.deepcopy(monkeys))
print("part b: {}".format(res_b))

# puzzle.answer_a = res_a
# puzzle.answer_b = res_b