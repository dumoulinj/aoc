from copy import copy, deepcopy
# a:
# b:

with open('ex25.txt') as infile:
   lines = infile.readlines()

sea = dict()

max_r = len(lines)
max_c = len(lines[0].strip())

def print_sea():
    for ir in range(max_r):
        for ic in range(max_c):
            print(sea[(ir, ic)], end="")
        print()

for ir, l in enumerate(lines):
    for ic, c in enumerate(l.strip()):
        sea[(ir, ic)] = c


def move_east(k, s, ns):
    r, c = k
    cc = (c + 1) % max_c
    if s[(r, cc)] == '.':
        ns[(r, c)] = '.'
        ns[(r, cc)] = '>'
        return True
    else:
        return False

def move_south(k, s, ns):
    r, c = k
    rr = (r + 1) % max_r
    if s[(rr, c)] == '.':
        ns[(r, c)] = '.'
        ns[(rr, c)] = 'v'
        return True
    else:
        return False

nb_steps = 1
while True:
    nb_moves = 0

    new_sea = copy(sea)
    for k, v in sea.items():
        if v == '>':
            if move_east(k, sea, new_sea):
                nb_moves += 1
    
    sea = copy(new_sea)
    for k, v in sea.items():
        if v == 'v':
            if move_south(k, sea, new_sea):
                nb_moves += 1
    
    sea = copy(new_sea)

    if nb_moves == 0:
        break
    nb_steps += 1

res = nb_steps
print("part a: {}".format(res))
#puzzle.answer_a = res 

#print("part b: {}".format(res))
#puzzle.answer_b = res 