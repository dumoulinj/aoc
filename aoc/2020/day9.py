from aocd.models import Puzzle
from aocd import numbers

puzzle = Puzzle(year=2020, day=9)

def check(i):
    for j in range(i-25, i-1):
            for k in range(j+1, i):
                #print("{} {} {}".format(i, j, k))
                if numbers[j]+numbers[k]==numbers[i]:
                    return True
    return False

s = len(numbers)
for i in range(25, s):
    if not check(i):
        print(i)
        print(numbers[i])
        answer_a = numbers[i]
        break


#puzzle.answer_a = numbers[i]

def check_2():
    for i in range(0, s-1):
        cum = numbers[i]
        for j in range(i+1, s):
            cum += numbers[j]
            if cum == answer_a:
                # solution
                values = list()
                for k in range(i, j+1):
                    values.append(numbers[k])
                values.sort()
                return values[0] + values[-1]
            elif cum > answer_a:
                break

sol = check_2()
print("answer b")
print(sol)
puzzle.answer_b = sol