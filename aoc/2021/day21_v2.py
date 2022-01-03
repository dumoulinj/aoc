from copy import copy, deepcopy
from collections import defaultdict 

# a: 14:55
# b: 


WINSCORE = 21

KNOWN_STATES = dict()

scores = list() 

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            s = i + j + k
            scores.append(s)

def play_quantum(p1, s1, p2, s2, player_index):
    nb_wins = (0, 0)

    if player_index == 1:
        if s1 >= WINSCORE:
            return (1, 0)
    else:
        if s2 >= WINSCORE:
            return (0, 1)

    players_hash = (p1, s1, p2, s2, player_index)
    if players_hash in KNOWN_STATES:
        return KNOWN_STATES[players_hash]

    for d_score in scores:
        if player_index == 0:
            _p1 = (p1 + d_score) % 10
            _s1 = s1 + _p1 + 1
            _nb_wins = play_quantum(_p1, _s1, p2, s2, (player_index + 1) % 2)
        else:
            _p2 = (p2 + d_score) % 10
            _s2 = s2 + _p2 + 1
            _nb_wins = play_quantum(p1, s1, _p2, _s2, (player_index + 1) % 2)
        
        nb_wins = (nb_wins[0] + _nb_wins[0], nb_wins[1] + _nb_wins[1])
    
    players_hash = (p1, s1, p2, s2, player_index)
    KNOWN_STATES[players_hash] = nb_wins

    return nb_wins


#wins = play_quantum(3, 0, 7, 0, 0) 
wins = play_quantum(7, 0, 1, 0, 0) 

print(wins)
res = max(wins)

print("part b: {}".format(res))
#puzzle.answer_b = res