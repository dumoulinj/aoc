from aocd.models import Puzzle
from aocd import lines

# a: 10:40
# b: > 24h

gamma = 0
epsilon = 0

puzzle = Puzzle(year=2021, day=3)

def get_g_e(l, eq):
    x = list()
    for i in range(len(l[0])):
        x.append("")

    for line in l:
        for i, c in enumerate(line):
            x[i] += c

    g = ""
    e = ""
    for c in x:
        zero = c.count('0') 
        un = c.count('1')
        if zero > un:
            g += "0"
            e += "1"
        else:
            if eq and zero == un:
                g += "2"
                e += "2"
            else:
                g += "1"
                e += "0"
    return g, e

g, e = get_g_e(lines, False)

gamma = int(g, 2)
epsilon = int(e, 2)

res = gamma * epsilon

print("part a: {}".format(res))
puzzle.answer_a = res


# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.


# The bit criteria depends on which type of rating value you want to find:
# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
i = 0
_lines = list()
for line in lines:
    _lines.append(line)

while len(_lines) > 1:
    filtered = list()
    g, e = get_g_e(_lines, True)

    for _line in _lines:
        if _line[i] == g[i] or (g[i] == '2' and _line[i] == '1'):
            filtered.append(_line)

    _lines = filtered
    i += 1
oxygen = int(_lines[0], 2)

i = 0
_lines = list()
for line in lines:
    _lines.append(line)

while len(_lines) > 1:
    filtered = list()
    g, e = get_g_e(_lines, True)
    for _line in _lines:
        if _line[i] == e[i] or (e[i] == '2' and _line[i] == '0'):
            filtered.append(_line)

    _lines = filtered
    i += 1

co2 = int(_lines[0], 2)

res = oxygen * co2
print("part b: {}".format(res))
puzzle.answer_b = res