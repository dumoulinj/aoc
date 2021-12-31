from aocd.models import Puzzle
from aocd import numbers

puzzle = Puzzle(year=2020, day=1)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        _i = numbers[i]
        _j = numbers[j]
        if _i + _j == 2020:
            print("part a: {}".format(_i*_j))

for i in range(len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)-1):
            _i = numbers[i]
            _j = numbers[j]
            _k = numbers[k]
            if _i + _j + _k== 2020:
                print("part b: {}".format(_i*_j*_k))