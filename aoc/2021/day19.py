from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys
import math
import attr
# a: 
# b: 

puzzle = Puzzle(year=2021, day=19)

@attr.s
class Position(object):
    x:int = attr.ib()
    y:int = attr.ib()
    z:int = attr.ib()

    def __eq__(self, other) -> bool:
        print("Test")
        return self.x == other.x and self.y == other.y and self.z == other.z

@attr.s
class Beacon(Position):
    def __eq__(self, other) -> bool:
        print("Test2")
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def update(self, new_pos):
        self.x = new_pos.x
        self.y = new_pos.y
        self.z = new_pos.z


@attr.s
class Orientation(object):
    x:int = attr.ib()
    y:int = attr.ib()
    z:int = attr.ib()
    up:int = attr.ib()

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z and self.up == __o.z

@attr.s
class Transformation(object):
    pos:Position = attr.ib()
    o:Orientation = attr.ib()

    def __hash__(self) -> int:
        return self.pos.x * self.o.up
    
    def __eq__(self, other: object) -> bool:
        return self.pos == other.pos and self.o == other.o

@attr.s
class Scanner(object):
    _id:int = attr.ib()
    beacons:list = attr.ib(init=False, factory=list)
    ref_beacons:list = attr.ib(init=False, factory=list)
    distances:defaultdict = attr.ib(init=False, default=attr.Factory(lambda: defaultdict(list)))
    position:Position = attr.ib(init=False)
    orientation:Orientation = attr.ib(init=False)
    parent = attr.ib(init=False, factory=bool)

    def get_size(self):
        return len(self.beacons)

    def __eq__(self, other):
        if (isinstance(other, Scanner)):
            return self._id == other._id
        return False

    def compute_distances(self):
        for i in range(len(self.beacons)-1):
            for j in range(i+1, len(self.beacons)):
                b1 = self.beacons[i]
                b2 = self.beacons[j]
                d = get_distance(b1, b2)
                self.distances[d].append((b1, b2))

with open('ex19.txt') as infile:
   lines = infile.readlines()

def get_distance(b1, b2):
    return int(math.sqrt((b2.x - b1.x)**2 + (b2.y - b1.y)**2 + (b2.z - b1.z)**2))
    #return math.sqrt((b2.x - b1.x)**2 + (b2.y - b1.y)**2 + (b2.z - b1.z)**2)

def get_equal_distances(s1, s2):
    ed = list()
    for k, v in s1.distances.items():
        if k in s2.distances:
            ed.append((v, s2.distances[k]))
    
    return ed

orientations = [
    Orientation(1, 1, 1, 0),    #  x y z
    Orientation(-1, -1, 1, 0),  # -x -y z
    Orientation(1, -1, -1, 0),  # x -y -z
    Orientation(-1, 1, -1, 0),  # -x y -z

    Orientation(1, -1, 1, 1),   # y -x z
    Orientation(-1, 1, 1, 1),   # -y, x, z
    Orientation(1, 1, -1, 1),   # y, x, -z
    Orientation(-1, -1, -1, 1), # -y, -x, -z
    
    Orientation(1, -1, 1, 2),   # x -z y
    Orientation(-1, 1, 1, 2),   # -x z y
    Orientation(1, 1, -1, 2),   # x z -y
    Orientation(-1, -1, -1, 2), # -x -z -y

    Orientation(-1, 1, 1, 3),   # -z y x
    Orientation(1, -1, 1, 3),   # z -y x
    Orientation(1, 1, -1, 3),   # z y -x
    Orientation(-1, -1, -1, 3), # -z -y -z

    Orientation(1, 1, 1, 4),    # y z x
    Orientation(1, -1, -1, 4),  # y -z -x
    Orientation(-1, 1, 1, 4),  # -y z x
    Orientation(-1, -1, -1, 4), # -y -z -x

    Orientation(-1, -1, 1, 5),  # -z -x y
    Orientation(1, -1, -1, 5),  # z -x -y
    Orientation(1, 1, 1, 5),    # z x y
    Orientation(-1, 1, -1, 5)   # -z x -y
]

def apply_transformation(p: Position, t: Transformation):
    ref = t.pos
    o = t.o

    if o.up == 0: # x y z
        nx = p.x * o.x + ref.x
        ny = p.y * o.y + ref.y
        nz = p.z * o.z + ref.z
    elif o.up == 1: # y x z
        nx = p.y * o.x + ref.x
        ny = p.x * o.y + ref.y
        nz = p.z * o.z + ref.z
    elif o.up == 2: # x z y
        nx = p.x * o.x + ref.x
        ny = p.z * o.y + ref.y
        nz = p.y * o.z + ref.z
    elif o.up == 3: # z y x
        nx = p.z * o.x + ref.x
        ny = p.y * o.y + ref.y
        nz = p.x * o.z + ref.z
    elif o.up == 4: # y z x
        nx = p.y * o.x + ref.x
        ny = p.z * o.y + ref.y
        nz = p.x * o.z + ref.z
    elif o.up == 5: # z x y
        nx = p.z * o.x + ref.x
        ny = p.x * o.y + ref.y
        nz = p.y * o.z + ref.z

    return Position(nx, ny, nz)

def get_transformations(a, b):
    transformations = list()
    for _a in a:
        for _b in b:
            a1 = _a[0]
            a2 = _a[1]

            b1 = _b[0]
            b2 = _b[1]

            for _b1, _b2 in [(b1, b2), (b2, b1)]:
                for o in orientations:
                    if o.up == 0: # x y z
                        bx = a1.x - o.x * _b1.x
                        by = a1.y - o.y * _b1.y
                        bz = a1.z - o.z * _b1.z
                    elif o.up == 1: # y x z
                        bx = a1.x - o.x * _b1.y
                        by = a1.y - o.y * _b1.x
                        bz = a1.z - o.z * _b1.z
                    elif o.up == 2: # x z y
                        bx = a1.x - o.x * _b1.x
                        by = a1.y - o.y * _b1.z
                        bz = a1.z - o.z * _b1.y
                    elif o.up == 3: # z y x
                        bx = a1.x - o.x * _b1.z
                        by = a1.y - o.y * _b1.y
                        bz = a1.z - o.z * _b1.x
                    elif o.up == 4: # y z x
                        bx = a1.x - o.x * _b1.y
                        by = a1.y - o.y * _b1.z
                        bz = a1.z - o.z * _b1.x
                    elif o.up == 5: # z x y
                        bx = a1.x - o.x * _b1.z
                        by = a1.y - o.y * _b1.x
                        bz = a1.z - o.z * _b1.y

                    ref = Position(bx, by, bz)
                    t = Transformation(ref, o)
                    nb = apply_transformation(_b2, t)

                    if nb.x == a2.x and nb.y == a2.y and nb.z == a2.z:
                        transformations.append(t)

    return transformations

scanners = list()
scanner_id = 0
scanner = None

for l in lines:
    l = l.strip()
    if l.startswith("--"):
        scanner = Scanner(scanner_id)
        if scanner_id == 0:
            scanner.orientation = Orientation(1, 1, 1, 0)
            scanner.position = Position(0, 0, 0)
            scanner.parent = None
    elif l == "" or l == " ":
        scanners.append(scanner)
        scanner_id += 1
    else:
        x, y, z = l.split(",")
        b = Beacon(int(x), int(y), int(z))
        scanner.beacons.append(b)
        scanner.ref_beacons.append(deepcopy(b))

scanners.append(scanner)

for s in scanners:
    s.compute_distances()

ref_scanners = list()
ref_scanners.append(scanners[0])

unref_scanners = list()
for i in range(1, len(scanners)):
    unref_scanners.append(scanners[i])


while len(unref_scanners) > 0:
    new_unref_scanners = list()
    new_ref_scanners = deepcopy(ref_scanners)
    for sunref in unref_scanners:
        found_ref = False
        s2 = sunref
        for sref in ref_scanners:
            if found_ref:
                break
            
            s1 = sref
            # print(s1._id, s2._id)

            ed = get_equal_distances(s1, s2)

            for a, b in ed:
                if found_ref:
                    break
                transformations = get_transformations(a, b)

                # Test each transformation
                for t in transformations:
                    if found_ref:
                        break
                    # Apply t to each beacons of s2
                    transformed = [apply_transformation(p, t) for p in s2.beacons]

                    count = 0
                    for bt in transformed:
                        for b1 in s1.beacons:
                            if bt.x == b1.x and bt.y == b1.y and bt.z == b1.z:
                            # if bt == b1:
                                count += 1
                    
                    # print("Count ", count)

                    if count >= 12:
                        print("Found ", s2._id, s1._id, t)
                        found_ref = True

                        s2.position = t.pos
                        s2.orientation = t.o
                        s2.parent = s1
                        parent = s2.parent

                        s2.ref_beacons = [apply_transformation(p, Transformation(s2.position, s2.orientation)) for p in s2.ref_beacons]
                        if parent is not None:
                            s2.position = apply_transformation(s2.position, Transformation(parent.position, parent.orientation))
                            s2.ref_beacons = [apply_transformation(p, Transformation(parent.position, parent.orientation)) for p in s2.ref_beacons]

                        # while parent is not None:
                        #     s2.position = apply_transformation(s2.position, Transformation(parent.position, parent.orientation))
                        #     s2.ref_beacons = [apply_transformation(p, Transformation(parent.position, parent.orientation)) for p in s2.ref_beacons]
                        #     parent = parent.parent

                        new_ref_scanners.append(s2)
                        break
                
        if not found_ref:
            new_unref_scanners.append(s2)
                    
    # unref_scanners = deepcopy(new_unref_scanners)
    # ref_scanners = deepcopy(new_ref_scanners)
    unref_scanners = new_unref_scanners
    ref_scanners = new_ref_scanners


        
all_beacons = set()
for s in scanners:
    print(s._id, s.position, s.orientation, s.parent._id if s.parent is not None else None)
    # if s._id != 1:
    #     continue

    #s.beacons = [apply_transformation(p, Transformation(s.position, s.orientation)) for p in s.beacons]
    for b in s.ref_beacons:
        all_beacons.add((b.x, b.y, b.z))

print(all_beacons)

res = len(all_beacons)
print("part a: {}".format(res))
#puzzle.answer_a = res

print("part b: {}".format(res))
#puzzle.answer_b = res