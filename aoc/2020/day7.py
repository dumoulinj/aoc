from aocd.models import Puzzle
from aocd import lines

puzzle = Puzzle(year=2020, day=7)

rules = dict()

for line in lines:
    line = line.replace(' bags', '').replace(' bag', '').replace('.', '')
    parts = line.split(' contain ')
    
    if parts[0] not in rules:
        rules[parts[0]] = list()
    
    inside_bags = parts[1].split(', ')

    for inside_bag in inside_bags:
        if inside_bag != 'no other':
            (nb, color1, color2) = inside_bag.split(' ')
            rules[parts[0]].append(((int)(nb), '{} {}'.format(color1, color2)))
    

def traverse(k):
    count = 0
    for a in rules[k]:
        if len(a) > 0:
            if a[1] == 'shiny gold':
                return 1
            else:
                count += traverse(a[1])
    return 1 if count > 0 else 0

count = 0
for k,v in rules.items():
    count += traverse(k)

#puzzle.answer_a = count

def traverse_2(k):
    count = 1
    for a in rules[k]:
        count += a[0] * traverse_2(a[1])
    return count

res = traverse_2('shiny gold')
puzzle.answer_b = res - 1