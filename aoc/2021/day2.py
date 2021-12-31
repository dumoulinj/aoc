from aocd.models import Puzzle
from aocd import lines

# a: 3:48
# b: 7:00 (1 bad submission)

puzzle = Puzzle(year=2021, day=2)
h = 0
depth = 0
for line in lines:
    s = line.split(' ')
    direction = s[0]
    x = int(s[1])

    if direction == 'forward':
        h += x
    elif direction == 'down':
        depth += x
    else:
        depth -= x

res = h * depth

print("part a: {}".format(res))
puzzle.answer_a = res

h = 0
depth = 0
aim = 0
for line in lines:
    s = line.split(' ')
    direction = s[0]
    x = int(s[1])

    if direction == 'forward':
        h += x
        depth += aim * x
    elif direction == 'down':
        #depth += x
        aim += x
    else:
        #depth -= x
        aim -= x

res = h * depth

print("part b: {}".format(res))
puzzle.answer_b = res


#print("part b: {}".format(count))
#puzzle.answer_b = count