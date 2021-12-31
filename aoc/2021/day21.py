from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys

import attr
# a: 14:55
# b: 

puzzle = Puzzle(year=2021, day=21)

p_nb_wins = [0, 0]

@attr.s
class Player(object):
    position: int = attr.ib()
    score: int = attr.ib()

@attr.s
class Universe(object):
    players: list = attr.ib()
    winscore: int = attr.ib()
    dice: int = attr.ib()
    nb_rolls: int = attr.ib()
    player_index: int = attr.ib()
    winner: Player = attr.ib(init=False)
    looser: Player = attr.ib(init=False)

    def get_res(self):
        return self.looser.score * self.nb_rolls

    def play(self):
        while True:
            dice_sum = 0
            for _ in range(3):
                self.nb_rolls += 1
                self.dice = (self.dice + 1) % 100
                dice_sum += self.dice
            
            _player = self.players[self.player_index]
            _player.position = (_player.position + dice_sum) % 10
            _player.score += _player.position + 1

            if _player.score >= self.winscore:
                self.winner = _player
                p_nb_wins[self.player_index] += 1
                self.looser = self.players[(self.player_index + 1) % 2]
                break

            self.player_index = (self.player_index + 1) % 2

    def play_quantum(self, roll_number, dice_list):
        while True:
            if len(dice_list) != 3:
                for roll_number in range(roll_number, 3):
                    for x in [1, 2, 3]:
                        new_universe = Universe(deepcopy(self.players), self.winscore, self.dice, self.nb_rolls, self.player_index)
                        new_dice_list = deepcopy(dice_list)
                        new_dice_list.append(x)
                        new_universe.play_quantum(roll_number+1, new_dice_list)

            if len(dice_list) != 3:
                break

            roll_number = 0
            self.nb_rolls += 3
            
            dice_sum = sum(dice_list)
            dice_list = list()

            _player = self.players[self.player_index]
            _player.position = (_player.position + dice_sum) % 10
            _player.score += _player.position + 1

            if _player.score >= self.winscore:
                self.winner = _player
                p_nb_wins[self.player_index] += 1
                #print(p_nb_wins)
                self.looser = players[(self.player_index + 1) % 2]
                break

            self.player_index = (self.player_index + 1) % 2

# players = list()
# p1 = Player(3, 0)
# p2 = Player(7, 0)
# p1 = Player(7, 0)
# p2 = Player(1, 0)

# players.append(p1)
# players.append(p2)

# u1 = Universe(players, 1000, 0, 0, 0)
# u1.play()
# res = u1.get_res()

# print("part a: {}".format(res))
#puzzle.answer_a = res

players = list()
p1 = Player(3, 0)
p2 = Player(7, 0)
# p1 = Player(7, 0)
# p2 = Player(1, 0)

players.append(p1)
players.append(p2)

u2 = Universe(players, 5, 0, 0, 0)
u2.play_quantum(0, list())
res = max(p_nb_wins)

print("part b: {}".format(res))
#puzzle.answer_b = res