from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys
import json

import attr
# a:
# b: 

puzzle = Puzzle(year=2021, day=18)

# with open('ex18.txt') as infile:
#    lines = infile.readlines()


def add(a, b):
    # Addition
    # [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]] 
    return "[" + a + "," + b + "]"

def is_pair(l):
    i = l.index(',')
    if l[i+1] == '[':
        return False
    else:
        return True

def explode(l):
    # if nested 4 times
    # -> leftmost explodes
        # explosion:
        # L + first number on the left (if any)
        # R + first number on the right (if any)
        # then the exploding pair = 0
    depth = 0
    left_s = ""
    right_s = ""

    left_i = -1
    right_i = -1 

    pos_a = -1 
    pos_b = -1

    pos_prev = -1
    pos_next = -1

    exploded = False

    for i, c in enumerate(l):
        if c == "[":
            depth += 1

        if exploded or (depth > 4 and is_pair(l[i:])):
            exploded = True
            if c == "[":
                pos_a = i
            elif c == "]":
                if right_s != "":
                    right_i = int(right_s)
                pos_b = i
                break
            elif c == ",":
                left_i = int(left_s)
            else:
                if left_i == -1:
                    left_s += c
                else:
                    right_s += c
        else:
            if c == "]":
                depth -= 1
            elif c not in ["[", ","]:
                pos_prev = i
    
    if exploded:
        if pos_b != -1:
            for i, c in enumerate(l[pos_b+1:]):
                if c not in ['[', ']', ',']:
                    pos_next = i
                    break
        
        
        _left = l[:pos_a]
        _right = l[pos_b+1:]

        if pos_prev != -1:
            _left_a = _left[:pos_prev+1]
            _left_b = _left[pos_prev+1:]
            for j in range(len(_left_a)-1, -1, -1):
                if _left_a[j] in ['[', ']', ',']:
                    break
            val = int(_left_a[j+1:]) + left_i
            _left = _left_a[:j+1] + str(val) + _left_b
        
        if pos_next != -1:
            _right_a = _right[:pos_next]
            _right_b = _right[pos_next:]
            for j in range(0, len(_right_b)):
                if _right_b[j] in ['[', ']', ',']:
                    break
            val = int(_right_b[:j]) + right_i
            _right = _right_a + str(val) + _right_b[j:]

        res = _left + '0' + _right
    else:
        res = l
    
    return res, exploded


def split(l):
    pos_a = -1
    pos_b = -1
    splitted = False
    for i, c in enumerate(l):
        if c not in ['[', ']', ',']:
            if l[i+1] not in ['[', ']', ',']:
                pos_a = i
                pos_b = i+1
                break
    
    if pos_a != -1 and pos_b != -1:
        splitted = True
        n = int(l[pos_a:pos_b+1])
        a = n//2
        b = n//2 + n % 2
        c = "[" + str(a) + "," + str(b) + "]"
        res = l[:pos_a] + c + l[pos_b+1:]
    else:
        res = l
    
    return res, splitted

def get_magnitude(l):
    left = l[0]
    right = l[1]

    if isinstance(left, list):
        mleft = 3 * get_magnitude(left)
    else:
        mleft = 3 * left
    
    if isinstance(right, list):
        mright = 2 * get_magnitude(right)
    else:
        mright = 2 * right
    
    return mleft + mright

def test_add():
    a = "[1,2]"
    b = "[[3,4],5]"

    assert add(a, b) == "[[1,2],[[3,4],5]]"

def test_explode():
    l = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    #l = "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[[10,10],20],40],[[11,9],[11,0]]]]"
    #l = "[[[5,0],[[[5,6],7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]"
    #l = "[[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]"
    res, exploded = explode(l)
    assert res == "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"

def test_split():
    l = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
    res, splitted = split(l)
    assert res == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"

def test_magnitude():
    assert get_magnitude([9,1]) == 29
    assert get_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

test_add()
test_explode()
test_split()
test_magnitude()

def part_a():
    snailfish = lines[0].strip()
    for l in lines[1:]:
        snailfish = add(snailfish, l.strip())
        i = 0
        while True:
            i += 1

            exploded = False
            splitted = False

            snailfish, exploded = explode(snailfish)

            if not exploded:
                snailfish, splitted = split(snailfish)

            if not exploded and not splitted:
                break

    l = json.loads(snailfish)
    res = get_magnitude(l)
    print("part a: {}".format(res))
    #puzzle.answer_a = res

maxres = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            a = lines[i].strip()
            b = lines[j].strip()
            snailfish = add(a, b)
            while True:
                exploded = False
                splitted = False

                snailfish, exploded = explode(snailfish)

                if not exploded:
                    snailfish, splitted = split(snailfish)

                if not exploded and not splitted:
                    break

            l = json.loads(snailfish)
            res = get_magnitude(l)
            maxres = max(res, maxres)

print("part b: {}".format(maxres))
puzzle.answer_b = maxres 