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

with open('ex15.txt') as infile:
   lines = infile.readlines()

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

nb_rows *= 5
nb_cols *= 5

# cavern = {
#     (0,0): 1,
#     (0,1): 8,
#     (1,0): 3,
#     (1,1): 8
# }

# nb_rows = 2
# nb_cols = 2

def get_num_node(r, c):
    return r*nb_cols + c

import networkx as nx
G = nx.Graph()

DR = [0, 1]
DC = [1, 0]

for r in range(nb_rows):
    for c in range(nb_cols):
        num_node_a = get_num_node(r, c)
        for d in range(2):
            rr = r+DR[d]
            cc = c+DC[d]
            if cc < nb_cols and rr < nb_rows:
                num_node_b = get_num_node(rr, cc)
                print(num_node_a, num_node_b)
                if r == 0 and c == 0:
                    _w = cavern[(rr, cc)]
                    G.add_edge(num_node_a, num_node_b, weight=_w)
                else:
                    _w = cavern[(rr, cc)]
                    G.add_edge(num_node_a, num_node_b, weight=_w)
                    G.add_edge(num_node_b, num_node_a, weight=_w)

#print(nx.shortest_path(G, 0, nx.number_of_nodes(G)-1, weight='weight'))
res = nx.shortest_path_length(G, 0, nx.number_of_nodes(G)-1, weight='weight')
print("part b: {}".format(res))
#puzzle.answer_b = res