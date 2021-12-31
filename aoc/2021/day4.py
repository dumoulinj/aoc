from aocd.models import Puzzle
from aocd import lines

# a: 32 min
# b: 45 min


puzzle = Puzzle(year=2021, day=4)

numbers = [int(x) for x in lines[0].split(',')]


def get_winner(part2):
    grids = list()
    marked = list()
    size = len(lines)
    for i in range(2, size, 6):
        grid = list()
        m = list()
        for j in range(5):
            grid.append([int(x) for x in lines[i+j].split(' ') if x != ''])
            m.append([0 for i in range(5)])
        grids.append(grid)
        marked.append(m)

    solved = set() 
    nb_grids = len(grids)

    for n in numbers:
        for i, grid in enumerate(grids):
            if i not in solved:
                for r in range(5):
                    for c in range(5):
                        if grid[r][c] == n:
                            marked[i][r][c] = 1
                            a = [x for x in marked[i][r]]
                            b = [x[c] for x in marked[i]]
                            sum_a = sum(a)
                            sum_b = sum(b)
                            if sum_a == 5 or sum_b == 5:
                                if part2:
                                    solved.add(i)
                                    if len(solved) == nb_grids:
                                        s = 0
                                        for _r in range(5):
                                            for _c in range(5):
                                                if marked[i][_r][_c] == 0:
                                                    s += grid[_r][_c]
                                        res = n * s
                                        return res
                                else:
                                    s = 0
                                    for _r in range(5):
                                        for _c in range(5):
                                            if marked[i][_r][_c] == 0:
                                                s += grid[_r][_c]
                                    res = n * s
                                    return res

res = get_winner(False)
print("part a: {}".format(res))
puzzle.answer_a = res

res = get_winner(True)
print("part b: {}".format(res))
puzzle.answer_b = res