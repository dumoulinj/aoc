from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy

# a: 14:05
# b: 

# puzzle = Puzzle(year=2021, day=22)

# with open('ex22.txt') as infile:
#    lines = infile.readlines()

# cubes = dict()
# for l in lines:
#     p1, p2 = l.strip().split(' ')
#     on_off = p1 == "on"
    
#     rx, ry, rz = p2.split(',')
#     x1, x2 = rx.split('..')
#     y1, y2 = ry.split('..')
#     z1, z2 = rz.split('..')

#     x1 = int(x1[2:])
#     x2 = int(x2)
#     y1 = int(y1[2:])
#     y2 = int(y2)
#     z1 = int(z1[2:])
#     z2 = int(z2)


#     limit = 50
#     for x in range(max(x1, -1*limit), min(x2, limit) + 1):
#         for y in range(max(y1, -1*limit), min(y2, limit) + 1):
#             for z in range(max(z1, -1*limit), min(z2, limit) + 1):
#                 cubes[(x, y, z)] = on_off

# res = sum(cubes.values())

# print("part a: {}".format(res))
# puzzle.answer_a = res

def do_intersect(a, b):
    ax1, ax2 = a[0]
    ay1, ay2 = a[1]
    az1, az2 = a[2]

    bx1, bx2 = b[0]
    by1, by2 = b[1]
    bz1, bz2 = b[2]

    if bx2 < ax1 or bx1 > ax2:
        return False
    if by2 < ay1 or by1 > ay2:
        return False
    if bz2 < az1 or bz1 > az2:
        return False
    
    return True

def get_nb_points_in_range(r):
    return (r[0][1] - r[0][0]) * (r[1][1] - r[1][0]) * (r[2][1] - r[2][0])

def get_intersect_range(a, b):
    ax1, ax2 = a[0]
    ay1, ay2 = a[1]
    az1, az2 = a[2]

    bx1, bx2 = b[0]
    by1, by2 = b[1]
    bz1, bz2 = b[2]
    
    ix1 = max(ax1, bx1)
    ix2 = min(ax2, bx2)

    iy1 = max(ay1, by1)
    iy2 = min(ay2, by2)

    iz1 = max(az1, bz1)
    iz2 = min(az2, bz2)

    return ((ix1, ix2), (iy1, iy2), (iz1, iz2))


def get_nb_points_off(off_list):
    nb = 0
    for off in off_list:
        nb += get_nb_points_in_range(off)
    
    for i in range(len(off_list)-1):
        for j in range(i+1, len(off_list)):
            a = off_list[i]
            b = off_list[j]
            nb -= get_nb_points_in_range(get_intersect_range(a, b))
    
    return nb

cubes_on = defaultdict(list)
for i, l in enumerate(lines):
    p1, p2 = l.strip().split(' ')
    on_off = p1 == "on"
    
    rx, ry, rz = p2.split(',')
    x1, x2 = rx.split('..')
    y1, y2 = ry.split('..')
    z1, z2 = rz.split('..')

    x1 = int(x1[2:])
    x2 = int(x2)
    y1 = int(y1[2:])
    y2 = int(y2)
    z1 = int(z1[2:])
    z2 = int(z2)

    a = ((x1, x2), (y1, y2), (z1, z2))

    nb_intersect = 0
    ir = list()
    for b in cubes_on:
        if do_intersect(a, b):
            nb_intersect += 1
            intersect_range = get_intersect_range(a, b)

            if on_off:
                ir.append(("x", intersect_range))
                cubes_on[b].append(("on", intersect_range))
            else:
                cubes_on[b].append(("off", intersect_range))

    if nb_intersect == 0 and on_off:
        cubes_on[a] = list()
    else:
        cubes_on[a] = ir

res = 0
i = 0
for c, action_list in cubes_on.items():
    print(i, len(cubes_on))
    if len(action_list) == 0:
        print("A")
        res += get_nb_points_in_range(c)
    else:
        print("B")
        x_list = list()
        for a, r in action_list:
            if a == 'x':
                x_list.append(r)

        x1, x2 = c[0]
        y1, y2 = c[1]
        z1, z2 = c[2]


        cubes = dict()       
        # for x in range(x1, x2 + 1):
        #     for y in range(y1, y2 + 1):
        #         for z in range(z1, z2 + 1):
        #             for _x in x_list:
        #                 _xx1, _xx2 = _x[0]
        #                 _xy1, _xy2 = _x[1]
        #                 _xz1, _xz2 = _x[2]

        #                 if (_xx1 <= x <= _xx2) and (_xy1 <= y <= _xy2) and (_xz1 <= z <= _xz2):
        #                     pass
        #                 else:
        #                     cubes[(x, y, z)] = True 
        
        for a, r in action_list:
            if a == "on" or a == "off":
                x1, x2 = r[0]
                y1, y2 = r[1]
                z1, z2 = r[2]
                
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        for z in range(z1, z2 + 1):
                            for _x in x_list:
                                _xx1, _xx2 = _x[0]
                                _xy1, _xy2 = _x[1]
                                _xz1, _xz2 = _x[2]

                                if (_xx1 <= x <= _xx2) and (_xy1 <= y <= _xy2) and (_xz1 <= z <= _xz2):
                                    pass
                                else:
                                    cubes[(x, y, z)] = a == "on"
        
        res += sum(cubes.values())

    i += 1


print("part b: {}".format(res))
#puzzle.answer_b = res

#8468310916723377
#2758514936282235