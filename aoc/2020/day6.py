
from aocd.models import Puzzle
from aocd import lines
import os

puzzle = Puzzle(year=2020, day=6)


groups = puzzle.input_data.split(os.linesep + os.linesep)


count = 0 
for group in groups:
    answers = set()
    group = group.replace('\n', '')
    for c in group:
        answers.add(c)
    count += len(answers)

print("part a: {}".format(count))
puzzle.answer_a = count

count = 0
for group in groups:
    persons = group.split('\n')
    group_size = len(persons)
    answers = dict()
    
    for person in persons:
        for c in person:
            if c not in answers:
                answers[c] = 1
            else:
                answers[c] += 1
    
    for k, v in answers.items():
        if v == group_size:
            count += 1


print("part b: {}".format(count))
puzzle.answer_b = count