from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys

import attr
# a: 38:00 
# b: 1:25:00

puzzle = Puzzle(year=2021, day=15)

#with open('ex15.txt') as infile:
#    lines = infile.readlines()

cavern = defaultdict(int)

nb_rows = len(lines)
nb_cols = len(lines[0].strip())

for r in range(nb_rows):
    for c in range(nb_cols):
        cavern[(r, c)] = int(lines[r][c])

for i in range(4):
    for r in range(nb_rows):
        for c in range(nb_cols):
            new_val = (cavern[(r+i*nb_rows, c)] + 1) % 10
            cavern[(r+(i+1)*nb_rows, c)] = new_val if new_val > 0 else 1

for i in range(4):
    for c in range(nb_cols):
        for r in range(nb_rows*5):
            new_val = (cavern[(r, c+i*nb_cols)] + 1) % 10
            cavern[(r, c+(i+1)*nb_cols)] = new_val if new_val > 0 else 1

# for i in range(50):
#     for j in range(50):
#         print(cavern[(i, j)], end='')
#     print()

START = (0, 0)
END = (nb_rows-1, nb_cols-1)

import numpy as np

nb_rows = nb_rows * 5
nb_cols = nb_cols * 5

cavern_map = np.ones((nb_rows, nb_cols), dtype=int)
for k, v in cavern.items():
    cavern_map[k[0]][k[1]] = v
cavern_map[0,0]=0

print(cavern_map)

#Initialize auxiliary arrays
distmap=np.ones((nb_rows, nb_cols),dtype=int)*np.Infinity
distmap[0,0]=0
originmap=np.ones((nb_rows, nb_cols),dtype=int)*np.nan
visited=np.zeros((nb_rows, nb_cols),dtype=bool)
finished = False
x,y=np.int(0),np.int(0)
count=0

#Loop Dijkstra until reaching the target cell
while not finished:
    # move to x+1,y
    if x < nb_rows-1:
        if distmap[x+1,y]>cavern_map[x+1,y]+distmap[x,y] and not visited[x+1,y]:
            distmap[x+1,y]=cavern_map[x+1,y]+distmap[x,y]
            originmap[x+1,y]=np.ravel_multi_index([x,y], (nb_rows,nb_cols))
    # move to x-1,y
    if x>0:
        if distmap[x-1,y]>cavern_map[x-1,y]+distmap[x,y] and not visited[x-1,y]:
            distmap[x-1,y]=cavern_map[x-1,y]+distmap[x,y]
            originmap[x-1,y]=np.ravel_multi_index([x,y], (nb_rows,nb_cols))
    # move to x,y+1
    if y < nb_cols-1:
        if distmap[x,y+1]>cavern_map[x,y+1]+distmap[x,y] and not visited[x,y+1]:
            distmap[x,y+1]=cavern_map[x,y+1]+distmap[x,y]
            originmap[x,y+1]=np.ravel_multi_index([x,y], (nb_rows,nb_cols))
    # move to x,y-1
    if y>0:
        if distmap[x,y-1]>cavern_map[x,y-1]+distmap[x,y] and not visited[x,y-1]:
            distmap[x,y-1]=cavern_map[x,y-1]+distmap[x,y]
            originmap[x,y-1]=np.ravel_multi_index([x,y], (nb_rows,nb_cols))

    visited[x,y]=True
    dismaptemp=distmap
    dismaptemp[np.where(visited)]=np.Infinity
    # now we find the shortest path so far
    minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
    x,y=minpost[0],minpost[1]
    if x==nb_rows-1 and y==nb_cols-1:
        finished=True
    count=count+1

#Start backtracking to plot the path  
mattemp=cavern_map.astype(float)
x,y=nb_rows-1,nb_cols-1
path=[]
mattemp[np.int(x),np.int(y)]=np.nan

while x>0.0 or y>0.0:
    path.append([np.int(x),np.int(y)])
    xxyy=np.unravel_index(np.int(originmap[np.int(x),np.int(y)]), (nb_rows,nb_cols))
    x,y=xxyy[0],xxyy[1]
    mattemp[np.int(x),np.int(y)]=np.nan
path.append([np.int(x),np.int(y)])


res = int(float(np.str(distmap[nb_rows-1,nb_cols-1])))

#print("part a: {}".format(res))
#puzzle.answer_a = res

print("part b: {}".format(res))
puzzle.answer_b = res