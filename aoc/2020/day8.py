from aocd.models import Puzzle
from aocd import lines
import attr

puzzle = Puzzle(year=2020, day=8)

@attr.s
class Instruction(object):
    operation: str = attr.ib()
    argument:int = attr.ib()

instructions = list()

#lines = "nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6"
#lines = lines.split('\n')

for line in lines:
    parts = line.split(' ')
    instructions.append(Instruction(parts[0], int(parts[1])))


accumulator = 0
c = 0

visited = set()

while c not in visited:
    visited.add(c)
    instruction = instructions[c]
    if instruction.operation == 'acc':
        accumulator += instruction.argument
        c += 1
    elif instruction.operation == 'jmp':
        c += instruction.argument
    else:
        c += 1

print(accumulator)
#puzzle.answer_a = accumulator

accumulator = 0
c = 0

visited = set()
visited_2 = set()
c_temp = -1
nb_instruction = len(instructions)
accumulator_bak = 0

while c < nb_instruction:
    nxt = False
    if c in visited or c in visited_2:
        c = c_temp
        c_temp = -1
        accumulator = accumulator_bak
        visited_2 = set()
        nxt = True

    if c_temp == -1 and nxt == False:
        visited.add(c)
    else:
        visited_2.add(c)

    instruction = instructions[c]
    if instruction.operation == 'acc':
        accumulator += instruction.argument
        c += 1
    else:
        if c_temp == -1 and nxt == False:
            c_temp = c
            accumulator_bak = accumulator
            if instruction.operation == 'jmp':
                # do a nope instead
                c += 1
            else:
                # do a jump instead
                c += instruction.argument
        else:
            if instruction.operation == 'jmp':
                c += instruction.argument
            else:
                c += 1

print(accumulator)
puzzle.answer_b = accumulator