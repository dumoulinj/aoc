# from aocd.models import Puzzle
from copy import copy, deepcopy

# puzzle = Puzzle(year=2021, day=23)

hotel = dict()

for c in range(11):
    hotel[(0, c)] = "."

ROOMS_SIZE = 4

room_col = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# # RA
# hotel[(1, room_col["A"])] = "B"
# hotel[(2, room_col["A"])] = "A"

# # RB
# hotel[(1, room_col["B"])] = "C"
# hotel[(2, room_col["B"])] = "D"

# # RC
# hotel[(1, room_col["C"])] = "B"
# hotel[(2, room_col["C"])] = "C"

# # RD
# hotel[(1, room_col["D"])] = "D"
# hotel[(2, room_col["D"])] = "A"

# # RA
# hotel[(1, room_col["A"])] = "B"
# hotel[(2, room_col["A"])] = "D"
# hotel[(3, room_col["A"])] = "D"
# hotel[(4, room_col["A"])] = "A"

# # RB
# hotel[(1, room_col["B"])] = "C"
# hotel[(2, room_col["B"])] = "C"
# hotel[(3, room_col["B"])] = "B"
# hotel[(4, room_col["B"])] = "D"

# # RC
# hotel[(1, room_col["C"])] = "B"
# hotel[(2, room_col["C"])] = "B"
# hotel[(3, room_col["C"])] = "A"
# hotel[(4, room_col["C"])] = "C"

# # RD
# hotel[(1, room_col["D"])] = "D"
# hotel[(2, room_col["D"])] = "A"
# hotel[(3, room_col["D"])] = "C"
# hotel[(4, room_col["D"])] = "A"

# RA
hotel[(1, room_col["A"])] = "A"
hotel[(2, room_col["A"])] = "D"
hotel[(3, room_col["A"])] = "D"
hotel[(4, room_col["A"])] = "C"

# RB
hotel[(1, room_col["B"])] = "D"
hotel[(2, room_col["B"])] = "C"
hotel[(3, room_col["B"])] = "B"
hotel[(4, room_col["B"])] = "D"

# RC
hotel[(1, room_col["C"])] = "A"
hotel[(2, room_col["C"])] = "B"
hotel[(3, room_col["C"])] = "A"
hotel[(4, room_col["C"])] = "B"

# RD
hotel[(1, room_col["D"])] = "C"
hotel[(2, room_col["D"])] = "A"
hotel[(3, room_col["D"])] = "C"
hotel[(4, room_col["D"])] = "B"

def get_room_ticket(hotel, a):
    C = room_col[a]

    for r in range(ROOMS_SIZE, 0, -1):
        if hotel[(r, C)] == ".":
            return (r, C)
        elif hotel[(r, C)] != a:
            return None 
    
    return None
    
def get_path(hotel, source, dest):
    nb_steps = 0
    
    crt = source

    while True:
        if crt == dest:
            return nb_steps
        
        if source[0] > 0 and crt[0] > 0 and crt[1] == source[1]:
            crt = (crt[0] - 1, crt[1])
        else:
            if crt[1] < dest[1]:
                crt = (crt[0], crt[1] + 1)
            elif crt[1] > dest[1]:
                crt = (crt[0], crt[1] - 1)
            else:
                crt = (crt[0] + 1, crt[1])

        if hotel[crt] != ".":
            return None
        
        nb_steps += 1

def is_in_place(hotel, cell):
    a = hotel[cell]
    C = room_col[a]

    if cell[0] == 0:
        return False
    
    if cell[1] != C:
        return False

    for r in range(ROOMS_SIZE, cell[0], -1):
        if hotel[(r, C)] != a:
            return False
    
    return True

def is_solved(hotel):
    for a, c in room_col.items():
        for r in range(1, ROOMS_SIZE + 1):
            if hotel[(r, c)] != a:
                return False
    return True

def print_hotel(hotel):
    for r in range(2 + ROOMS_SIZE):
        for c in range(-1, 12):
            if (r, c) in hotel:
                print(hotel[(r, c)], end="")
            else:
                print(" ", end="")
        print()

def get_minimum_cost(hotel):
    cost = 0
    cells = [c for c in hotel if hotel[c] != '.' and not is_in_place(hotel, c)]

    in_place = dict()

    for a in room_col.keys():
        in_place[a] = ROOMS_SIZE

    for cell in cells:
        in_place[hotel[cell]] -= 1
    
    for cell in cells:
        a = hotel[cell]
        steps = abs(room_col[a] - cell[1]) + ROOMS_SIZE - in_place[a]
        cost += steps * ENERGY[a]
        in_place[a] += 1
    
    return cost


def get_hotel_hash(hotel):
    _hash = ""

    for c in range(11):
        _hash += hotel[(0, c)]
    
    for c in [2, 4, 6, 8]:
        for r in range(1, ROOMS_SIZE+1):
            _hash += hotel[(r, c)]
    
    return _hash


ENERGY = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

best_score = 1e10

print_hotel(hotel)

optimize = True 

DP = dict()

def solve(hotel):
    global best_score 
    global optimize
    global DP

    if is_solved(hotel):
        return 0

    hotel_hash = get_hotel_hash(hotel)

    if hotel_hash in DP:
        return DP[hotel_hash]



    # print_hotel(hotel)
    # input("Press Enter to continue...")

    # all candidates
    candidates = list()
    for cell, a in hotel.items():
        if a != ".":
            if not is_in_place(hotel, cell):
                if cell[0] > 0:
                    if hotel[(cell[0]-1, cell[1])] == '.':
                        candidates.append(cell)
                else:
                    candidates.append(cell)

    if optimize:
        candidates.sort(key=lambda x:ENERGY[hotel[x]], reverse=True)


    for cell in candidates:
        a = hotel[cell]
        room = get_room_ticket(hotel, a)

        if room:
            steps = get_path(hotel, cell, room)

            if steps:
                cost = steps * ENERGY[a]

                # if new_score > best_score:
                #     continue

                new_hotel = deepcopy(hotel)
                new_hotel[cell] = "."
                new_hotel[room] = a

                
                # if optimize:
                #     if new_score + get_minimum_cost(new_hotel) > best_score:
                #         continue

                return cost + solve(new_hotel)
    

    # candidates not in hallway
    candidates = list()
    for cell, a in hotel.items():
        if a != ".":
            if not is_in_place(hotel, cell) and cell[0] > 0 and hotel[(cell[0]-1, cell[1])] == '.':
                candidates.append(cell)
    
    #candidates.sort(key=lambda x:x[1], reverse=False)
    
    ans = 1e10
    for cell in candidates:
        hcs = list(range(11))
        if optimize:
            hcs.sort(key=lambda x:abs(cell[1]-x))
        for c in hcs:
            if c not in [2, 4, 6, 8] and hotel[(0, c)] == '.':
                hc = (0, c)
                a = hotel[cell]
                steps = get_path(hotel, cell, hc)

                if steps:
                    cost = steps * ENERGY[a]

                    # if new_score > best_score:
                    #     continue

                    new_hotel = deepcopy(hotel)
                    new_hotel[cell] = "."
                    new_hotel[hc] = a

                    # if optimize:
                    #     if new_score + get_minimum_cost(new_hotel) > best_score:
                    #         continue

                    ans = min(ans, cost + solve(new_hotel))
    

        DP[hotel_hash] = ans
    
    return ans

print(solve(hotel))