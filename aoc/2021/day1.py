from aocd.models import Puzzle
from aocd import numbers

# a: 3min10
# b: 7min00

puzzle = Puzzle(year=2021, day=1)

count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        count += 1

print("part a: {}".format(count))
puzzle.answer_a = count

count = 0
for i in range(3, len(numbers)):
    if (numbers[i-3] + numbers[i-2] + numbers[i-1]) < (numbers[i-2] + numbers[i-1] + numbers[i]):
        count += 1

print("part b: {}".format(count))
puzzle.answer_b = count