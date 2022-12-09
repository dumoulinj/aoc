from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines
from collections import defaultdict

# a: 
# b:  

day = 9

puzzle = Puzzle(year=2022, day=day)

# with open('day9.ex') as infile:
#     lines = infile.readlines()


def do_move(H, T):
    # Get distance
    if abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1:
        # same row
        if H[0] == T[0]:
            if T[1] < H[1]:
                T[1] = H[1] - 1
            else:
                T[1] = H[1] + 1
        # same col
        elif H[1] == T[1]:
            if T[0] < H[0]:
                T[0] = H[0] - 1
            else:
                T[0] = H[0] + 1
        # diag 
        else:
            sr = 0
            sc = 0
            if T[0] < H[0]:
                sr = 1
            else:
                sr = -1
            if T[1] < H[1]:
                sc = 1
            else:
                sc = -1
            
            T[0] += sr
            T[1] += sc
        return True
    else:
        return False 

def viz():
    min_r = min(-5, min([x[0] for x in snake]))
    max_r = max(5, max([x[0] for x in snake]))
    min_c = min(-5, min([x[1] for x in snake]))
    max_c = max(-5, max([x[1] for x in snake]))
    
    for r in range(max_r, min_r, -1):
        for c in range(min_c, max_c+1):
            p = '.'
            for i, s in enumerate(snake):
                if s[0] == r and s[1] == c:
                    p = i
                    break
            print(p, end='')
        print()
    a = input()

    print()


def run(size, do_viz):
    m = defaultdict(int)

    snake = []

    for i in range(size):
        snake.append([0, 0])

    dirs = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (1, 0),
        'D': (-1, 0)
    }

    m[(0, 0)] = 1

    if do_viz:
        viz()


    for l in lines:
        d, n = l.strip().split(' ')
        n = int(n)
        if do_viz:
            print('Move ', d, n)
        for i in range(1, n+1):
            snake[0] = [snake[0][0]+dirs[d][0], snake[0][1]+dirs[d][1]]
            for j in range(len(snake)-1):
                do_move(snake[j], snake[j+1])
            m[(snake[-1][0], snake[-1][1])] += 1
            if do_viz:
                viz()

    return len(m) 

res_a = run(2, False)
res_b = run(10, False) 

print("part a: {}".format(res_a))
print("part b: {}".format(res_b))

#puzzle.answer_a = res_a
# puzzle.answer_b = res_b