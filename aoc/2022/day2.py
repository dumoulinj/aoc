from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
#a: 9:22
#b: 19:16
puzzle = Puzzle(year=2022, day=2)

# A : Rock / B : Paper / C : Scissors
# X :Rock / Y : Paper / Z : Scissors

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6,
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

res_a = 0
for r in lines:
    res_a += scores[r]

print("part a: {}".format(res_a))
puzzle.answer_a = res_a


strat = {
    "A X": "C",
    "A Y": "A",
    "A Z": "B",
    "B X": "A",
    "B Y": "B",
    "B Z": "C",
    "C X": "B",
    "C Y": "C",
    "C Z": "A" 
}

res_b = 0
for r in lines:
    c = strat[r]
    a, b = r.split(' ')
    res_b += scores[b] + scores[c]

print("part b: {}".format(res_b))
puzzle.answer_b = res_b